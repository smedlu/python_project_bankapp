import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import tempfile
import json
import pandas as pd
import pytest
from src.project_bankapp.utils import get_transactions_data

def test_get_transactions_data_json_success():
    data = [{"a": 1}, {"a": 2}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        file_path = f.name
    try:
        result = get_transactions_data(file_path)
        assert result == data
    finally:
        os.remove(file_path)

def test_get_transactions_data_json_not_list():
    data = {"a": 1}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        file_path = f.name
    try:
        result = get_transactions_data(file_path)
        assert result == []
    finally:
        os.remove(file_path)

def test_get_transactions_data_csv_success():
    data = pd.DataFrame([{"a": 1}, {"a": 2}])
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        data.to_csv(f.name, sep=';', index=False)
        file_path = f.name
    try:
        result = get_transactions_data(file_path)
        assert result == [{"a": 1}, {"a": 2}]
    finally:
        os.remove(file_path)

def test_get_transactions_data_xlsx_success():
    data = pd.DataFrame([{"a": 1}, {"a": 2}])
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as f:
        data.to_excel(f.name, index=False)
        file_path = f.name
    try:
        result = get_transactions_data(file_path)
        assert result == [{"a": 1}, {"a": 2}]
    finally:
        os.remove(file_path)

def test_get_transactions_data_file_not_found():
    result = get_transactions_data("non_existent_file.json")
    assert result == []

def test_get_transactions_data_unknown_ext():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("test")
        file_path = f.name
    try:
        result = get_transactions_data(file_path)
        assert result == []
    finally:
        os.remove(file_path)

