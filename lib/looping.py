#!/usr/bin/env python3

def happy_new_year():
    i = 10 
    while i >= 0:
        if i == 0:
         print("Happy New Year!")
        else:
           print(i)
        i -= 1
happy_new_year()


def square_integers(int_list):
    squared_integers = [integer ** 2 for integer in int_list]
    return(squared_integers)
   
    
    

def fizzbuzz():
      num = 1
      while num <= 100:
          if num % 15 == 0:
             print("FizzBuzz")
          elif num % 5 == 0:
               print("Buzz")
          elif num % 3 == 0:
               print ("Fizz")
          else:
              print(num)
          num += 1
          
fizzbuzz()
