def cacti_number(plot):
	row = len(plot)
	col = len(plot[0])
	
	count = 0
	for i in range(row):
		for j in range(col):
			if plot[i][j] == 0:
				adjacent_empty = True
				if i > 0 and plot[i-1][j] == 1:
					adjacent_empty = False
				if j > 0 and plot[i][j-1] == 1:
					adjacent_empty = False

				if i < row-1 and plot[i+1][j] == 1:
					adjacent_empty = False
				if j < col-1 and plot[i][j+1] == 1:
					adjacent_empty = False

				if i > 0 and j > 0 and plot[i-1][j-1] == 1:
					adjacent_empty = False
				if i > 0 and j < col-1 and plot[i-1][j+1] == 1:
					adjacent_empty = False

				if i < row-1 and j > 0 and plot[i+1][j-1] == 1:
					adjacent_empty = False
				if i < row-1 and j < col-1 and plot[i+1][j+1] == 1:
					adjacent_empty = False

				if adjacent_empty:
					count += 1
	return count
