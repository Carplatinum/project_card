import pytest
from unittest.mock import patch
from src.utils import read_json_file

@pytest.fixture
def json_file(tmp_path):
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as file:
        json.dump([{"id": 1}, {"id": 2}], file)
    return file_path