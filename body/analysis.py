#
# Date Created: 2019.04.0d4
# Modified By: Shi Yi Wei
# Purpose: connect to Baidu API and run test image set to collect data 
# on the accuracy of Baidu's body scanning technology
#

import os
import json
import urllib, urllib2
import base64
import time

def main():

    directory = "./data/analysis" # TODO: Add dir name for data

    api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    access_token = '24.3ba60e2073f090a0a614373a0d5a80c6.2592000.1558582725.282335-16088071'
    request_url = api_url + "?access_token=" + access_token

    # set detection options (gender, glasses, etc.)
    fields = "gender,glasses"

    # traverse all test image files and output results for each image
    for root, dirs, files in os.walk(directory, topdown=False):
    	for filename in files:
    	    if filename.endswith(".jpg"):
                filepath = root + "/" + filename
                print(filepath)
                curr_img = extract_img(filepath)  
            
                params = {"image": curr_img}
                params = urllib.urlencode(params)
                
                request = urllib2.Request(url=request_url, data=params)
                request.add_header('Content-Type', 'application/x-www-form-urlencoded')
                response = urllib2.urlopen(request)
                content = response.read()
                if content:
                    print(content)
    		time.sleep(0.3)


#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

