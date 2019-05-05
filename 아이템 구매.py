P,Q,W=map(int,input().split())

for i in range(W//P+1):
	newW=W-P*i
	# print("체력 물약 개수:",i)
	# print("체력 물약 빼고 남은 돈:",newW)
	# print("남은 돈//Q:",newW//Q)
	if newW%Q==0:
		print(i,newW//Q)
		exit()
