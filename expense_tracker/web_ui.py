from flask import Flask, render_template_string, request, redirect, url_for
from collections import defaultdict

from .expense_tracker import load_expenses, add_expense

app = Flask(__name__)

INDEX_TEMPLATE = """
<h1>Expenses</h1>
<a href="{{ url_for('add') }}">Add Expense</a> |
<a href="{{ url_for('summary') }}">Summary</a>
<ul>
{% for e in expenses %}
  <li>{{ e['description'] }} - ${{ e['amount'] }} [{{ e['category'] }}]</li>
{% else %}
  <li>No expenses recorded.</li>
{% endfor %}
</ul>
"""

ADD_TEMPLATE = """
<h1>Add Expense</h1>
<form method="post">
  Description: <input type="text" name="description"><br>
  Amount: <input type="number" step="0.01" name="amount"><br>
  Category: <input type="text" name="category"><br>
  <input type="submit" value="Add">
</form>
<a href="{{ url_for('index') }}">Back</a>
"""

SUMMARY_TEMPLATE = """
<h1>Summary by Category</h1>
<a href="{{ url_for('index') }}">Back to Expenses</a>
<ul>
{% for category, total in summary.items() %}
  <li>{{ category }}: ${{ "%.2f"|format(total) }}</li>
{% else %}
  <li>No expenses recorded.</li>
{% endfor %}
</ul>
"""

@app.route('/')
@app.route('/expenses')
def index():
    expenses = load_expenses()
    return render_template_string(INDEX_TEMPLATE, expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        desc = request.form.get('description', '')
        amount = request.form.get('amount', '')
        category = request.form.get('category', '')
        if desc and amount and category:
            add_expense(desc, amount, category)
        return redirect(url_for('index'))
    return render_template_string(ADD_TEMPLATE)

@app.route('/summary')
def summary():
    expenses = load_expenses()
    totals = defaultdict(float)
    for e in expenses:
        totals[e['category']] += float(e['amount'])
    return render_template_string(SUMMARY_TEMPLATE, summary=totals)


def main():
    app.run()


if __name__ == '__main__':
    main()
