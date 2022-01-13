# write by number int dari 0 - 360
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(360):
	value = randint(0,360)
	print(value)