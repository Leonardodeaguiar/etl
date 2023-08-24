from src.stages.contracts.mock.transform_contract import transform_contract_mock
from src.errors.load_error import LoadError
from .load_data import LoadData


class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_attributes = []

    def insert_artist(self, data):
        self.insert_artist_attributes.append(data)


def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)  # type: ignore

    load_data.load(transform_contract_mock)
    assert repo.insert_artist_attributes == transform_contract_mock.load_content


def test_load_error():
    repo = RepositorySpy()
    load_data = LoadData(repo)  # type: ignore

    try:
        load_data.load("erro")  # type: ignore
    except Exception as exception:
        assert isinstance(exception, LoadError)
