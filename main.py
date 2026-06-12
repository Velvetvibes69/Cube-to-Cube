def cube(num):
    return num*num*num

#define a function that will execute the cube function if the user's entered number is divisible by 3
def by_three(num):
    if num %3 ==0:
        return cube(num)
    else:
        return False
#display results
print(by_three(27))
print(by_three(67))