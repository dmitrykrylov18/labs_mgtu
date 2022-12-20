import random

def gen_random(num_count, begin, end):
      a=[]
      for i in range(num_count): a.append(random.randint(begin,end))
      print(a)

gen_random(5,1,10)

