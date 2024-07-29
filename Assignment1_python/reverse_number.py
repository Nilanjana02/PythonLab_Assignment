def reverse_number(num):
    rel = num
    rev = 0
    while num != 0:
        r = num % 10
        rev = rev*10+r
        num = num // 10
    print(rev)    

num = int(input("Enter a number: "))
reverse_number(num) 

