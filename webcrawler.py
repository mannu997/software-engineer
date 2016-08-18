import bs4
import urllib2
import re

def get_number(text):
    regex = re.compile(r'\d+')
    num = regex.findall(text)
    num = [int(i) for i in num]
    return max(num)

def crawler(keyword , pagenumber = None):
    if pagenumber == None :
        url = 'http://www.shopping.com/products?KW=%s'%(keyword)
        html = urllib2.urlopen(url)
        soup = bs4.BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class':'numTotalResults'})
            return get_number(spans[0].getText())
        except:
            return "No matches for %s"%(keyword)
    else:
        url = 'http://www.shopping.com/products~PG-%s?KW=%s'%(pagenumber,keyword)
        html = urllib2.urlopen(url)
        soup = bs4.BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class':'quickLookGridItemFullName hide'})
            items=[]
            for i in spans:
                items.append(i.getText())
            return items
        except:
            return "No matches for %s"%(keyword)
	
			
			
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
       name , keyword = argv
       print crawler(keyword)
    elif len(argv) == 3:
       name , keyword , pagenumber =argv
       lis = crawler(keyword , pagenumber)
       for i in lis :
            print i	   
    else:
       print "pass keyword or pagenumber as first and second argument"
       
