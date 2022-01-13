# write by number int dari 0 - 402
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(402):
	value = randint(0,402)
	print(value)