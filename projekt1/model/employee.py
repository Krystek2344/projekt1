from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Employee:
    name: str
    surname: str
    job: str
    age: str
    experience: str
    salary: Decimal
    workEvaluation: str
    email: str
