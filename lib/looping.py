#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter=10
    while counter>0:
       print(counter)
       counter -= 1
    print("Happy New Year!")
    pass
happy_new_year()

def square_integers(int_list):
    height_incrime=[int*int for int in int_list]
    return height_incrime
    # code goes here!
    pass

def fizzbuzz():
    for num in range(1, 101):  # Range from 1 to 100 inclusive
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to print FizzBuzz
fizzbuzz()



    

