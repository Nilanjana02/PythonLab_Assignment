def prime_series(n):
    if(n>=2):
        print(2)
    for j in range(3,n+1,2):
        flag = 1
        k =int(j/2) 
        for i in range(2,k):
            if j%i == 0:
                flag = 0
                break
        if flag == 1:
            print(j)
            
n = int(input("Enter how many prime number you want to display: "))
prime_series(n) 

