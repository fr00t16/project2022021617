# write by number int dari 0 - 369
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(369):
	value = randint(0,369)
	print(value)