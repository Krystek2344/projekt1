from projekt1.loader.file_loader.json_and_text_loader import JsonDataLoader
import pytest


class TestJsonDataLoaderWithIncorrectPath:
    def test_when_path_has_incorrect_extension(self):
        with pytest.raises(AttributeError) as e:
            JsonDataLoader().load('datajson/employees.txt')
        assert 'File has incorrect extension' == str(e.value)

    def test_when_file_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            JsonDataLoader().load('tests/data_test/employes_test.json')
        assert str(e.value).startswith('File not found')


class TestJsonDataLoaderWithIncorrectContent:
    def test_file_with_content(self):
        result = JsonDataLoader().load('tests/data_test/employees_test.json')
        assert 1 == len(result)
        assert 'employees' in result
