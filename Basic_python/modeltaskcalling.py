import moduletask as md

val1=float(input("Enter number 1: "))
val2=float(input("Enter number 2: "))
print("1) sum \n 2) difference \n 3) multiply \n 4) divivion \n 5) Floor Division \n 6) Modolus \n 7) exit")




while(True):
    val=int(input("enter the option"))
    if(val==1):
        print(f"sum:={md.sum(val1,val2)}")

    elif(val==2):
        print(f"difference: {md.sub(val1,val2)}")
    elif(val==3):
        print(f"mulltiply {md.mul(val1,val2)}")
    elif(val==4):
        print(f"floordivision {md.floordiv(val1,val2)}")
    elif(val==5):
        print(f"modolus: {md.mod(val1,val2)}")
    elif(val==7):
        break
