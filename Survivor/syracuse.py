import time
import math
count = 0
max = count
max_num= 0
top = int(input('Enter the max range. '))
run_time = time.time()
for num in range(1,top):
    if count > max:
        max_num = num - 1
        max = count
    count = 0
    while num > 1:
        

        if (num % 2 == 0):    #this means number is even
            num /= 2
            
        else:
            num = num * 3 + 1 
        count = count + 1
print(max_num)
print(f'Finished sequence in {time.time()-run_time} seconds' )
#print(max_num / math.pi / math.e / math.sqrt(2**1000))