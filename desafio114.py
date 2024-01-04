import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://open.spotify.com/intl-pt')
except urllib.error.URLError:
    print('O Google esta em baixa.')
else:
    print('O site esta no ar.')
    print(site.read().decode('utf-8'))
