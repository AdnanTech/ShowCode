import math

def is_fibonacci(input):
  phi = 0.5 + 0.5 * math.sqrt(5.0)
  a = phi * input

  if(input >= 0 and input <= 2147483647 and (input % 1) == 0):  
    return input == 0 or abs(round(a) - a) < 1.0 / input   
  else:
    return False

if __name__=='__main__':
  input = 0
  print("Fib: ", is_fibonacci(input))