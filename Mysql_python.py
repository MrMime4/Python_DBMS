import mysql.connector
import mysqlDB

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="study"
)

Query = mydb.cursor()

Insert_Query = "INSERT INTO study.first (name, age) VALUES(%s,%s)"
Display_Query = "SELECT * FROM study.first"
No_of_rows = "SELECT COUNT(*) FROM study.first"
Delete_Query = "DELETE FROM study.first WHERE id = %s"
Search_Query = "SELECT * FROM study.first WHERE id = %s"

class Node:
    
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def Display(self):

        Query.execute(No_of_rows)
        count = Query.fetchone()[0]
        if(count == 0):
            print("No Data To Show..!\n")

        Query.execute(Display_Query)
        myresult = Query.fetchall()
        for i in myresult:
            print(i)
        print("\n")    

            
    def Insert(self,name,age):

        val = (name,age)
        Query.execute(Insert_Query,val)
        mydb.commit()
        print(Query.rowcount,"Record Inserted.\n")


        NewNode = Node(name,age)
        NewNode.next = self.head
        self.head = NewNode
        
    def Delete(self,key):

        Query.execute(No_of_rows)
        count = Query.fetchone()[0]
        if(count == 0):
            print("No Record To Delete..!\n")

        Query.execute(Delete_Query,(key,))
        mydb.commit()
        print(Query.rowcount, "Record Deleted.\n")

        
    def Search(self,key):

        Query.execute(No_of_rows)
        count = Query.fetchone()[0]
        if(count == 0):
            print("No Record To Search..!\n")

        Query.execute(Search_Query,(key,))
        record = Query.fetchone()
        print(record)
        print(Query.rowcount, "Record Found.\n")
            
        
    
if __name__ == '__main__':
    
    llist = LinkedList()
    while(True):
        ch = input("Enter \n1.INSERT A RECORD/\n2.DELETE A RECORD/\n3.DISPLAY ALL RECORDS/\n4.SEARCH A RECORD/ \n0.EXIT :=> ")
        print()
        if (ch == '1'):
            name = input("Enter New Name:")
            age = int(input("Enter New Age:"))
            llist.Insert(name,age)
        elif (ch == '2'):
            key = int(input("Enter ID Of The Record:"))
            llist.Delete(key)  
        elif (ch == '3'):
            llist.Display()  
        elif (ch == '4'):
            key = int(input("Enter ID Of The Record:"))
            llist.Search(key)     
        else:    
            print("EXITED Of Program")
            break