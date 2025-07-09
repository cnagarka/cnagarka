import json
from pathlib import Path
import expense_tracker.expense_tracker as et


def test_invalid_amount_rejected(tmp_path, capsys, monkeypatch):
    data_file = tmp_path / 'expenses.json'
    monkeypatch.setattr(et, 'DATA_FILE', data_file)
    et.add_expense('item', 'not-a-number', 'misc')
    out = capsys.readouterr().out
    assert 'Invalid amount' in out
    assert not data_file.exists()
