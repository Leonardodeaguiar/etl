from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content=[
        {
            "name": "Zanini-Viola, Giuseppe",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=11597",
        },
        {
            "name": "Zanotti, Giampietro",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=11631",
        },
        {
            "name": "Zao Wou-Ki",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=3427",
        },
        {
            "name": "Zas-Zie",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/collection/anZ2.htm",
        },
        {
            "name": "Zie-Zor",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/collection/anZ3.htm",
        },
    ],
    extraction_date=date.today(),
)
