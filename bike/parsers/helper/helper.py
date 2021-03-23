import urllib

def get_url_content(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib.request.urlopen(req)
    return con.read()

