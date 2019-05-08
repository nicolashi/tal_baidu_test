#
# generate new token using refresh token
#

import urllib, urllib2, sys
try: 
    import urllib.request as urllib2
except ImportError:
    import urllib2
import ssl

# api key
client_id = "xDI1sdxGBAqDXmP1SN854oXx"
# secret key
client_secret = "j051S00hqjGdm8CEXDm4ZaYsAqQ2Ddmv"
refresh_token = "25.8e3be89217c9495725e8a5b7529b7226.315360000.1870331211.282335-15993344"

host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&refresh_token=" + refresh_token + \
	   "&client_credentials&client_id=" + client_id + "&client_secret=" + client_secret
request = urllib2.Request(host)
request.add_header('Content-Type','application/json;charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print(content)
