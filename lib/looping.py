#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    i = 10
    while i >= 1:
        print (i)
        i -= 1
    print ("Happy New Year!")
happy_new_year()




def square_integers(int_list):
    # code goes here!
    for i in int_list:
        int_list = i ** 2
        print (int_list)
    pass
print(square_integers([1, 2, 3, 4, 5]))




def fizzbuzz():
#     # code goes here!
    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print ("Fizz")
        else:
            print (number)
fizzbuzz()
