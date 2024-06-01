pswd = input(" enter the password " )

def view():
    a = input( " enter the account name for which you want to view password ")
    with open('file.txt','r') as f:
        for line in f.readlines():
            user,pas = line.split("|")
            if ( user == a):
                print(" Password for",a,"is",pas)
                return
            
    print("Account does not exist ")


def add():
    acc = input("Enter account name : ")
    pasd = input("Enter password : ")

    with open("file.txt","a") as f:
        f.write(acc+" | "+pasd+"\n")



while True:
    mode = input(" Do you want to view password or add a new password (view/add). Press Q to quit ").lower()
    if ( mode == "q"):
        break
    if ( mode == "view"):
        view()
    elif(mode == "add"):
        add()
    else:
        print("Invalid mode. Try again ! ")
        continue