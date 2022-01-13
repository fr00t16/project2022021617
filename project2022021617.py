# write by number int dari 0 - 998
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(998):
	value = randint(0,998)
	print(value)