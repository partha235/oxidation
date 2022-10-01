x=int(input("enter number of electron"))
y=1
c=x
k,w=2,1
for i in range(1,c+1):
    f=2*y**2
    d=f
    print(f," electrons")
    print(y,"shell")
    
    if f>=x:
        print(x,"electron present")
        q=["s","p","d","f"]
        
        for e in q:
            if e=="s":
                if x==1:
                    print("s hyb ",1)
                else:
                    print("s hyb ",2)
                x=x-2
            else:
                b=2*(k+w)
                c=x-b
                if x<=b:
                    print(e," hybri ",abs(x))
                    break
                print(e,"hyb ",b)
                k=k+1
                w=w+1
                x=c
               
        break
    y+=1
    x=x-d