iport json

def main():
	# expected = [glasses, gender]
	# glasses: 0 -> no glasses, 1 -> glasses
	# gender: 0 -> female, 1 -> male
	expected = [0, 0]
	data = {}

	successes = 0
	fails = 0

	with open("emotions_results", "r") as f:
		for line in f:
			try:
				data = json.loads(line)
				if check_pass(data, expected) == True:
					successes += 1
				else:
					fails += 1
			except:
				exp_val = search(line, "\d_\d_\d_\d")
				expexted[0] = exp_val.split()[0]
				expected[1] = exp_val.split()[2]


    print("accuracy (%)", end="")
    accuracy = successes / (successes + fails) * 100


def check_pass(obtained, expected):
    if gender in obtained:
        if gender == "female": #TODO: figure out syntax


if __name__ == "__main__":
    main()
