import studenindex as si
from studentoperation import Add,remove,search,update,view
import  sys
print("-"*60)
while(True):
    si.menu()
    n=int(input("Enter choice :"))
    if(n==1):
        Add()
    elif(n==2):
        update()
    elif(n==3):
        remove()
    elif(n==4):
        view()
    elif(n==5):
        search()
    elif(n==6):
        sys.exit()
    else:
        print("wrong choice")

