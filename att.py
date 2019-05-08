import os
import urllib, urllib2
import base64
import time

def main():

    # filepath to data
    data_dir = "./face_analysis_data/cls_face_att/"

    api_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    # token must be updated every 30 days
    access_token = '24.9e4fc89b43b955ff1d803c189446a47c.2592000.1557630178.282335-15993344'
    request_url = api_url + "?access_token=" + access_token

    # select attribute types
    fields = "gender,glasses,expression"

    for root, dirs, files in os.walk(data_dir, topdown=False):
        for filename in files:
            if filename.endswith(".jpg"):
                filepath = root + "/" + filename
                print(filepath)
                curr_img = extract_img(filepath)  
                params = "{\"image\":\"" + str(curr_img) + "\"," +\
                         "\"image_type\":\"BASE64\"," +\
                         "\"max_face_num\":10 ," +\
                         "\"face_field\":\"" + fields + "\"}"
                
                request = urllib2.Request(url=request_url, data=params)
                request.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(request)
                content = response.read()
                if content:
                    print(content)

            # stay within qps limit
            time.sleep(0.4)



#
# extract_img
# purpose: convert image file data into base64
#
def extract_img(filepath):
    with open(filepath, "rb") as infile:
        return base64.b64encode(infile.read())

if __name__ == "__main__":
   main()

