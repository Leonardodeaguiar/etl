from typing import Dict
import requests


class HttpRequester:
    def __init__(self) -> None:
        self.__url = "https://web.archive.org/web/20120916140934/http://www.nga.gov/collection/anZ1.htm"

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url, timeout=200)
        return {"status_code": response.status_code, "html": response.text}  # type: ignore
