# write by number int dari 0 - 508
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(508):
	value = randint(0,508)
	print(value)