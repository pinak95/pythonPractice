# import sys


# Function to read integers from input
def read_int():
    return int(input().strip())


# Function to read a list of integers from input
def read_list():
    return list(map(int, input().split()))
    # return [int(x) for x in input().split()] Alternative solution using list comprehension


# Function to read a string from input
def read_string():
    return input().strip()


# Function to solve the problem for each test case
def solve():
    # Modify this section based on the specific problem requirements
    result = 0
    # Print the result for each test case
    print(result)


# Main function to run the program
if __name__ == "__main__":
    # Read the number of test cases
    t = read_int()

    # Loop through each test case and call the solve function
    for _ in range(t):
        solve()
