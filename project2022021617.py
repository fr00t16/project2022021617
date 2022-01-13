# write by number int dari 0 - 603
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(603):
	value = randint(0,603)
	print(value)