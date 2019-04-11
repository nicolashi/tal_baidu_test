#
# Date Created: 2019.04.09
# Modified By: Shi Yi Wei
# Purpose: run test image set to collect data on the acccuracy of Baidu's 
#          facial recognition API
#

import os
import urllib, urllib2
import base64

def main():

    directory = "C:/Users/user/Desktop/algo/data/face_recognition/"

    api_url = "https://aip.baidubce.com/rest/2.0/face/v2/identify"
    access_token = '24.f6df1652adfbc27ae00113f16f1e8bc6.2592000.1557303389.282335-15917127'
    request_url = api_url + "?access_token=" + access_token


    # traverse all test image files and output results for each image
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpg"):
                print(filename)
                filepath = root + "/" + filename
                curr_img = extract_img(filepath)
                #print("\n" + filepath + "\n")
           
                #params = "{\"image\":\"" + str(curr_img) + \
                #"027d8308a2ec665acb1bdf63e513bcb9\"," +\
                #"\"image_type\":\"BASE64\"," +\
                #"\"max_face_num\":10 ," +\
                #"\"face_field\":\"" + fields + "\"}"
            
                #request = urllib2.Request(url=request_url, data=params)
                #request.add_header('Content-Type', 'application/json')
                #response = urllib2.urlopen(request)
                #content = response.read()
                #if content:
                    #print(content)


#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

