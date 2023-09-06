
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="chandan", database="project")
mycur=mydb.cursor()
print("==============================CENTRAL LIBRARY===================================")
c="y"
while c=="y" or c=="Y" :
              print("1. BOOK ISSUE" '\n'
                    "2. BOOK RETURN" '\n'
                    "3. BOOK STATUS"'\n'
                    "4. NEW BOOK"'\n'
                    "5. LIBRARY STATUS"'\n'
                    "6. NEW DONATORS"'\n'
                    "7. DONATORS"'\n')
              a=int(input("ENTER YOUR CHOICE : "))
              if a==1:
                            c=input("Enter bookname : ")
                            querry="select * from books where bookname=%s"
                            value=(c,)
                            mycur.execute(querry,value)
                            myresult=mycur.fetchall()
                            x=mycur.rowcount
                            for row in myresult:
                                e=row[4]
                            ans="yes"
                            sql="UPDATE books SET issuestatus= %s WHERE bookname= %s"
                            val=(ans,c)
                            if x>0 and e!="yes":
                                print("%10s"%"book no","%20s"%"bookname","%10s"%"shelf no","%10s"%"ROW NO")
                                for row in myresult:
                                    print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%10s"%row[3])
                                q="update books set issuedate= curdate() where bookname= %s"
                                valu=(c,)
                                mycur.execute(q,valu)
                                try:
                                    mycur.execute(sql,val)
                                    mydb.commit()
                                    print("================================BOOK ISSUED====================================")
                                except:
                                    print("=========================SORRY WE DON'T HAVE THAT BOOK=====================")
                                    mydb.close()
                            elif e=="yes":
                                print("========================BOOK ALREADY ISSUED===========================")
                            else:
                                print("=========================SORRY WE DON'T HAVE THAT BOOK=====================")
                                
                                
              elif a==2:
                        c=input("Enter bookname : ")
                        querry="select * from books where bookname=%s"
                        value=(c,)
                        mycur.execute(querry,value)
                        myresult=mycur.fetchall()
                        x=mycur.rowcount
                        for row in myresult:
                            e=row[4]
                        ans="No"
                        sql="UPDATE books SET issuestatus= %s WHERE bookname= %s"
                        val=(ans,c)
                        if x>0 and e=="yes":
                            print("%10s"%"book no","%20s"%"bookname","%10s"%"shelf no","%10s"%"ROW NO")
                            for row in myresult:
                                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%10s"%row[3])
                                j="delete from books where bookno= %s"
                                v=(row[0],)
                                mycur.execute(j,v)
                                q="INSERT INTO books(bookno,bookname,shelfno,rowno,issuestatus) VALUES(%s,%s,%s,%s,%s)"
                                valu=(row[0],row[1],row[2],row[3],"No")
                                mycur.execute(q,valu)
                            try:
                                mycur.execute(sql,val)
                                mydb.commit()
                                print("================================BOOK RETURNED===================================")
                            except:
                                print("=========================SORRY WE DON'T HAVE THAT BOOK=====================")
                                mydb.close()
                        elif e=="No":
                                print("========================BOOK HASN'T BEEN ISSUED=============================")
                        else:
                            print("=========================SORRY WE DON'T HAVE THAT BOOK=====================")    
              elif a==3:
                            a=input("ENTER BOOKNAME :")
                            sql="select * from books where bookname=%s"
                            val=(a,)
                            mycur.execute(sql,val)
                            myresult=mycur.fetchall()
                            print("%10s"%"book no","%20s"%"bookname","%10s"%"shelf no","%10s"%"ROW NO","%10s"%"issuestatus","%20s"%"issuedate")
                            for row in myresult:
                                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%10s"%row[3],"%10s"%row[4],"%20s"%row[5])
              elif a==4:
                            def newbook():
                                          sql="SELECT MAX(bookno) FROM books"
                                          mycur.execute (sql)
                                          myresult=mycur.fetchone()
                                          n=int(input("ENTER NUMBER OF NEW BOOKS : "))
                                          for i in range(0, n):
                                                        a= input("BOOK NAME : ")
                                                        b=myresult[0]+i+1
                                                        c=int(input("shelf no.: "))
                                                        d=int(input("row : "))
                                                        e="No"
                                                        sql="INSERT INTO books(bookno,bookname,shelfno,rowno,issuestatus) VALUES(%s,%s,%s,%s,%s)"
                                                        val=(b,a,c,d,e)
                                                        mycur.execute(sql,val)
                                                        mydb.commit()
                                                        print(mycur.rowcount,"record(s) inserted")
                            newbook()
              elif a==5:
                            sql="select * from books"
                            mycur.execute(sql)
                            myresult=mycur.fetchall()
                            print("%10s"%"Book no","%50s"%"Bookname","%10s"%"Shelf no","%10s"%"Row no","%10s"%"Issuestatus","%20s"%"Issuedate")
                            for row in myresult:
                                          print("%10s"%row[0],"%50s"%row[1],"%10s"%row[2],"%10s"%row[3],"%10s"%row[4],"%20s"%row[5])
              

              elif a==6:
                  import csv
                  with open ('donators.csv','a',newline='')as file:
                      writer=csv.writer(file)
                      global n
                      n=int (input("ENTER NUMBER OF ENNTRIES : "))
                      for i in range(0,n):
                          did=int(input("ENTER DONATOR'S ID : "))
                          global b
                          b=input("ENTER BOOKNAME : ")
                          d=input("ENTER DONATOR'S NAME : ")
                          writer.writerow([did,b,d])
                          sql="SELECT MAX(bookno) FROM books"
                          mycur.execute (sql)
                          myresult=mycur.fetchone()
                          a= b
                          x=myresult[0]+1
                          c=int(input("SHELF NUMBER: "))
                          d=int(input("ROW NUMBER : "))
                          e="No"
                          sql="INSERT INTO books(bookno,bookname,shelfno,rowno,issuestatus) VALUES(%s,%s,%s,%s,%s)"
                          val=(x,a,c,d,e)
                          mycur.execute(sql,val)
                          mydb.commit()
                          print(mycur.rowcount,"record(s) inserted")
              elif a==7:
                import csv
                with open ('donators.csv','r')as file:
                    reader=csv.reader(file)
                    for row in reader:
                        print("%10s"%row[0],"%20s"%row[1],"%20s"%row[2])
              print(" ")
              c=input("Enter y tO CONTINUE and n to STOP : ")
              print(" ")
              
                                          
              
                                          

                             

              



