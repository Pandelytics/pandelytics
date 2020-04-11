import requests
from bs4 import BeautifulSoup
import json

def whoRonaNews():
    #get page text using request and beautifulsoup
    page = requests.get("https://www.who.int/news-room/detail/search-results?indexCatalogue=genericsearchindex1&searchQuery=covid-19&wordsMode=AllWords") 
    bsObj = BeautifulSoup(page.text, 'html.parser')
    #get the page to all data
    weblink = bsObj.find('div',class_ = 'sf-search-results--container media-list')
    
    #get list of data
    articlelink = weblink.find_all(class_='link-container')
    articleheader= weblink.find_all(class_ ='heading')
    articletime = weblink.find_all(class_ = 'timestamp')
    thearticle = weblink.find_all(class_ = 'text-underline')
    
    #get the link of all artiles add to linklist
    linklist = []
    for i in range(len(articlelink)):
        llist = articlelink[i].get('href')
        linklist.append(llist)
     #get the list of all articles header add to headertestlist   
        headertextlist = []
        for i in range(len(articleheader)):
            htlist = articleheader[i].getText()
            headertextlist.append(htlist)
     #get the list of the each artiles 
            timelist = []    
            for i in range(len(articletime)):
                tlist = articletime[i].getText()
                timelist.append(tlist)
       #the list of all main-artiles body          
                articlelist = []
                for i in range(len(thearticle)):
                    text = thearticle[i].getText()
                    articlelist.append(text)
                    
    #create dictionary for the lists
    
    data = dict()
        
    data['articlelink'] = linklist
    data['the-header'] = headertextlist
    data['article-released-time'] = timelist 
    data['the-main-article'] = articlelist

       #convert list to json
    data_json = json.dumps(data)

    return (data_json)