# write by number int dari 0 - 219
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(219):
	value = randint(0,219)
	print(value)