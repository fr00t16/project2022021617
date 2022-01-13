# write by number int dari 0 - 53
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(53):
	value = randint(0,53)
	print(value)