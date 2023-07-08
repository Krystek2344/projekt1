from projekt1.model.employee import Employee
from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
import pytest


# todo zmienić nazwę ?? Na Dict?? TestEmployeeFromDict??
class TestEmployeeFromText:
    # def test_when_data_is_not_correct(self):
    #     with pytest.raises(AttributeError) as e:
    #         Employee.from_dict({'...': '...'})
    #     assert str(e.value).startswith('Data is not correct')

    def test_when_data_is_correct(self):
        emp_ex = JsonDataLoader().load('tests/data_test/employees_test.json')
        employee_test = Employee.from_dict(emp_ex['employees'][0])
        assert employee_test == Employee('ET1', 'ADAM', 'Kowal', 'Dev', '20', '1', '3000', '4', 'kow@mail.com', 'C1')
