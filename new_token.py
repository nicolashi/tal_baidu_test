#
# generating token for the first time
#

import urllib, urllib2, sys
try: 
    import urllib.request as urllib2
except ImportError:
    import urllib2
import ssl

# api key
client_id = "6vaK4m5bSG695W5bDXMFhQox"
# secret key
client_secret = "HHUxam5V7j1ymGCGiolElHLvaTL5ane8"

host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + client_id + \
	   "&client_secret=" + client_secret
request = urllib2.Request(host)
request.add_header('Content-Type','application/json;charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print(content)
