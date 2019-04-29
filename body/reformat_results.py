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
                detected += 1
                try:
                    # TODO: split results for each person
                    data = json.loads(line)
                    split_data(data["person_info"])
                except:
                    pass
            else:
                total_files += 1
                curr_file = line[30:-1]
                print(curr_file, end=" ")

#    print("Total Files: ", end="")
#    print(total_files)
#    print("Usable Files: ", end="")
#    print(detected)


def split_data(all_data):
    for person in all_data:
        location = person["location"]
        xmin = location["left"]
        ymax = int(location["top"]) + int(location["height"])
        xmax = int(location["left"]) + int(location["width"])
        ymin = location["top"]
        score = round(location["score"], 6)
        print(xmin, ymin, xmax, ymax, score, end=" ")
    print("\n", end="")


if __name__ == "__main__":
    main()
