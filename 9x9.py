i = 1
a = 2
while i < 10:
	print('구구단을 하자 '+str(a)+' x '+str(i)+' = '+str(a*i))
	i = i + 1
	if(i == 10):
		print('-------------------------')
		i = 1
		a = a + 1
		if(a == 10):
			print('구구단 9단까지 끝')
			break
