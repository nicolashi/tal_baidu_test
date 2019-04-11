#
# Date Created: 2019.04.04
# Modified By: Shi Yi Wei
# Purpose: connect to Baidu API and run test image set to collect data 
# on the accuracy of Baidu's facial scanning technology 
# (Features tested include: gender, expression (smile or not), glasses)
#

import os
import urllib, urllib2
import base64

def main():

    directory = "C:/Users/user/Desktop/algo/data/face_analysis/"

    api_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    access_token = '25.09f3d361d83fe0f82b3e827d493d2702.315360000.1870328063.282335-15993344'
    request_url = api_url + "?access_token=" + access_token

    # set detection options (gender, expression(smile), glasses)
    fields = "gender,gender_probability,expression,expression_probability,glasses,glasses_probability"

    # traverse all test image files and output results for each image
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            filepath = directory + filename
            curr_img = extract_img(filepath)
            #print("\n" + filepath + "\n")
            
            params = "{\"image\":\"" + str(curr_img) + "\"" +\
            "\"image_type\":\"BASE64\"," +\
            "\"max_face_num\":10 ," +\
            "\"face_field\":\"" + fields + "\"}"
            
            request = urllib2.Request(url=request_url, data=params)
            request.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(request)
            content = response.read()
            if content:
                print(content)


#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

