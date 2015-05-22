import urllib
import urllib2

def data_url():
    url = 'http://127.0.0.1/medAI/ss_type.php'
    values = {'w_txt' : 'art',
              'location' : 'Northampton',
              'language' : 'Python' }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page;

def word_type(word):
    url = 'http://127.0.0.1/medAI/ss_type.php'
    values = {'w_txt' : word}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page.strip().split(',');
