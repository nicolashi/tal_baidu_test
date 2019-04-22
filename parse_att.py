from __future__ import print_function
from re import search
import json

def main():
	# expected = [glasses, gender]
	# glasses: 0 -> no glasses, 1 -> glasses
	# gender: 0 -> female, 1 -> male
    expected = [0, 0]
    data = {}

    successes = 0
    fails = 0

    file_count = 0
    curr_file = ""
    data_count = 0
    curr_json = ""

    with open("att_results", "r") as f:
        for line in f:
            if line[0] != ".":
                data_count += 1
                curr_json = line
                try:
                    print(curr_file)
                    print(line)
                    if line.find("glasses") != -1:
                        if check_correct(line, expected) == True:
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
                curr_file = line
                file_count += 1
                exp_val = line[72:79]
                expected[0] = exp_val[0]
                expected[1] = exp_val[2]
  
    print("successes: ", end="")
    print(successes)
    print("fails: ", end="")
    print(fails)
    print("accuracy(%): ", end="")
    total = successes + fails
    accuracy = float(successes) / total * 100
    print(accuracy)
    

def check_correct(obtained, expected):
   # print("\n\n")
    #print("checking: ", end="")
    #print(expected)
    #print(obtained)
    #print("\n\n")
    gender = '2'
    glasses = '2'
    if "female" in obtained:
        #print("FEMALE")
        gender = '0'
    else:
        gender = '1'
    #print(obtained)
    #print(gender)
    #print("gender done")
    if gender != expected[1]:
        return False

    # get value of glasses
    #glasses_index = obtained.find("glasses")
    #glasses_sect = obtained[glasses_index:]
   # if "none" in glasses_sect:
          #print("glasses")
     #   glasses = '0'
    #else:
      #  glasses = '1'
 #   #print("glasses done")
    #if glasses != expected[0]:
     #   return False

    return True



if __name__ == "__main__":
    main()
