from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
from projekt1.model.company import Company


class TestCompanyFromDict:
    def test_when_data_is_correct(self):
        company_data_ex = JsonDataLoader().load('tests/data_test/companies_test.json')
        company_test = Company.from_dict(company_data_ex['companies'][0])
        assert company_test == Company('CT1', 'AlphaT', 'CAT1')
