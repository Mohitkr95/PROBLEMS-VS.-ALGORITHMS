def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.
   Args:
      ints(list): list of integers containing one or more integers
   """
   min_int = ints[0]
   max_int = ints[0]
   for i in ints:
      if i <min_int:
         min_int = i
      elif i >max_int:
         max_int = i
   return (min_int, max_int)




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max(l))
# expected output:(0, 9)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print('-----------------------------')

print(get_min_max([1]))
# expected output:(1, 1)
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print('-----------------------------')

print(get_min_max([1,1,1,1,5]))
# expected output:(1, 5)
print ("Pass" if ((1, 5) == get_min_max([1,1,1,1,5])) else "Fail")
print('-----------------------------')

print(get_min_max([0, 45, 5, 8, 9, 123, -10]))
# expected output:(-10, 123)
print ("Pass" if ((-10, 123) == get_min_max([0, 45, 5, 8, 9, 123, -10])) else "Fail")