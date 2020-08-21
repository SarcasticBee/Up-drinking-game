import sys
sys.path.append('Users/paulk/Documents/pol/programming/factor.py')
sys.path.append('Users/paulk/Documents/pol/programming/check.py')

import factor
import check

# not best approach
# see from minute 9:30
# Corey Schafer. (2017). Python Tutorial for Beginners 9. Found at:
# https://www.youtube.com/watch?v=CqvZ3vGoGs0


up = 17
print('Up is', up)

for i in range(1,200):
    if i == up:
        print('Up!!!!')
    elif factor.multiple(i, up):
        print('Up!!!!')
    elif check.contains(i, up):
    #elif str(up) in str(i):
        print('Up!!!!')
    else:
        print(i)

        
