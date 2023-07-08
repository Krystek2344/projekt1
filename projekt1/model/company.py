from dataclasses import dataclass
from typing import Self, Any

@dataclass
class Company:
    companyId: str
    name: str
    addressId: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return Company(str(data['companyId']), str(data['name']), str(data['addressId']))
