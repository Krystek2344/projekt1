from projekt1.validator.validator import RegexEmployeesJsonDataValidator
from dataclasses import dataclass
from typing import Self, Any



@dataclass
class Employee:
    userId: str
    name: str
    surname: str
    job: str
    age: str
    experience: str
    salary: str
    rating: str
    email: str
    companyId: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        # if not RegexEmployeesJsonDataValidator().validate(data):
        #     raise AttributeError('Data is not correct')
        return Employee(str(data['userId']), str(data['name']), str(data['surname']), str(data['job']), str(data['age']),\
         str(data['experience']), str(data['salary']), str(data['rating']), str(data['email']), str(data['companyId']))
