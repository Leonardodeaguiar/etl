import datetime
from src.stages.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {
            "first_name": "Giuseppe",
            "last_name": "Zanini-Viola",
            "surname": None,
            "artist_id": "11597",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=11597",
            "extraction_date": datetime.date(2023, 8, 23),
        },
        {
            "first_name": "Giampietro",
            "last_name": "Zanotti",
            "surname": None,
            "artist_id": "11631",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=11631",
            "extraction_date": datetime.date(2023, 8, 23),
        },
        {
            "first_name": "Wou-Ki",
            "last_name": "Zao",
            "surname": None,
            "artist_id": "3427",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=3427",
            "extraction_date": datetime.date(2023, 8, 23),
        },
        {
            "first_name": "Wou-Ki",
            "last_name": "Zao",
            "surname": None,
            "artist_id": "3427",
            "link": "https://web.archive.org/web/20120916140934/http://www.nga.gov/cgi-bin/tsearch?artistid=3427",
            "extraction_date": datetime.date(2023, 8, 23),
        },
    ]
)
