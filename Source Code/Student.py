from tkinter import *
from tkinter import ttk
import pymysql

class Student:
   def __init__(self,root):
       self.root=root
       self.root.title("Student Management System")
       self.root.geometry("1350x700+0+0")

       title= Label(self.root,text="Students Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="white",fg="black")  
       title.pack(side=TOP,fill=X)
# -----------All Variables-------

       self.roll_var= StringVar()
       self.name_var= StringVar()
       self.email_var= StringVar()
       self.gender_var= StringVar()
       self.contact_var= StringVar()
       self.dob_var= StringVar()
       
       self.search_by= StringVar()
       self.search_txt= StringVar()

       



      #------- Manage Frame--------

       Manage_Frame= Frame(self.root,bd=4, relief=RIDGE,bg="grey")
       Manage_Frame.place(x=20,y=100,width=450,height=580)

       m_title= Label (Manage_Frame, text="Manage Students",fg="black", bg="white", font=("times new roman", 25, "bold") )
       m_title.grid(row=0,columnspan=2,pady=20 )

       lbl_roll= Label( Manage_Frame,text="Roll Number",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w" )

       txt_Roll= Entry(Manage_Frame, textvariable=self.roll_var, font=("times new roman", 15), bd=5, relief=GROOVE)
       txt_Roll.grid(row=1, column=1,pady=10,padx=20,sticky="w")

       lbl_name= Label( Manage_Frame,text="Name",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w" )

       txt_name= Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15 ), bd=5, relief=GROOVE)
       txt_name.grid(row=2, column=1,pady=10,padx=20,sticky="w")

       lbl_email= Label( Manage_Frame,text="Email",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w" )

       txt_email= Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 15), bd=5, relief=GROOVE)
       txt_email.grid(row=3, column=1,pady=10,padx=20,sticky="w")

       lbl_gender= Label( Manage_Frame,text="Gender",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w" )

       combo_gender= ttk.Combobox(Manage_Frame,textvariable=self.gender_var, font=("times new roman", 14, "bold"),state='readonly')
       combo_gender['values']= ("Male","Female","Other")
       combo_gender.grid(row=4, column=1, padx=20, pady=10)

    #    gender


       lbl_contact= Label( Manage_Frame,text="Contact",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w" )

       txt_contact= Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15 ), bd=5, relief=GROOVE)
       txt_contact.grid(row=5, column=1,pady=10,padx=20,sticky="w")

       lbl_dob= Label( Manage_Frame,text="Date of Birth",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w" )

       txt_dob= Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15), bd=5, relief=GROOVE)
       txt_dob.grid(row=6, column=1,pady=10,padx=20,sticky="w")

       lbl_address= Label( Manage_Frame,text="Address",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w" )

       self.txt_address= Text(Manage_Frame, width=30,height=4, font=("",10))
       self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

      #  Button Frame
       btn_Frame= Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
       btn_Frame.place(x=15, y=500, width=420)

       addbtn= Button(btn_Frame,text="Add",width=10, command= self.add_students ).grid(row=0,column=0,padx=10,pady=10)
       updatebtn= Button(btn_Frame,text="Update",width=10, command= self.update_data).grid(row=0,column=1,padx=10,pady=10)
       deletebtn= Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
       clearbtn= Button(btn_Frame,text="Clear",width=10,command= self.clear ).grid(row=0,column=3,padx=10,pady=10)

      
      #------- Detail Frame-------

       Detail_Frame= Frame(self.root,bd=4, relief=RIDGE,bg="grey")
       Detail_Frame.place(x=500,y=100,width=800,height=580)

       lbl_search= Label(Detail_Frame,text="Search By",fg="black", bg="white", font=("times new roman", 15, "bold"))
       lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w" )

       combo_search= ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=11, font=("times new roman", 14, "bold"),state='readonly')
       combo_search['values']= ("Name","Roll","Contact")
       combo_search.grid(row=0, column=1, padx=20, pady=10)

       txt_search= Entry(Detail_Frame,textvariable=self.search_txt, width=20, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
       txt_search.grid(row=0, column=2,pady=10,padx=20,sticky="w")

       searchbtn= Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
       showallbtn= Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

      # ------Table Frame----------

       Table_Frame= Frame(Detail_Frame,bd=4, relief=RIDGE,bg="grey")
       Table_Frame.place(x=16,y=60,width=760,height=500)

       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       
       self.Student_table= ttk.Treeview(Table_Frame,columns=("Roll", "Name","email","gender", "Contact No.","Date Of Birth","Address"),xscrollcommand= scroll_x.set, yscrollcommand=scroll_y.set )
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.Student_table.xview)
       scroll_y.config(command=self.Student_table.yview)

       self.Student_table.heading("Roll", text="Roll No.")
       self.Student_table.heading("Name", text="Name.")
       self.Student_table.heading("email", text="Email Address")
       self.Student_table.heading("gender", text="Gender")
       self.Student_table.heading("Contact No.", text="Contact No.")
       self.Student_table.heading("Date Of Birth", text="Date Of Birth")
       self.Student_table.heading("Address", text="Address")

       self.Student_table['show']='headings'

       self.Student_table.column("Roll",width=50)  
       self.Student_table.column("Name",width=100)  
       self.Student_table.column("email",width=100) 
       self.Student_table.column("Contact No.",width=100)  
       self.Student_table.column("Date Of Birth",width=100)  
       self.Student_table.column("Address",width=150) 
       self.Student_table.pack(fill=BOTH,expand=1)
       self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
       self.fetch_data()

      #  self.Student_table.pack()
   def add_students(self):
      con= pymysql.connect(host="localhost", user="root", password="",database="stm")
      cur=con.cursor()
      cur.execute("Insert into students values (%s,%s,%s,%s,%s,%s,%s)", (
         self.roll_var.get(),
         self.name_var.get(),
         self.email_var.get(),
         self.gender_var.get(),
         self.contact_var.get(),
         self.dob_var.get(),
         self.txt_address.get('1.0', END)


      ) )
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()

   def fetch_data(self):
      con= pymysql.connect(host="localhost", user="root", password="",database="stm")
      cur=con.cursor()
      cur.execute("select * from students")
      rows= cur.fetchall()
      if len(rows)!=0:
         self.Student_table.delete(*self.Student_table.get_children())
         for row in rows:
            self.Student_table.insert('', END, values=row)
            con.commit()
      con.close()

   def clear(self):
      self.roll_var.set("")
      self.name_var.set("")
      self.email_var.set("")
      self.gender_var.set("")
      self.contact_var.set("")
      self.dob_var.set("")
      self.txt_address.delete('1.0', END)

   def get_cursor(self,ev):
      cursor_row= self.Student_table.focus()
      contents= self.Student_table.item(cursor_row)
      row= contents['values']

      self.roll_var.set(row[0])
      self.name_var.set(row[1])
      self.email_var.set(row[2])
      self.gender_var.set(row[3])
      self.contact_var.set(row[4])
      self.dob_var.set(row[5])
      self.txt_address.delete('1.0', END)
      self.txt_address.insert(END,row[6])

   def update_data(self):
      con= pymysql.connect(host="localhost", user="root", password="",database="stm")
      cur=con.cursor()
      cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s", (

         self.name_var.get(),
         self.email_var.get(),
         self.gender_var.get(),
         self.contact_var.get(),
         self.dob_var.get(),
         self.txt_address.get('1.0', END),
         self.roll_var.get()


      ) )
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()
      
   def delete_data(self):
      con= pymysql.connect(host="localhost", user="root", password="",database="stm")
      cur=con.cursor()
      cur.execute("delete from students where roll=%s", self.roll_var.get())
      con.commit()
      con.close()
      self.fetch_data()
      self.clear()

   def search_data(self):
      con= pymysql.connect(host="localhost", user="root", password="",database="stm")
      cur=con.cursor()
      cur.execute("select * from students where "+ str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'"  )

      rows= cur.fetchall()
      if len(rows)!=0:
         self.Student_table.delete(*self.Student_table.get_children())
         for row in rows:
            self.Student_table.insert('', END, values=row)
            con.commit()
      con.close()













root= Tk()
ob= Student(root)
root.mainloop()
