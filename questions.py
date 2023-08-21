#QUESTION 1

def hello_name(user_name):
    print('hello ' + user_name)
hello_name("Lyla Guthrie")

#QUESTION 2

def first_odds():
    for num in range(1, 100):
        if num % 2 != 0:
            print(num)
first_odds()

#QUESTION 3

def max_num_in_list(a_list):
    print(max(a_list))
a_list = [72, 54, 36, 22, 1, 7]
max_num_in_list(a_list)

# QUESTION 4

def is_leap_year(a_year):
   if a_year % 4 == 0:
       return True
   elif a_year % 100 == 0:
       return True
   else:
       return False
       
print(is_leap_year(2024)) #leap year
print(is_leap_year(2021)) #non-leap year
    
# QUESTION 5

def is_consecutive(n_list):
    for i in range(len(n_list)):
        if i + 1 >= len(n_list):
            return False
        elif n_list[i] + 1 == n_list[i + 1]:
            return True
print(is_consecutive([1,2,3,4,5]))
       
       