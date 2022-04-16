# https://www.spoj.com/problems/AGGRCOW/
def is_possible(st_location, d, c):
	lastplacedcow = st_location[0]
	cows = 1
	for i in range(1,len(st_location)):
		if st_location[i] - lastplacedcow >= d:
			cows += 1
			lastplacedcow = st_location[i]
	return True if cows >= c else False

def maxmindist(st_location, c):
	st_location.sort()
	l = 1
	h = st_location[-1]-st_location[0]
	
	while l <= h:
		mid = l+(h-l)//2
		if is_possible(st_location, mid, c):
			l = mid+1
		else:
			h = mid-1
	return h

t = int(input())

while t:
	t -= 1
	n, c = input().split()
	n = int(n)
	c = int(c)
	st_location = []
	for i in range(n):
		s = input()
		st_location.append(int(s))
	print(maxmindist(st_location, c))