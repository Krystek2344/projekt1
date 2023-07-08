from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
import pytest
from typing import Any


class TestRegexEmployeesJsonDataValidator:
    def test_validate(self):
        test_data = JsonDataLoader().load('tests/data_test/employees_test.json')['employees'][0]

        assert test_data['userId'] == 'ET1'
        assert test_data['companyId'] == 'C1'

  # def test_check_json_file_data_with_regex(self):
  #     test_data = JsonDataLoader().load('tests/data_test/employees_test.json')
  #     pass
