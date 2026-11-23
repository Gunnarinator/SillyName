from login_utils import verify_un, verify_pw

def loadDB():
    retval = {}
    with open("db.txt","r") as f:
        for line in f.readlines():
            un,pw = line.split(",")
            retval[un.strip()] = pw.strip()

    return retval


def login(db):
    print("Hello what is your username?")
    un = input(">>")
    
    if(verify_un(db, un)):
        print("What is ur password")
        pw = input(">>")
    
        if(verify_pw(db,un,pw)):
            print("Hello!")
            return True
        else:
            print("oops that's not the password")
            return False 
    print("oops we don't have that username")
    return False
                


if __name__ == "__main__":
    db = loadDB()
    login_success = False

    while(not login_success):
        login_success = login(db)
    