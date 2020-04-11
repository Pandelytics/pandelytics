"""@desc
		Base classes inherited by every Analytic Engine
"""

from abc import ABCMeta, abstractmethod
from urllib.parse import urlencode, urlparse

import requests
from bs4 import BeautifulSoup

from pandelytics import utils


class Base:

    __metaclass__ = ABCMeta

    """
    Search base to be extended by parsers
    """
    # Summary of engine
    summary = None
    # Search Engine Name
    name = None
    # Search Engine unformatted URL
    url = None
    _parsed_url = None

    def get_params(self):
        """ This  function should be overwritten to return a dictionary of query params"""
        return {}

    @property
    def parsed_url(self):
        """ Return URL """
        if not self._parsed_url:
            params = self.get_params()
            if params:
                self.url += urlencode(params)

            self._parsed_url = urlparse(self.url)
        return self._parsed_url

    @abstractmethod
    def parse_soup(self, soup):
        """
        Defines the results contained in a soup
        """
        raise NotImplementedError("subclasses must define method <parse_soup>")

    def get_headers(self):
        """ Get Headers for requests """
        headers = {
            "Cache-Control": 'no-cache',
            "Connection": "keep-alive",
            "User-Agent": utils.rand_user_agent(),
        }
        return headers

    def request(self, url):
        """
        Returns the source code of a webpage.

        :rtype: string
        :param url: URL to pull it's source code
        :return: html source code of a given URL.
        """
        try:
            response = requests.get(url, headers=self.get_headers())
            html = response.text
        except Exception as exc:
            raise Exception('ERROR: {}\n'.format(exc))
        return str(html)

    def response(self, **kwargs):
        """ Get results from soup"""

        html = self.request(self.parsed_url.geturl())
        soup = BeautifulSoup(html, 'lxml')

        results = self.parse_soup(soup, **kwargs)
        return results
