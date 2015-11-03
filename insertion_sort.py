import random
import datetime

x=[]
def create_list():
	for i in range(0,100):
		random_num = random.randint(0,10000)
		x.append(random_num)

def print_pretty():
	for i in range(0,10):
		for j in range(0,10):
			print '{0:5d}'.format(x[j+i*10]),
		print

def switch(last_index, first_index, target_value):
	
	
	for k in range(last_index, first_index, -1):
		x[k] = x[k-1]
	x[first_index] = target_value


def insertion_sort():
	for i in range(1, len(x)):
		target = x[i]
		for j in range(0, i):
			if(target < x[j]):
				switch(i,j,target)
				break

create_list()
print 'Unsorted x'
print_pretty()
insertion_sort()
print 'Sorted x'
print_pretty()


