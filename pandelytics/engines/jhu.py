"""@desc
		Parser for John Hopkins University results
"""
from pandelytics.engines.base import Base
import pandas as pd
import json
import requests
from io import StringIO

class Data(Base):
    """
    Searches Repository for string
    """
    name = "JHU"
    urls = {
        "total-cases": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        "recoveries": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
    }
    url = urls["total-cases"]


    def request(self, url, **kwargs):
        """
        Overrides base class request by allowing selection of 
        url by setting kwargs return_type

        :rtype: string
        :param url: URL to pull it's source code
        :return: html source code of a given URL.
        """
        return_type = kwargs.get("return_type")
        if return_type in self.urls.keys():
            url = self.urls[return_type]
        return super(Data, self).request(url)

    def parse_soup(self, soup):
        """
        Parses the dataframe to json

        :return: dict 
        """
        csv_text = soup.find('p').getText()
        df = pd.read_csv(StringIO(csv_text), sep=",")
        return json.loads(df.to_json(orient='index'))
