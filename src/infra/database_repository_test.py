import pytest
from src.stages.contracts.mock.transform_contract import transform_contract_mock
from .database_connector import DatabaseConnector
from .database_repository import DatabaseRepository


pytest.mark.skip(reason="No need to inser data in database")


def test_insert_artist():
    DatabaseConnector.connect()
    database_repo = DatabaseRepository()

    database_repo.insert_artist(transform_contract_mock.load_content[0])
