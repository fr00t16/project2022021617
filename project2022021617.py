# write by number int dari 0 - 989
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(989):
	value = randint(0,989)
	print(value)