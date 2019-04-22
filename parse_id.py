from __future__ import print_function
from re import search
import json

def main():
    successes = 0
    fails = 0
    total_files = 0
    faces_found = 0

    curr_file = ""

    with open("id_results", "r") as f:
        for line in f:
            if line[0] != ".":
                total_files += 1
                try:
                    if line.find("user_id") != -1:
                        faces_found += 1
                        if check_correct(line, curr_file) == True:
                            #print("success")
                            successes += 1
                        else:
                            fails += 1
                except:
                    pass
            else:
                curr_file = line[63:-1]
 
    print("successes: ", end="")
    print(successes)
    print("fails: ", end="")
    print(fails)

    print("precision(%): ", end="")
    precision = float(successes) / faces_found * 100
    print(precision)

    print("recall(%): ", end="")
    recall = float(successes) / total_files * 100
    print(recall)
    



def check_correct(obtained, filepath):
    expected = filepath.split("\\", 2)[0]
    start_idx = obtained.find("user_id")
    if expected in obtained[start_idx:-1]:
        return True
    return False



if __name__ == "__main__":
    main()
