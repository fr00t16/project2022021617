# write by number int dari 0 - 863
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(863):
	value = randint(0,863)
	print(value)