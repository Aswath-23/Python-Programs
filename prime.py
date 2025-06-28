def prime(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

n=int(input("Enter a number: "))
if prime(n)==1:
    print("Prime")
else:
    print("Not Prime")
