n=input("enter the name:")
a=int(input("enter the age :"))
g=input("enter sex : ' M or F ':")
d=int(input("enter the number of days:"))
if(a>18 and a<=30 and g=="m"):
    print ("your wage is :" ,700*d)
elif(a>30 and a<=40 and g=="f"):
    print("your wage is :" ,750*d)
elif(a>30 and a <=40 and g=="m"):
    print("your wage is :" ,800*d)
elif(a>30 and a <=40 and g=="f"):
    print("your wage is :" ,800*d)
else:
    print("invalid entry")            