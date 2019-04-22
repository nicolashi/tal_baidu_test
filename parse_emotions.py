from __future__ import print_function
from re import search
import json

def main():
	# expected: 0 -> no smile, 1 -> smile
    expected = 0

    successes = 0
    fails = 0
    
    curr_file = ""

    expected_data = create_database()
    #print(expected_data)   

    with open("emotion_results", "r") as f:
        for line in f:
            if line[0] != ".":
                try:
                    if line.find("expression") != -1:
                        if check_correct(line, curr_file, expected_data) == True:
                            #print("success")
                            successes += 1
                        else:
                            #print("fail", end=" ")
                            #print(line, end=" ")
                            #print("EXPECTED: ", end=" ")
                            #print(expected)
                            fails += 1
                except:
                    pass
            else:
                curr_file = line[63:-1]
 
    print("successes: ", end="")
    print(successes)
    print("fails: ", end="")
    print(fails)
    print("accuracy(%): ", end="")
    total = successes + fails
    accuracy = float(successes) / total * 100
    print(accuracy)
    

def create_database():
    database = {}
    with open("list.txt", "r") as f:
        for line in f:
            curr = line.split()
            if curr[1] == "1":
                database[curr[0]] = 1
            else:
                database[curr[0]] = 0
#   print(database) 
    return database


def check_correct(obtained, filename, database):
    smile = 1
    expected = 0
    if "none" in obtained:
        smile = 0
    for key in database:
        if key == filename:
            expected = database[key]
            print(expected, end=" ")
            print(smile, end=" ")
            print(filename)
    if expected == smile:
        return True
    return False
    

    


if __name__ == "__main__":
    main()
