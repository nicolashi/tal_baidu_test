#
# removes the filepaths printed in the oringial output
#

with open("emotion_results", "r")as f:
    for line in f:
        if line[0] != ".":
            print(line)
