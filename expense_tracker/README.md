# Expense Tracker

This is a simple command line expense tracking application written in Python.

## Usage

```
python expense_tracker.py add "Lunch" 12.50 food
python expense_tracker.py list
python expense_tracker.py summary
```

The amount should be provided as a number (do not quote it).

Expenses are stored in `expenses.json` in the same directory.

## Web Interface

A basic web interface is available using Flask. Run it with:

```
python -m expense_tracker.web_ui
```

Then open `http://localhost:5000` in your browser to view and add expenses.

