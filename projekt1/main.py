from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
from projekt1.validator.validator import RegexEmployeesJsonDataValidator
import json
import re


def main() -> None:

    # employees_data = JsonDataLoader().load('../tests//data_test/employees_test.json')
    employees_data = JsonDataLoader().load('../datajson/employees.json')


    emp1 = employees_data
    print(emp1['employees'][0])


if __name__ == '__main__':
    main()
