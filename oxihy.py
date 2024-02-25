na=input("enter positive atom name")
x=int(input("enter number of electron"))
y=1
c=x
k,w=2,1
for i in range(1,c+1):
    f=2*y**2
    d1=f
    print(f," electrons")
    print(y,"shell")
    
    if f>=x:
        print(x,"electron present")
        q=["s","p","d","f"]
        
        for e1 in q:
            if e1=="s":
                if x==1:
                    print("s hyb ",1)
                else:
                    print("s hyb ",2)
                x=x-2
            else:
                b=2*(k+w)
                c=x-b
                if x<=b:
                    print(e1," hybri ",abs(x))
                    print(na,"atom has free space for bonding in  ",e1," sub-orbital.",d1-x)
                    break
                print(e1,"hyb ",b)
                k=k+1
                w=w+1
                x=c
               
        break
    y+=1
    x=x-d1

na=input("enter negative atom name")
x=int(input("enter number of electron"))
y=1
c=x
k,w=2,1
for i in range(1,c+1):
    f=2*y**2
    d2=f
    print(f," electrons")
    print(y,"shell")
    
    if f>=x:
        print(x,"electron present")
        q=["s","p","d","f"]
        
        for e2 in q:
            if e2=="s":
                if x==1:
                    print("s hyb ",1)
                else:
                    print("s hyb ",2)
                x=x-2
            else:
                b=2*(k+w)
                c=x-b
                if x<=b:
                    print(e2," hybri ",abs(x))
                    print(na,"atom has free space for bonding in  ",e2," sub-orbital.",d2-x)
                    break
                print(e2,"hyb ",b)
                k=k+1
                w=w+1
                x=c
               
        break
    y+=1
    x=x-d2

if e1>=e2:
    print("good bond")

elif e1<=e2:
    print("poor bond")
else:
    print("try another")
