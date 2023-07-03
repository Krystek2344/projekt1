from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
from abc import abstractmethod, ABC
from typing import Any
import re


class Validator(ABC):
    @abstractmethod
    def validate(self, json_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
        pass

# todo.1 Postarać się wyznaczyć metodę do ogarnięcia podwajających się sprawdzeń (napisy). Czy jest to
#     dobra praktyka, żeby tyle sprawdzeń robić (na całym pliku) - co jak będzie kilkaset wierszy/pozycji??
#     Czy lepiej zrobiź sobie tak jak w przypadku employees_constrains i wywalić regexy (companies, employees i address)
#     do pliku i wyciągać sobie regexy i wyszukiwać po kluczu? Walidacja maila?

class RegexEmployeesJsonDataValidator(Validator):

    def validate(self, json_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
        employees_constrains = {
            'userId': '^[E]\d+$',
            'name': '^[A-Z]+$',
            'surname': '^[A-Z]+$',
            'job': '^[A-Z]+$',
            'age': '^\d+$',
            'experience': '^\d+$',
            'salary': '^\d+\.\d{2}$',
            'rating': '^\d+\.\d{1}$',
            'email': '^[\w\.-]+@[\w\.-]+\.\w+$',
            'companyId': '^[C]\d+$'
        }

        errors = {}

        # for data in json_data['employees']:
        #     # print(data)
        #     for k, v in data.items():
                # print(f'K {k} v {v}')
        if not json_data['employees']['userId']:
            errors['userId'] = 'Employee json data must contain id'
        elif not re.match(r'^[E]\d+$', json_data['userId']):
            errors['userId'] = 'Employee id must be a number'

        if not json_data['name']:
            errors['name'] = 'Employee json data must contain name'
        elif not re.match(r'^[A-Z]+$', json_data['name']):
            errors['name'] = 'Employee name must contain only upper letters'
            # str(data['name']).upper()

        if not json_data['surname']:
            errors['surname'] = 'Employee json data must contain surname'
        elif not re.match(r'^[A-Z]+$', json_data['surname']):
            errors['surname'] = 'Employee surname must contain only upper letters'
            # str(data['surname']).upper()

        if not json_data['job']:
            errors['job'] = 'Employee json data must contain job name'
        elif not re.match(r'^[A-Z]+$', json_data['job']):
            errors['surname'] = 'Employee job name must contain only upper letters'
            # str(data['job']).upper()

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
            # round(float(data['salary']), 1)
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
            errors['companyId'] = 'Employee email must be a string'

        if len(errors) != 0:
            raise ValueError(errors_to_str(errors))

        return json_data





def errors_to_str(errors: dict[str, str]) -> str:
    return ', '.join([f'{k}: {v}' for k, v in errors.items()])

