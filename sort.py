def sort_dictionary(dict):
	sort_by_age = sorted(dict.items(), key = lambda x: x[1][1])
	result = [(name, phone_num) for name, (phone_num, age) in sort_by_age]
	return result

