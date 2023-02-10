import random,time    
def checkinput(n1,n2):
    chance=3
    ans=0
    while(chance>0):
        start=time.time()
        chance-=1
        try:
            ui=int(input())
        except:
            print("invalid input , enter a number")    
        end=time.time()
        
        if(ui==n1*n2):
            if( abs(end-start)<=10):
                print("correct!")
                ans=1
                break
            else:
                print("sorry timeout,try again ")
                
        else:
            if chance==0:
                print("wrong answer ,you have exceeds the tries you have")
            else:
                print("wrong answer try again")   
    return  ans     

def multquiz():
    grad=0
    for i in range(10):
        n1=random.randint(0,9)
        n2=random.randint(0,9)
        print("%d * %d = "%(n1,n2),end=' ')
        grad+=checkinput(n1,n2)    
    print("you have pass %d of 10 "%grad)

multquiz()    