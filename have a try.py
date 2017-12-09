def judge(L):
	B=[(i,value) for i,value in enumerate(L) if isinstance(value,int)==True]
	L=[x.lower() for x in L if isinstance(x,str)==True]
	i=0
	while i<len(B):
		L.insert(B[i][0],B[i][1])
		i=i+1
	print(L)
L=eval(input())
judge(L)