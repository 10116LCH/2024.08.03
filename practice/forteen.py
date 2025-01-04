for i in (1, 101):
    if i//10 == 3 or i//10 == 6 or i//10 == 9:
        print ("짝")
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print ("짝짝")
        else :
            print("짝")
    else:
        print(i)






