from pandelytics.engines.base import Base


class News(Base):
    name = "WHO"
    url = "https://www.who.int/news-room/detail/search-results?"

    def get_params(self):
        params = {}
        params["indexCatalogue"] = "genericsearchindex1"
        params["searchQuery"] = "covid-19"
        params["wordsMode"] = "AllWords"

        return params

    def parse_soup(self, soup):
        # get the page to all data
        weblink = soup.find(
            'div', class_='sf-search-results--container media-list')

        # get list of data
        links = weblink.find_all(class_='link-container')
        headers = weblink.find_all(class_='heading')
        times = weblink.find_all(class_='timestamp')
        details = weblink.find_all(class_='text-underline')

        data = []
        for i in range(len(links)):
            rdict = {}
            rdict["header"] = headers[i].getText()
            rdict["link"] = links[i].get('href')
            rdict["time"] = times[i].getText()
            rdict["details"] = details[i].getText()
            data.append(rdict)

        return data
