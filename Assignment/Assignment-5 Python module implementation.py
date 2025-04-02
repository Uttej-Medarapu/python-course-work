def primenumber(num):
        for i in range(2,(num//2)+1):
            if num%i==0:
                print(f"{num}is not a prime number")
                break
        else:
            print(f"{num}is prime number")
        


def fac(m):
    if m==0:
        return 1
    return m * fac(m- 1)
m=int(input("enter a number for factorial:"))
print(f"factorial of {m} is {fac(m)}")
 

def fibonacci(n):
    a,b=0,1
    for j in range(n):
        print(a,end=" ")
        a,b=b,a+b



def gcd(k,l):
    while l!=0:
        k,l=l,k%l
    return k


def lcm(m,n):
    return print(f"LCM of two numbers is{(m*n) // gcd(m,n)}")



def reverse_number(rev):
    k = list(str(rev)[::-1]) 
    print("".join(k))  



def palindrome(palin):
    if palin == palin[::-1]:
       return print(f"given {palin} is polindrome")
    else:
        return print(f"given {palin} is not polindrome")


def sum_of_digits(n):
    tot= 0
    for l in str(n):
        tot += int(l)
    return print("sum of digits",tot)

# The sum of each digit, 
# where each digit is raised to the power of the total number of digits,
#  is equal to the given number."
#153 is armstrong number
def armstrong(n):
    num_str = str(n)
    power = len(num_str)
    armstrong_sum=0
    for digit in num_str:
        digit_int = int(digit) 
        powered_value = digit_int ** power   #imp line
        armstrong_sum += powered_value 
    if (armstrong_sum == n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is NOT an Armstrong number.")


# sum of its divisors = given number called as perfect number
def perfect_num(n):
    perfect = 0  
    for i in range(1, n):  
        if n % i == 0:  
            perfect += i  
    if (perfect == n):
        return print(f"{n} is perfect number" ) 
    else:
        return print(f"{n} is not perfect number") 








# def evenorodd():
#     a=int(input("\n enter a number to know even or odd:"))
#     if a%2==0:
#         print("Given number is even")
#     else:
#         print("Given number is odd")
#     print("*"*10)