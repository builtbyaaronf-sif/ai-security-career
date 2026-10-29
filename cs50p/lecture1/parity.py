def main():
    x = int(input("what is the value of x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False    

main()