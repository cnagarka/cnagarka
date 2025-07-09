from collections import defaultdict

def add_expense(expenses, amount, category, description=""):
    """Add an expense entry to the list of expenses."""
    entry = {
        "amount": float(amount),
        "category": category,
        "description": description,
    }
    expenses.append(entry)
    return entry


def list_expenses(expenses):
    """Return the list of recorded expenses."""
    return list(expenses)


def summarize_expenses(expenses):
    """Return a summary of total expenses per category."""
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += float(expense["amount"])
    return dict(summary)
