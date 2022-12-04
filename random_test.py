import random

random.seed(1)
rand_list = [random.randint(1,2) for i in range(1000)]
print(rand_list[:10])