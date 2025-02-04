from tkinter import *
import mysql.connector
from tkinter import ttk, messagebox
import string
import random
import uuid

# Initialize the main window
root = Tk()
root.title("College Management System")
root.geometry("1000x600+200+100")
root.resizable(False, False)

# Function to close the window
def on_closing():
    root.destroy()

# Helper function to generate a unique course ID
def random_course_id():
    return str(uuid.uuid4()).split('-')[0].upper()

# Functions to manage courses
def add_course():
    if CourseNameEntry.get() == "" or SemesterEntry.get() == "" or DepartmentEntry.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        course_name = CourseNameEntry.get()
        semester = SemesterEntry.get()
        department = DepartmentEntry.get()
        course_id = random_course_id()
        db = mysql.connector.connect(host="localhost", user="root", password="Ayesha123@", database="College_db")
        mycursor = db.cursor()
        try:
            mycursor.execute("INSERT INTO course_table (course_id, course_name, semester, department) VALUES (%s, %s, %s, %s)",
                             (course_id, course_name, semester, department))
            db.commit()
            messagebox.showinfo("Success", "Course added successfully")
            show_courses()
            clear_course_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            db.rollback()
        db.close()

def update_course():
    course_id = CourseIdEntry.get()
    course_name = CourseNameEntry.get()
    semester = SemesterEntry.get()
    department = DepartmentEntry.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Ayesha123@", database="College_db")
    mycursor = db.cursor()
    try:
        mycursor.execute("UPDATE course_table SET course_name = %s, semester = %s, department = %s WHERE course_id = %s",
                         (course_name, semester, department, course_id))
        db.commit()
        messagebox.showinfo("Success", "Course updated successfully")
        show_courses()
        clear_course_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        db.rollback()
    db.close()

def delete_course():
    course_id = CourseIdEntry.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Ayesha123@", database="College_db")
    mycursor = db.cursor()
    try:
        mycursor.execute("DELETE FROM course_table WHERE course_id = %s", (course_id,))
        db.commit()
        messagebox.showinfo("Success", "Course deleted successfully")
        show_courses()
        clear_course_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        db.rollback()
    db.close()

def show_courses():
    db = mysql.connector.connect(host="localhost", user="root", password="Ayesha123@", database="College_db")
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM course_table")
    rows = mycursor.fetchall()
    CourseTable.delete(*CourseTable.get_children())
    for row in rows:
        CourseTable.insert('', END, values=row)
    db.close()

def get_course_data(event):
    currow = CourseTable.focus()
    contents = CourseTable.item(currow)
    row = contents['values']
    CourseIdEntry.delete(0, END)
    CourseNameEntry.delete(0, END)
    SemesterEntry.delete(0, END)
    DepartmentEntry.delete(0, END)
    CourseIdEntry.insert(0, row[0])
    CourseNameEntry.insert(0, row[1])
    SemesterEntry.insert(0, row[2])
    DepartmentEntry.insert(0, row[3])

def clear_course_fields():
    CourseIdEntry.delete(0, END)
    CourseIdEntry.insert(0, random_course_id())
    CourseNameEntry.delete(0, END)
    SemesterEntry.delete(0, END)
    DepartmentEntry.delete(0, END)

# Header
header = Frame(root, bg="brown", bd=0)
header.place(x=0, y=0, width=1000, height=75)
Label(header, text="College Management System", font=("Helvetica", 28, "bold"), bg="brown", fg="#eae2b7").pack()

# Course Management Frame
course_frame = Frame(root, bg="brown", bd=0)
course_frame.place(x=10, y=100, width=450, height=450)

Label(course_frame, text="Manage Courses", font=("Helvetica", 20, "bold"), bg="brown", fg="#eae2b7").pack()

Label(course_frame, text="Course ID", font=("Helvetica", 15), bg="brown", fg="#eae2b7").place(x=10, y=50)
CourseIdEntry = Entry(course_frame, font=("Helvetica", 15), bd=0)
CourseIdEntry.place(x=150, y=50, width=200)
CourseIdEntry.insert(0, random_course_id())

Label(course_frame, text="Name", font=("Helvetica", 15), bg="brown", fg="#eae2b7").place(x=10, y=100)
CourseNameEntry = Entry(course_frame, font=("Helvetica", 15), bd=0)
CourseNameEntry.place(x=150, y=100, width=200)

Label(course_frame, text="Semester", font=("Helvetica", 15), bg="brown", fg="#eae2b7").place(x=10, y=150)
SemesterEntry = Entry(course_frame, font=("Helvetica", 15), bd=0)
SemesterEntry.place(x=150, y=150, width=200)

Label(course_frame, text="Department", font=("Helvetica", 15), bg="brown", fg="#eae2b7").place(x=10, y=200)
DepartmentEntry = Entry(course_frame, font=("Helvetica", 15), bd=0)
DepartmentEntry.place(x=150, y=200, width=200)

Button(course_frame, text="Add", font=("Helvetica", 12), bg="indianred", fg="white", bd=0, command=add_course).place(x=50, y=250, width=70)
Button(course_frame, text="Update", font=("Helvetica", 12), bg="indianred", fg="white", bd=0, command=update_course).place(x=150, y=250, width=70)
Button(course_frame, text="Delete", font=("Helvetica", 12), bg="indianred", fg="white", bd=0, command=delete_course).place(x=250, y=250, width=70)
Button(course_frame, text="Clear", font=("Helvetica", 12), bg="indianred", fg="white", bd=0, command=clear_course_fields).place(x=150, y=300, width=70)

# Course Table Frame
course_table_frame = Frame(root, bg="indianred", bd=0)
course_table_frame.place(x=470, y=100, width=520, height=450)

scrolly = Scrollbar(course_table_frame, orient=VERTICAL)
CourseTable = ttk.Treeview(course_table_frame, columns=("course_id", "course_name", "semester", "department"), yscrollcommand=scrolly.set)
scrolly.pack(side=RIGHT, fill=Y)
scrolly.config(command=CourseTable.yview)

CourseTable.heading("course_id", text="Course ID")
CourseTable.heading("course_name", text="Name")
CourseTable.heading("semester", text="Semester")
CourseTable.heading("department", text="Department")
CourseTable['show'] = "headings"
CourseTable.pack(fill=BOTH, expand=1)
CourseTable.bind("<ButtonRelease-1>", get_course_data)

show_courses()
root.mainloop()
