print("=" * 56)
print("                 LIBRARY MANAGEMENT SYSTEM")
print("=" * 56)

import pymysql
import matplotlib.pyplot as plt

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="library_management"
    )

while(True):
 print('1.Add new Books')
 print('2.Issue Of a Book')
 print('3.Display Books')
 print('4.Submission of a Book')
 print('5.Update Books')
 print('6.Delete Books')
 print('7.Graph')
 print('8.Logout')
 ch=int(input('Enter your choice from the given list:'))


 # Add a new book
 if(ch==1):
    con = get_connection()
    c=con.cursor()
    p=input("Enter Book Name: ")
    i=input("Enter Author's Name: ")
    f=int(input("Enter Book Code: "))
    t=int(input("Total no.of Books: "))
    s = "INSERT INTO books (bname, bcode, total, author) VALUES (%s, %s, %s, %s)"
    c.execute(s, (p, f, t, i))
    con.commit()
    con.close()
    print("\nBook Added Successfully\n")

 # Issue a book    
 elif(ch==2):
    con = get_connection()
    c=con.cursor()
    n=input("Enter Name:")
    r=input("Enter Reg no:")
    bc=input("Enter Book Code:")
    d=input("Enter Date:")
    q = "INSERT INTO issuedbooks (name, regno, bcode, issued) VALUES (%s, %s, %s, %s)"
    c.execute(q, (n, r, bc, d))
    con.commit()
    con.close()
    print("\nData entered Successfully\n")

 # Display all books
 elif(ch==3):
    con = get_connection()
    c=con.cursor()
    x="select * from books;"
    c=con.cursor()
    c.execute(x)
    m=c.fetchall()
    for i in m:
        print("Book name: ", i[0])
        print("Book code: ", i[1])
        print("Total: ", i[2])
        print("Author: ", i[3])
        print("\n")
    print("Data Displayed Successfully\n")
    con.close()

 # Submit a returned book      
 elif(ch==4):
    con = get_connection()
    c=con.cursor()
    n=input("Enter Name: ")
    r=input("Enter Reg No: ")
    bc=int(input("Enter Book Code: "))
    e=input("Enter Date: ")
    k = "INSERT INTO submission (name, regno, bcode, submission) VALUES (%s, %s, %s, %s)"
    c.execute(k, (n, r, bc, e))
    con.commit()
    con.close()
    print("\nData entered successfully\n")

 # Update book details
 elif(ch==5): 
    con = get_connection()
    c=con.cursor()
    bc=int(input("Enter Book Code:"))
    a='select * from books where bcode='+str(bc)
    data=c.execute(a)
    if(data!=0):
        b=c.fetchall()
        print('Book Name =', b[0][0])
        print('Book Code =', b[0][1])
        print('Total =', b[0][2])
        print('Author =', b[0][3])
        nn=input('Enter new book name::')
        nm=int(input('Enter new total::'))
        nr=int(input('Enter new book code::'))
        y = "UPDATE books SET bname=%s, bcode=%s, total=%s WHERE bcode=%s"
        c.execute(y, (nn, nr, nm, bc))
        con.commit()
        con.close()
        print("\nUpdated Successfully\n")
    else:
        print("\nBook code does not exist\n")
 
 # Delete a book
 elif(ch==6):    
    con = get_connection()
    c=con.cursor()
    ac=int(input("Enter Book Code: "))
    w = "DELETE FROM books WHERE bcode=%s"
    c.execute(w, (ac,))
    con.commit()
    con.close()
    if c.rowcount > 0:
        print("\nBook deleted successfully\n")
    else:
        print("\nBook Code not found\n")

 # Display book statistics
 elif(ch==7):
    con = get_connection()
    c = con.cursor()
    c.execute("SELECT bcode, total FROM books")
    data = c.fetchall()
    book_codes = [row[0] for row in data]
    totals = [row[1] for row in data]
    plt.figure(figsize=(8, 5))
    plt.bar(book_codes, totals, color='royalblue')
    plt.xlabel("Book Code")
    plt.ylabel("Number of Books")
    plt.title("Book Code vs Number of Books")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    con.close()

 # Exit application
 elif(ch==8):
    break

 else:
    print('Your choice is invalid,Please choose from the given list:')
