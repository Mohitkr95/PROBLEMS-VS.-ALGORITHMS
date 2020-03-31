import time

def sqrt(number):
   """
   Calculate the floored square root of a number
   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   if number < 0:
      return None

   current_num = number
   previous_num = None

   while True:
      current_square = current_num ** 2
      next_square = (current_num+1)**2
   
      if current_square == number or (current_square < number and next_square > number):
         break
      elif current_square > number:
         previous_num = current_num
         current_num = current_num//2
      else:
         current_num = (current_num+previous_num)//2
         
   return current_num


#tests
print(sqrt(9))
#expected output: 3
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print('--------------------------------------')

print(sqrt(-9))
#expected output: None
print ("Pass" if  (None == sqrt(-9)) else "Fail")
print('--------------------------------------')

print(sqrt(0))
#expected output: 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print('--------------------------------------')

print(sqrt(4))
#expected output: 4
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print('--------------------------------------')

print(sqrt(1))
#expected output: 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print('--------------------------------------')

print(sqrt(27))
#expected output: 5
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print('--------------------------------------')

print(sqrt(107))
#expected output: 10
print ("Pass" if  (10 == sqrt(107)) else "Fail")
print('--------------------------------------')

print(sqrt(1247))
#expected output: 35
print ("Pass" if  (35 == sqrt(1247)) else "Fail")