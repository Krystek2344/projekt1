from dataclasses import dataclass


@dataclass
class CompanyAddress:
    addressId: str
    city: str
    street: str
    number: str
    country: str
