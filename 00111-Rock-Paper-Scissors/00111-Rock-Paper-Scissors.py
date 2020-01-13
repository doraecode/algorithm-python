A,B,C = [int(x) for x in input("enter value ").split()]
if A+B+C<=100 :
    if(A>B and A>C):
        print("PAPER")
    elif B>A and B>C :
        print("SCISSORS")
    elif C>A and C>B :
        print("ROCK")
    else:
        print("I DON'T KNOW")
else:
    print("BUG")
