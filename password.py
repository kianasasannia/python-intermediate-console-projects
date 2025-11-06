pas= input("enter your pass : ")
pas2=input("enter your pass again : ")
if(pas==pas2):
    print("your password saved")
    inpu=input("do you want to countinue? Enter 1 for login Enter 2 for exit :")                                           
    if inpu=="1":
        a=input("please enter your pass : ")
        if a==pas2:
            f=open("demofile3.txt","r")
            print(f.read())
        else:
            print("the password is wrong")
    elif inpu=="2":
        print("exited")
        exit(0)   
    else:
        print("1 or 2 ?")    
        inpu=input("do you want to countinue? Enter 1 for login Enter 2 for exit : ")
else:
    print("the passwords that you enterd isn't match together !")
   

