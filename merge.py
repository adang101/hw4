def merge(mList1, mList2):
	# 2 pre-sorted integer lists
	i = j = 0
	mergedList = []
	while i < len(mList1) and j < len(mList2):
		if mList1[i] <= mList2[j]:
			mergedList.append(mList1[i])
			i += 1
		else:
			mergedList.append(mList2[j])
			j += 1
	
	mergedList.extend(mList1[i:])
	mergedList.extend(mList2[j:])
	return mergedList
