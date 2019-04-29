import os
import json
import urllib, urllib2
import base64
import time

def main():

    directory = "./new_test_398/test_gallery"

    api_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    access_token = '24.9e4fc89b43b955ff1d803c189446a47c.2592000.1557630178.282335-15993344'
    request_url = api_url + "?access_token=" + access_token

    # traverse all test image files and output results for each image
    for root, dirs, files in os.walk(directory, topdown=False):
        for filename in files:
            if filename.endswith(".jpg"):
                filepath = root + "/" + filename
                print(filepath)
                curr_img = extract_img(filepath)

                # params = "{\"image\":\"" + str(curr_img) + "\"," +\
                #          "\"image_type\":\"BASE64\"," +\
                #          "\"group_id\": \"test_gallery\" ," +\
                #          "\"user_id\":\"" + filename + "\"}"

                params = {}
                params["image"] = str(curr_img)
                params["image_type"] = "BASE64"
                params["group_id"] = "new_test_398"
                params["user_id"] = filename[:-4]
                jsonparams = json.dumps(params)

                request = urllib2.Request(url=request_url, data=jsonparams)

                request.add_header('Content-Type', 'application/json; charset=UTF-8')
                response = urllib2.urlopen(request)
                content = response.read()
                if content:
                    print(content)
            time.sleep(0.5)


#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

