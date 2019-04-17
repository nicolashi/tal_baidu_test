import json
from re import search

def main():
	# expected = [glasses, gender]
	# glasses: 0 -> no glasses, 1 -> glasses
	# gender: 0 -> female, 1 -> male
    expected = [0, 0]
    data = {}

    successes = 0
    fails = 0
    
    with open("att_results", "r") as f:
        for line in f:
    	    try:
                print("FONUD JSON DATA")
                data = json.dumps(line)
                data = json.loads(data)
                #print(data)
#				if check_pass(data, expected) == True:
#                   successes += 1
#				else:
#					fails += 1
            except:
                try:
                    exp_val = line[73:80]
                    print("FOUND FILENAME")
                    print(exp_val)
                    #expexted[0] = exp_val.split()[0]
                    #expected[1] = exp_val.split()[2]
                except:
                    print("E X C E P T I O N")
                    print(line)
                    print("\n")
        

   # print("accuracy (%)", end="")
   # accuracy = successes / (successes + fails) * 100
    

def check_pass(obtained, expected):
    if gender in obtained:
        if gender == "female": #TODO: figure out syntax
            pass

if __name__ == "__main__":
    main()
