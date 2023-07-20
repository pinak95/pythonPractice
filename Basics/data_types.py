pi = 3.14

# To check the data type of variable you can use the type() function
print('Data type of pi=3.14 is ', type(pi))

num_add = 3 + 2
num_sub = 3 - 2
num_mul = 3 * 2
num_div = 3 / 2
num_floor_div = 3 // 2
num_exp = 3 ** 2
num_mod = 3 % 2

# To add the numbers you can use the + operator
print(f'\nBasic Arithmetic operations: '
      f'\n For Addition(3+2): {num_add}'
      f'\n For Subtraction(3-2): {num_sub}'
      f'\n For Multiplication(3*2): {num_mul}'
      f'\n For Division(3/2): {num_div}'
      f'\n For Floor Division(3//2): {num_floor_div}'
      f'\n For Exponent(3**2): {num_exp}'
      f'\n For Modulus(3%2): {num_mod}')


def i_add(i):
    i += 1
    return i


def i_sub(i):
    i -= 3
    return i


def i_mul(i):
    i *= 10
    return i


def i_div(i):
    i /= 2
    return i


def i_floor_div(i):
    i //= 2
    return i


def i_exp(i):
    i **= 2
    return i


def i_mod(i):
    i %= 2
    return i


# ShortHand operators
print('\nBasic Short Hand operations: For i=10 '
      '\n For Addition(i+=1): ', i_add(10),
      '\n For Subtraction(i-=3): ', i_sub(10),
      '\n For Multiplication(i*=10): ', i_mul(10),
      '\n For Division(i/=2): ', i_div(10),
      '\n For Floor Division(i//=2): ', i_floor_div(10),
      '\n For Exponent(i**=2): ', i_exp(10),
      '\n For Modulus(i%=2): ', i_mod(10))

# To print the absolute value of a number we can use the abs() function
print('\nThe absolute value of -10 is:', abs(i_add(-11)))

""" To print the round value of a number we can use the round() function
    round() function returns the nearest integer value of a number """
print('The round value of 9.24897/2 when we just print the first 2 decimal places: ', round(i_div(9.24897), 2))

# To cast a string to integer we can use int()

num_1 = '10'
num_2 = '20'

# This will print 1020
print(num_1 + num_2)

# This will print 30 as it should
print(int(num_1) + int(num_2))
