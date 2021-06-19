def maximum_product(input):
 
  # edge case 
  if (input == 1):
     return 0

   # n equals to 2 or 3 must be handled explicitly
  if (input == 2 or input == 3):
     return (input - 1)
   
  # keep removing parts of size 3 while n is greater than 4
  temp = 1
  while (input > 4):
    input -= 3
    temp *= 3 # Keep multiplying 3 to temp
    
  return (input * temp) # The last part multiplied by previous parts
 

if __name__=='__main__':
  input = 8
  print("Maximum Product is", maximum_product(input))