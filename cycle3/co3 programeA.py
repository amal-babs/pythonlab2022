import random
mylist=['Ann','Ben','Ciril','Deril','Eric','Fugi']
print(random.choice(mylist))
print(random.choices(mylist,k=4))
print(random.sample(mylist,k=1))
random.shuffle