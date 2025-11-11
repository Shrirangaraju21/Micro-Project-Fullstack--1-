# Expense Tracker (Micro-Project-Fullstack--1-)

Expense Tracker is a lightweight Django web application for logging and visualizing personal expenses. It's designed for easy local setup (SQLite), straightforward CRUD operations for expenses, and quick visual insights using Chart.js. This repository contains the Django project and a single `tracker` app with templates, static assets, and migrations to get you started.

## Key features
- User registration and login
- Add, edit, and delete expenses with amount, date, category, and notes
# Expense Tracker — Micro-Project (Fullstack)

This repository implements a small but complete Expense Tracker built with Django. The app is intended as a learning/full‑stack microproject and provides personal expense management, category grouping, and quick visual analytics. It is intentionally lightweight so you can run it locally with minimal setup (SQLite) and extend it for production use.

## Highlights

- Purpose: let users record expenses, categorize them, and visualize spending by category.
- Simple authentication workflow: register and log in (Django's built-in auth). Each user sees only their own expenses.
- Visualizations: category totals are shown using Chart.js on the `category_chart` view.
- Clean, responsive templates and a central stylesheet at `tracker/static/style.css`.

## Data model (brief)

- Expense
	- `user` (ForeignKey to Django `User`) — owner of the expense
	- `title` (CharField) — short description
	- `amount` (FloatField) — expense amount
	- `category` (CharField) — category label (e.g., Food, Transport)
	- `date` (DateField) — expense date

The model lives in `tracker/models.py`. The app uses a simple, denormalized category string which keeps the schema flexible and easy to change; you can normalize categories into a separate model later if needed.

## Important routes / views

- `/` (index) — dashboard listing the user's expenses and total spending. Template: `tracker/index.html`.
- `/add/` — add a new expense using `ExpenseForm`. Template: `tracker/add_expense.html`.
- `/edit/<id>/` — edit an existing expense (permission enforced, only owner can edit). Template: `tracker/edit_expense.html`.
- `/delete/<id>/` — deletes the specified expense (owner-only).
- `/chart/` — category aggregation view that renders `tracker/category_chart.html` and injects JSON-safe arrays for Chart.js.
- `/register/` — user registration (uses Django's `UserCreationForm`). Template: `tracker/register.html`.

See `tracker/views.py` for implementation details.

## Installation & quick run (Windows / PowerShell)

1. Clone and open the project directory:

```powershell
git clone <your-repo-url>
cd C:\Users\shrir\Desktop\shree\expense__tracker
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
# If `requirements.txt` is missing, install Django directly:
pip install django==5.2.8
```

4. Run migrations and create a superuser (optional):

```powershell
python manage.py migrate
python manage.py createsuperuser
```

5. Start the development server:

```powershell
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to use the app.

## Development notes

- Templates are under `tracker/templates/tracker/`. The app uses Django template inheritance with `base.html`.
- Static CSS is in `tracker/static/style.css`. If you change CSS during development, reload the browser to see updates.
- Forms: `tracker/forms.py` defines `ExpenseForm` (ModelForm) with a date widget for the `date` field.
- Charts: `tracker/category_chart.html` receives JSON-encoded arrays (`categories`, `totals`, `colors`) and uses Chart.js to render a doughnut chart.

## Tests

There are no automated tests included yet. Recommended minimal tests to add:

- Model tests for `Expense` (creation, string representation).
- View tests for permission enforcement (only owner can edit/delete) and for correct aggregation in `category_chart`.




## Security & privacy notes

- This project is for learning/demo purposes. If deploying to production, switch from SQLite to PostgreSQL, add proper `ALLOWED_HOSTS`, configure secret management (don't keep `SECRET_KEY` in source control), enable HTTPS, and review user data policies.

## Teame Members 
Team Number 1
- Shriranagaraju D    4MC23IS103
- Purushotham T P     4MC23IS091
- Prasanna Kumar K S  4MC23IS075
- Saketh Devang H R   4MC23IS083
- Harish J Doddamani  4MC22IS039
