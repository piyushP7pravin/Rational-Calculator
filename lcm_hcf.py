def lcm(x,y):
	if x>y:
		greater=x
	else:
		greater=y
	while True:
		if ((greater%x)==0)and((greater%y)==0):
			lcm=greater
			break
		greater+=1
	return lcm

def hcf(x,y):
	if x<y:
		smaller=x
	else:
		smaller=y
	while True:
		if ((x%smaller)==0)and((y%smaller))==0:
			hcf=smaller
			break
		smaller-=1
	return hcf