import urllib2
def get_url(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html;

    # try -- get_url('http://127.0.0.1/medAI/ss_type.php?w_txt=art')
