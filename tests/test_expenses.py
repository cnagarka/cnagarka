import expenses


def test_add_expense():
    records = []
    entry = expenses.add_expense(records, 10.0, "food", "lunch")
    assert len(records) == 1
    assert records[0] == entry
    assert entry["amount"] == 10.0
    assert entry["category"] == "food"
    assert entry["description"] == "lunch"


def test_list_expenses():
    records = []
    expenses.add_expense(records, 5, "travel")
    expenses.add_expense(records, 2, "food")
    listed = expenses.list_expenses(records)
    assert listed == records


def test_summarize_expenses():
    records = []
    expenses.add_expense(records, 5, "travel")
    expenses.add_expense(records, 10, "food")
    expenses.add_expense(records, 7.5, "food")
    summary = expenses.summarize_expenses(records)
    assert summary == {"travel": 5.0, "food": 17.5}
