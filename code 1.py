import pickle
import sys
import os

os.system("cls")
books={}
users={}
ibooks={}
books=pickle.load(open("booksdata" , "rb"))
users=pickle.load(open("users","rb"))
ibooks=pickle.load(open("issuedbooksdata","rb"))
def add():
    name=input("Enter the the name of Book : ").upper()
    author=input("Enter the name of Author : ").upper()
    edition=input("Enter edition : ")
    books[name]=[author , edition]

def search():
    name=input("Enter the name of book : ").upper()
    if name in books:
        print("Book Name : " , name)
        print("Author :" , books[name][0])
        print("Edition :" , books[name][1])
        print("STATUS : Available")
    else:
        print("No book found")

def delete():
    name=input("Enter the name of book : ").upper()
    books.pop(name)
    print("DELETED")

def help():
    print("To search a book type : search")
    print("To add a book type : Add")
    print("To delete a book type : Delete book")
    print("To issue a book type : issue book")
    print("To return a book type : return book")
    print("To delete account type : delete account")
    print("To recover password type : recover password")
    print("For help type : Help")

def issue():
    if username in ibooks:
        print("To issue a new book you have to return previously issued book")
    else:
        name = input("Enter the name of book : ")
        ibooks[username]=name
        print(name," is issued to ",username)

def return_book():
    if username in ibooks:
        ibooks.pop(username)
        print("Book is returned")
    else:
        print("You don't have any book previously issued")
def delete_account():
    users.pop(username)
    print("Your account is deleted")

def take_query():
    while True:
        query=input("Enter your query : ").upper()
        if query=="ADD":
            add()
            continue
        elif query=="SEARCH":
            search()
            continue
        elif query=="DELETE Book":
            delete()
            continue
        elif query=="HELP":
            help()
            continue
        elif query=="ISSUE BOOK":
            issue()
            continue
        elif query=="RETURN BOOK":
            return_book()
            continue
        elif query=="DELETE ACCOUNT":
            delete_account()
            break
        elif query=="BYE":
            print("Hope to see you again. HAVE A NICE DAY")
            break
        elif query=="CHANGE PASSWORD":
            password=input("Enter your new password : ")
            users[username][0]=password
            print("Your password is changed successfully")
            continue
        else:
            print("Wrong Query")
            continue

if __name__== "__main__":

    print("To search a book type : search")
    print("To add a book type : Add")
    print("To delete a book type : Delete book")
    print("To issue a book type : issue book")
    print("To return a book type : return book")
    print("To delete account type : delete account")
    print("To change password type : change password")
    print("For help type : Help")

    while True :
        fquery = input("Want to login/signup/recover password/exit : ")
        if fquery=="login":
            username=input("Enter your username : ")
            if username in users:
                password=input("Enter your Password : ")
                if password==users[username][0]:
                    print("Welcome {}".format(username))
                    break
            else:
                print("No account with this username exist")


        elif fquery=="signup":
            while True:
                username = input("Create a username : ")
                if username in users:
                    print("This username already exist. Try a different username")
                else:
                    users[username]=[]
                    password=input("Create a Password : ")
                    users[username].append(password)
                    food=input("Whats your favourite Food ? (this question will be used to recover your password) : ")
                    users[username].append(food)
                    break
            print("Welcome {}".format(username))
            break

        elif fquery=="recover password":
            username = input("Enter your registered username : ")
            if username in users:
                food=input("Enter your favourite food : ")
                if food==users[username][1]:
                    print("Your Password is : ", users[username][0])
                else:
                    print("Wrong answer.Try Again")
        elif fquery=="exit":
            sys.exit("Hope to see you again. HAVE A NICE DAY")
        else:
            print("Wrong keyword entered")

    take_query()
    pickle.dump(books, open("booksdata", "wb"))
    pickle.dump(ibooks, open("issuedbooksdata", "wb"))
    pickle.dump(users, open("users", "wb"))

