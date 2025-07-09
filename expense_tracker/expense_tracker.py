import json
import sys
from pathlib import Path
from collections import defaultdict

DATA_FILE = Path(__file__).with_name('expenses.json')


def load_expenses():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)


def add_expense(description, amount, category):
    expenses = load_expenses()
    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)
    save_expenses(expenses)
    print('Added expense:', expense)


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print('No expenses recorded.')
        return
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp['description']} - ${exp['amount']} [{exp['category']}]")


def summarize_expenses():
    expenses = load_expenses()
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp['category']] += float(exp['amount'])
    for category, total in summary.items():
        print(f"{category}: ${total}")


def print_help():
    print('Usage: python expense_tracker.py [add|list|summary] ...')
    print('Commands:')
    print('  add <description> <amount> <category>')
    print('  list')
    print('  summary')


def main(args):
    if not args:
        print_help()
        return
    command = args[0]
    if command == 'add' and len(args) == 4:
        _, desc, amount, category = args
        add_expense(desc, amount, category)
    elif command == 'list':
        list_expenses()
    elif command == 'summary':
        summarize_expenses()
    else:
        print_help()


if __name__ == '__main__':
    main(sys.argv[1:])
