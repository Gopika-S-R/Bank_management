import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# cur.execute("create database DjangoORM")
# print("Database created")


# cur.execute('''create table employee(id int primary key auto_increment,
#     name varchar(30),
#     designation varchar(30),
#     salary decimal(10,2))
# ''')
# print("table created")
# Object-Relational Mapping






class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=','
                placeholder+=','
            cols+=col
            placeholder+='%s'
        values=tuple(kwargs.values())
        print(f"insert into employee ({cols}) values ({placeholder}),{values}")
        # query=f"insert into employee ({cols}) values ({placeholder})"
        # cur.execute(query,values)
        # print("Data inserted")
        # conn.commit()
            

    def list(self,*args,**kwargs):
        cur.execute("select *from employee")
        print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT *FROM employee WHERE {key}={kwargs.get ( key)}")
            print(cur.fetchall())
    def update(self,*args,**kwargs):
            print(args,kwargs)
            for key in kwargs:
               
                cur.execute(f"update employee set '{key}={kwargs.get(key)}' where id={args[0]}")
                conn.commit()

    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select *from employee where {key}= ' {kwargs.get(key)}' ")


    def delete(self,*args,**kwargs):
        cur.execute("delete from employee where id={args[0]}")
        conn.commit()


employee=Employee()

while True:
    print("1.Create employee")
    print("2.List all employees")
    print("3.Employee detail view")
    print("4.Update employee")
    print("5.Delete employee")
    print("6.Filter employees")
    print("7.Exit")

    choice=int(input("Enter the choice:"))
    if choice==1:
        name=input("Enter the employee name:")
        desig=input("Enter the designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=desig,salary=salary)

    elif choice==2:
        employee.list()

    elif choice==3:
        print("")
        employee.retrieve("enter the employee ID:")
        employee.retrieve(id=id)
    elif choice==4:
        id=int(input("enter the id of employee:"))
        print("update:")
        print("1.name")
        print("2.Designation")
        print("3.Salary")
        choice=int(input("enter you choice:"))
        if choice==1:
            name=input("enter the new name")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("enter the new designation")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("enter the new salary:"))
            employee.update("id,salary=salary ")
        else:
            print("invalid choice")

    elif choice==5:
        id=int(input("enter the employee ID:"))
        employee.delete(id)

    elif choice==6:
        print("Filter options:")
        print("1.Filter by name:")
        print("1.Filter by designation:")
        print("1.Filter by salary:")
        choice=int(input("enter you choice:"))
        if choice==1:
            name=input("enter a name:")
            employee.filter(name=name)
        elif choice ==2:
            desig=input("enter the designation:")
            employee.filter(designation=desig)
        elif choice == 3:
            salary=float(input("enter a salary:"))
            employee.filter(salary=salary)


        employee.filter()
    elif choice==7:
        print("Thank you")
        break
    else:
        print("Invalid choice")
        





#hi






conn.close()
print("connection closed")
