def NextFit(blockSize, m, processSize, n):
	allocation = [-1] * n
	j = 0
	t = m-1
	
	for i in range(n):
		while j < m:
			if blockSize[j] >= processSize[i]:
				allocation[i] = j
				blockSize[j] -= processSize[i]
				t = (j - 1) % m
				break
				
			if t == j:
				t = (j - 1) % m
				break
				
			j = (j + 1) % m
			
	print("Process No. Process Size Block no.")
	for i in range(n):
		print("\t", i + 1, "\t", processSize[i],end = "\t\t")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

if __name__ == '__main__':
	blockSize = [100,500,200,300,600]
	processSize = [212,417,112,426]
	m = len(blockSize)
	n = len(processSize)
	NextFit(blockSize, m, processSize, n)
