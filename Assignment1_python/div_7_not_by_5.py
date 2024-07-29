def DivBy_7_not_5():
    for i in range(1000,2000):
        if i%7 == 0 and i%5 != 0:
            print(i)
            
print("The numbers between 1000 and 2000 which is divisible by 7 but not multiple of 5: ")
DivBy_7_not_5() 

