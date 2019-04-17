with open("att_results", "r")as f:
    for line in f:
        if line[0] != ".":
            print(line)
