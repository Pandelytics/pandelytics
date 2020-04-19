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

class Data(Base):
    name = "NCDC"
    url = 'http://covid19.ncdc.gov.ng/'

    def parse_soup(self, soup):
        naija_summary = soup.select('table#custom1')
        state_summary = soup.select('table#custom3')

        lines = naija_summary[0].find_all('tr')
        gen_dict = {}
        for line in lines:
            tds = line.find_all('td')
            label = tds[0].getText()
            gen_dict[label] = tds[1].getText().replace('\n', '')

        headers = state_summary[0].find_all('th')
        keys = []
        for header in headers:
            key = header.getText().replace('\r\n                        ', '')
            keys.append(key)

        rows = state_summary[0].find_all('tr')
        state_data = []
        for i in range(1, len(rows)):
            tds = rows[i].find_all('td')
            sdict = {}
            for j in range(5):
                sdict[(keys[j])] = tds[j].getText().replace('\n', '')
            state_data.append(sdict)

        return(gen_dict, state_data)