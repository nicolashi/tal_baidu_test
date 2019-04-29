from __future__ import print_function
from re import search
import json

def main():
    successes = 0
    fails = 0
    total_files = 0
    detected = 0

    curr_file = ""
   
    with open("results", "r") as f:
        for line in f:
            if line[0] != ".":
                total_files += 1
                try:
                    if line.find("person_info") != -1:
                        detected += 1
                        if check_correct(line, curr_file) == True:
                            #print("success")
                            successes += 1
                        else:
                            fails += 1
                except:
                    pass
            else:
                ref = line.find("test")
                curr_file = line[ref + 5:-1]
                #print(curr_file)
 
    print("successes: ", end="")
    print(successes)
    print("fails: ", end="")
    print(fails)

    print("precision(%): ", end="")
    precision = float(successes) / detected * 100
    print(precision)

    print("recall(%): ", end="")
    recall = float(successes) / total_files * 100
    print(recall)
    



def check_correct(obtained, filepath):
    expected = filepath.split("/", 2)[0]
    start_idx = obtained.find("user_id")
    #print(obtained[start_idx:start_idx+15])
    if expected in obtained[start_idx:start_idx + 15]:
        return True
    return False



if __name__ == "__main__":
    main()
