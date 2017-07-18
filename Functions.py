#Calculate fibonacci

def fibonacci(n):
    a=0
    b=1
    for num in range(n):
        a=b
        b=a+num
        print(a,'\n')
    return b

numb = int(input("Enter n"))
print(fibonacci(numb))
