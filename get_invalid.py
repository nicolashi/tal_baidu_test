import json
with open("att_results", "r") as f:
    for line in f:
        if line[0] != ".":
            #print(line)
            data = json.loads(line)
            if data['error_code'] != 0:
                print(curr_file)
        else:
            curr_file = line[34:-1]
