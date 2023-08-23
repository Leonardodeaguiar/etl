from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError
from .extract_html import ExtractHtml


def test_extract():
    http_requester = HttpRequester()
    http_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, http_collector)
    response = extract_html.extract()
    print()
    print(response)

    assert isinstance(response, ExtractContract)


def test_extract_error():
    http_requester = "Vai dar Errado"
    http_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, http_collector)

    try:
        extract_html.extract()
    except Exception as exception:
        assert isinstance(exception, ExtractError)
        print(exception)
