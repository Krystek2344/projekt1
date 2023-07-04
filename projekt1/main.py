from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
from projekt1.validator.validator import RegexEmployeesJsonDataValidator
import json
import re


def main() -> None:

    employees_data = JsonDataLoader().load('../datajson/employees.json')


    emp1 = len(employees_data['employees'])
    # print(RegexEmployeesJsonDataValidator().validate(employees_data['employees'][0]))
    # RegexEmployeesJsonDataValidator().validate(emp1)
    print(emp1)

if __name__ == '__main__':
    main()
