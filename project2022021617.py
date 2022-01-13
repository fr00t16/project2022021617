# write by number int dari 0 - 60
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(60):
	value = randint(0,60)
	print(value)