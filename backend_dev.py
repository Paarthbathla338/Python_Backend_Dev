#Backend Dev
#User Registeration
print("Create your Account")
name=input("Enter your UserName:")
passwrd=input("Enter your Password: ")
if len(name)>=1:
    print(f"Username '{name}' created.")
    print("Login Now")
    check1=input("Enter Username: ")
    if check1 != name:
        print("Error:Username Not found")
        exit(1)
    check2=input("Enter Password: ")
    if check2 == passwrd:
        print("Login Succesful")
        
