#
# Date Created: 2019.04.09
# Modified By: Shi Yi Wei
# Purpose: run test image set to collect data on the acccuracy of Baidu's 
#          facial recognition API
#

import os
import json
import urllib, urllib2
import base64
import time

def main():

    directory = "./det_face_id_tf_v1.0.2/images/test/"

    api_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    access_token = '24.9e4fc89b43b955ff1d803c189446a47c.2592000.1557630178.282335-15993344'
    request_url = api_url + "?access_token=" + access_token

    # traverse all test image files and output results for each image
    for root, dirs, files in os.walk(directory, topdown=False):
        for filename in files:
            if filename.endswith(".jpg"):
                filepath = root + "/" + filename
                print(filepath)
                curr_img = extract_img(filepath)

                params = {}
                params["image"] = str(curr_img)
                params["image_type"] = "BASE64"
                params["group_id_list"] = "comparison_test"
                params = json.dumps(params)

                request = urllib2.Request(url=request_url, data=params)

                request.add_header('Content-Type', 'application/json; charset=UTF-8')
                response = urllib2.urlopen(request)
                content = response.read()
                if content:
                    print(content)

            time.sleep(0.05)


#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

