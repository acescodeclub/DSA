# Recursion is basically doing something over and over
# With this idea in mind it means we can use recursion in place of a loop
# So I'm going to loop through a list of numbers and print them out
# I am going to use a regular for loop first then use recursion to show that we can achieve the same result
# Read the reference book on recursion for more information

arr = [1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# print elements in a list using a regular for loop
def regularForLoop(arr): 
    for i in range(len(arr)): 
        print(arr[i])
        
# print elements in a list using a recursion
def recursiveLoop(arr, index=0):
    if index == len(arr): # base case
        return 
    print(arr[index])
    recursiveLoop(arr, index + 1)

# NOTE: 
# The base case is your terminating condition otherwise your loop will run forever
# for this example we want to call the function with a different index each time but when we reach the ...
# ... end of the list we need to terminate the loop two first of all prevent an index out of bounds error
# But most importantly an infinite loop because for some problems we won't get any error and the loop will run ... 
# ... forever (Actually until your computer has had enough)

regularForLoop(arr)
recursiveLoop(arr)


# Now I'm going to divide a number by 2 continously until we get a quotient smaller than 2 (that is 1)
# So we want to stop the loop when the remainder is smaller than two

def divideByTwo(n, cache): 
    cache.append(n) # cache is an array that stores all our quotient values
    if n == 1: # we stop the loop when we get 1
        return cache
    n = n // 2 # our quotient which will be passed to the function next
    return divideByTwo(n, cache)
    
print(divideByTwo(67, []))

# So the baseline is that wherever you use a loop you can probably use recursion as well
# It can be a tricky topic to understand so you can read the reference book or watch some videos online ...
# ... on how to read recursive code

