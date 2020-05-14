from pandelytics.engines.base import Base

class News(Base):
    name = "NCDC"
    url = "https://ncdc.gov.ng/news/press"

    def parse_soup(self, soup):
        data = soup.findAll('div',class_='col-sm-10')
        results = []
        for entry in data:
            result = {}
            result["title"]= entry.h3.text
            result["link"]= (self.url)+entry.find("a").get("href")
            result["details"]= entry.article.text
            # result["img"]  = entry.img.text
            result["date"]= entry.h4.text
            results.append(result)
        

        return results

