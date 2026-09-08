import mysql.connector
from datetime import date
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="db_password",
    database="library_db"
)
cursor=con.cursor()
def add_book():
    book_id=int(input("Enter book id:"))
    book_name=input("Enter book name:")
    author=input("Enter author name:")
    quantity=int(input("Enter quantity:"))
    sql="INSERT INTO books(book_id,book_name,author,quantity) values(%s,%s,%s,%s)"
    values=(book_id,book_name,author,quantity)
    cursor.execute(sql,values)
    con.commit()
    con.close()
    cursor.close()
    print("Book add successfully✅")
def view_book():
    cursor.execute("select * from books")
    book_data=cursor.fetchall()
    for row in book_data:
        print(row)
    con.close  
def issue_book():
    book_id=int(input("Enter book id:"))  
    student_name=input("Enter student name:")  
    cursor.execute("select quantity from books where book_id=%s",(book_id,))
    result=cursor.fetchone()
    if result and result[0]>0:
        sql="INSERT INTO issue_books(book_id,student_name,issue_date) values(%s,%s,%s)"
        values=(book_id,student_name,date.today())
        cursor.execute(sql,values)
        cursor.execute("UPDATE books SET quantity=quantity-1 where book_id=%s",(book_id,))
        con.commit()
        print("Book issued✅")
    else:
        print("Book not available😑")   
    con.close() 
def return_book():
    book_id=int(input("Enter book id:"))
    cursor.execute("select issue_id from issue_books where book_id=%s AND return_date IS NULL",(book_id,)) 
    result=cursor.fetchone()
    if result:
        cursor.execute(
            "UPDATE issue_books SET return_date=%s WHERE issue_id=%s",(date.today(),result[0])
        )       
        cursor.execute(
            "UPDATE books SET quantity=quantity +1 where book_id=%s ",(book_id,)
        )
        con.commit()
        print("Book Returned Successfully")
    else:
        print("No issue record found")
    con.close()
          
