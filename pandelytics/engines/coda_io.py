"""@desc
		Parser for NCDC results
"""

from pandelytics.engines.base import Base


class Data(Base):
    """
    Searches Google for string
    """
    name = "Coda.io"
    url = "https://coda.io/@atc/coronavirus-2019-ncov-updates-resources/country-data-6"

    def parse_soup(self, soup):
        """
        Parses Google Search Soup for results
        """

        # get a list of each column data
        country = soup.select('[data-column-id = "c-E-YMA09Lx_"]')

        last_update_date = soup.select('[data-column-id = "c-cXnlNCXBHV"]')
        confirmed_cases = soup.select('[data-column-id = "c-ubb_Gf1NEQ"]')
        doubling_rate = soup.select('[data-column-id = "c-WBbk86F0ko"]')
        days_since_crossing_threshold = soup.select(
            '[data-column-id = "c-5z5Hfd-vNY"]')

        recovered = soup.select('[data-column-id = "c-i4EEVOMVxQ"]')
        percent_recovered = soup.select('[data-column-id = "c-BYew3BSK4f"]')

        deaths = soup.select('[data-column-id = "c-OduUQXvRBG"]')
        mortality_rate = soup.select('[data-column-id = "c-odu_uQXv_rBG"]')
        cases_per_million = soup.select('[data-column-id = "c-36sbn16eu_r"]')

        total_tests = soup.select('[data-column-id = "c-l_ya_pEb4xut"]')
        tests_per_million = soup.select('[data-column-id = "c-_d_r2m_fo_zBb"]')
        positivity_rate = soup.select('[data-column-id = "c-q_uJQUJGa_g6"]')

        # create a list of dictionaries for each row
        data = []
        print(len(country), len(last_update_date), len(confirmed_cases), len(doubling_rate),
              len(days_since_crossing_threshold), len(
                  recovered), len(percent_recovered),
              len(deaths), len(mortality_rate), len(
                  cases_per_million), len(total_tests),
              len(tests_per_million), len(positivity_rate)
              )
        for i in range(2, len(country)):
            rdict = {}
            rdict['Country'] = country[i].getText()
            rdict['Last Update Date'] = last_update_date[i].getText()
            rdict['Confirmed Cases'] = confirmed_cases[i].getText()
            rdict['Doubling rate'] = doubling_rate[i].getText()
            rdict['Days since crossing threshold'] = days_since_crossing_threshold[i].getText()
            rdict['Recovered'] = recovered[i].getText()
            rdict['Recovered %'] = percent_recovered[i].getText()
            rdict['Deaths'] = deaths[i].getText()

            data.append(rdict)
        return data
