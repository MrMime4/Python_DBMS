from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

mydb = client['study']

mycollection = mydb['first']
 

class Node:
    
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
class LinkedList:
        
    def Display(self):
        find_query = mydb.first.find()
        for i in find_query:
            print(i)


    def Insert(self,name,age):
        rec = {'name': name,
            'age': age}
        try:
            insert_query = mydb.first.insert_one(rec)
            print("1 Record Added\n")
        except:
            print("Error On record Added\n")    


        
    def Delete(self,key):
        try:
            delete_query = mydb.first.delete_one({'name': key})
            print("1 Record Removed")
        except:
            print("Unable to Remove")    

 

        
    def Search(self,key):
        try:
            search_query = mydb.first.find({'name': key})
            print(f'Search result :=> {0}',(search_query[0]))
        except:
            print("No result Found..!")    
        
    
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
            key = input("Enter Name you want to Delete: ")
            llist.Delete(key)  
        elif (ch == '3'):
            llist.Display()  
        elif (ch == '4'):
            key = input("Enter Name you want to Search: ")
            llist.Search(key)     
        else:    
            print("EXITED Of Program")
            break