from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
from abc import abstractmethod, ABC
from typing import Any
import re


class Validator(ABC):
    @abstractmethod
    def validate(self, json_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
        pass


class RegexEmployeesJsonDataValidator(Validator):

    def validate(self, json_data: dict[str, Any]) -> dict[str, Any]:

        errors = {}

        if not json_data['userId']:
            errors['userId'] = 'Employee json data must contain id'
        elif not re.match(r'^[E]\d+$', json_data['userId']):
            errors['userId'] = 'Employee id must be a number'

        if not json_data['name']:
            errors['name'] = 'Employee json data must contain name'
        elif not re.match(r'^[A-Z]+$', json_data['name']):
            errors['name'] = 'Employee name must contain only upper letters'

        if not json_data['surname']:
            errors['surname'] = 'Employee json data must contain surname'
        elif not re.match(r'^[A-Z]+$', json_data['surname']):
            errors['surname'] = 'Employee surname must contain only upper letters'

        if not json_data['job']:
            errors['job'] = 'Employee json data must contain job name'
        elif not re.match(r'^[A-Z]+$', json_data['job']):
            errors['job'] = 'Employee job name must contain only upper letters'

        if not json_data['age']:
            errors['age'] = 'Employee json data must contain age'
        elif not re.match(r'^\d+$', json_data['age']):
            errors['age'] = 'Customer age must be a number'

        if not json_data['experience']:
            errors['experience'] = 'Employee json data must contain experience'
        elif not re.match(r'^\d+$', json_data['experience']):
            errors['experience'] = 'Customer experience must be a number'

        if not json_data['salary']:
            errors['salary'] = 'Employee json data must contain salary'
        elif not re.match(r'^\d+\.\d{2}$', json_data['salary']):
            errors['salary'] = 'Customer salary must be a float number'

        if not json_data['rating']:
            errors['rating'] = 'Employee json data must contain rating'
        elif not re.match(r'^\d+$', json_data['rating']):
            errors['rating'] = 'Customer rating must be a number'

        if not json_data['rating']:
            errors['rating'] = 'Employee json data must contain rating'
        elif not re.match(r'^\d+$', json_data['rating']):
            errors['rating'] = 'Customer rating must be a number'

        if not json_data['email']:
            errors['email'] = 'Employee json data must contain email'
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', json_data['email']):
            errors['email'] = 'Employee email must be a string'

        if not json_data['companyId']:
            errors['companyId'] = 'Employee json data must contain companyId'
        elif not re.match(r'^[C]\d+$', json_data['companyId']):
            errors['companyId'] = 'Employee company ID must be a string'

        if len(errors) != 0:
            raise ValueError(self._errors_to_str(errors))

        return json_data

    def _errors_to_str(self, errors: dict[str, str]) -> str:
        return ', '.join([f'{k}: {v}' for k, v in errors.items()])

    @staticmethod
    def check_json_employee_file_data_with_regex(json_file_data: dict[str, list[dict[str, Any]]]) -> dict[str, list[dict[str, Any]]]:
        pass

