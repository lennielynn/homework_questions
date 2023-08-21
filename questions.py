#QUESTION 1 - Write a function to print “hello_USERNAME!” USERNAME is the input of the function. 

def hello_name(user_name):
    print('hello ' + user_name)
hello_name("Lyla Guthrie")

#QUESTION 2 - Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 100):
        if num % 2 != 0:
            print(num)
first_odds()

#QUESTION 3 - Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    print(max(a_list))
a_list = [72, 54, 36, 22, 1, 7]
max_num_in_list(a_list)

# QUESTION 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

def is_leap_year(a_year):
   if a_year % 4 == 0:
       return True
   elif a_year % 100 == 0:
       return True
   else:
       return False
       
print(is_leap_year(2024)) #leap year
print(is_leap_year(2021)) #non-leap year
    
# QUESTION 5 - Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.

def is_consecutive(n_list):
    for i in range(len(n_list)):
        if i + 1 >= len(n_list):
            return False
        elif n_list[i] + 1 == n_list[i + 1]:
            return True
print(is_consecutive([1,2,3,4,5]))
       
       
