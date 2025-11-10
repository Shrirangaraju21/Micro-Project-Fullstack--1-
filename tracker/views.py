from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'tracker/index.html', {'expenses': expenses, 'total': total})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)  # ✅ Removed user argument
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # ✅ Still needed to assign ownership
            expense.save()
            return redirect('index')
    else:
        form = ExpenseForm()  # ✅ Removed user argument
    return render(request, 'tracker/add_expense.html', {'form': form})

@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/edit_expense.html', {'form': form})

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('index')

@login_required
def category_chart(request):
    data = Expense.objects.filter(user=request.user).values('category').annotate(total=Sum('amount')).order_by('-total')
    categories = [entry['category'] for entry in data]
    totals = [entry['total'] for entry in data]
    base_colors = ['#0d6efd', '#198754', '#ffc107', '#dc3545', '#6f42c1', '#20c997', '#fd7e14', '#0dcaf0', '#6610f2', '#6c757d']
    colors = base_colors[:len(categories)]
    return render(request, 'tracker/category_chart.html', {
        'categories': categories,
        'totals': totals,
        'colors': colors
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})