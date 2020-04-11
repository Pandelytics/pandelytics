from pandelytics.engines.base import Base


class News(Base):
    name = "NCDC"
    url = "https://ncdc.gov.ng/news/press"

    def parse_soup(self, soup):
        links = soup.findAll('a', {'class': 'white-text'})
        titles = soup.select("article h3")
        details = soup.find_all('article')

        data = []
        for i in range(0, len(links)):
            rdict = {}
            rdict['title'] = titles[i].get_text()
            rdict['detail'] = details[i].get_text()
            rdict['link'] = links[i].get_text()
            data.append(rdict)
        return data
