##############################################################
#   Code Created By Ahmet Acarer                             #
##############################################################


def fibonacci(n):
    if n < 0:
      return "Please enter positive numbers"
    if n == 0:
      return n;
    if n == 1:
      return n;
    return fibonacci(n-1) + fibonacci(n - 2)
    



#print the fibonacci to the n-th number
print(fibonacci(-10))
