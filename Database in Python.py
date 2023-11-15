from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#SQLite
root = Tk()
root.title("Databases")
root.geometry("300x450")



#Create a table Only has to be ran once*
'''c.execute(""" CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text,
    province text,
    postalcode integer
)""")'''


def delete():
    conn = sqlite3.connect('address_book.db')
    
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + select_entry.get())
    
    
    conn.commit()
    
    conn.close()
    
    
def edit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    
    record_id = select_entry.get()
    c.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                province = :province,
                postalcode = :postalcode
                
                WHERE oid = :oid""",
                { 'first': f_name_updater.get(),
                  'last': l_name_updater.get(),
                  'address': address_updater.get(),
                  'city': city_updater.get(),
                  'province': province_updater.get(),
                  'postalcode': postalcode_updater.get(),
                  'oid': record_id
                })
    
    conn.commit()
    
    conn.close()
    updater.destroy()
    
    
    
def update():
    global updater
    updater = Tk()
    updater.title("Update Address")
    updater.geometry("300x450")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    
    record_id = select_entry.get()
    
    c.execute("SELECT *, oid FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()



    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"  #record[0] to get specific parts of the database
        
    global f_name_updater
    global l_name_updater
    global address_updater
    global city_updater
    global province_updater
    global postalcode_updater

    #Entry boxes for the update window
    f_name_updater = Entry(updater, width = 30)
    f_name_updater.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    l_name_updater = Entry(updater, width = 30)
    l_name_updater.grid(row = 1, column = 1)
    address_updater = Entry(updater, width = 30)
    address_updater.grid(row = 2, column = 1)
    city_updater = Entry(updater, width = 30)
    city_updater.grid(row = 3, column = 1)
    province_updater = Entry(updater, width = 30)
    province_updater.grid(row = 4, column = 1)
    postalcode_updater = Entry(updater, width = 30)
    postalcode_updater.grid(row = 5, column = 1)

    #Labels for entry boxes for update window
    f_name_label = Label(updater, text = "First Name")
    f_name_label.grid(row = 0, column = 0, pady = (10, 0))
    l_name_label = Label(updater, text = "Last Name")
    l_name_label.grid(row = 1, column = 0)
    address_label = Label(updater, text = "Address")
    address_label.grid(row = 2, column = 0)
    city_label = Label(updater, text = "City")
    city_label.grid(row = 3, column = 0)
    province_label = Label(updater, text = "Province")
    province_label.grid(row = 4, column = 0)
    postalcode_label = Label(updater, text = "Postal code")
    postalcode_label.grid(row = 5, column = 0)
    
    for record in records:
        f_name_updater.insert(0, record[0])
        l_name_updater.insert(0, record[1])
        address_updater.insert(0, record[2])
        city_updater.insert(0, record[3])
        province_updater.insert(0, record[4])
        postalcode_updater.insert(0, record[5])
    
    update_btn = Button(updater, text = "Save Record", command = edit)
    update_btn.grid(row = 6, column = 0, columnspan = 2, pady = (10, 0))

    conn.commit()
    
    conn.close()
    
    
    
def submit():
    #Create a database or connect to an existing one
    conn = sqlite3.connect('address_book.db')

    #Cursor 
    c = conn.cursor()
    
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :province, :postalcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'province': province.get(),
                'postalcode': postalcode.get()
            })
    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    #Clear the text boxes for additional entries
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    province.delete(0, END)
    postalcode.delete(0, END)
    
    
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM addresses")
    #Different ways to fetch: c.fetchmany(insert_number) c.fetchone()
    records = c.fetchall()  
    
    
    #print(records)
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"  #record[0] to get specific parts of the database
        
    query_label = Label(root, text = print_records)
    query_label.grid(row = 12, column = 0, columnspan = 2)
    conn.commit()
    conn.close()





f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

province = Entry(root, width = 30)
province.grid(row = 4, column = 1)

postalcode = Entry(root, width = 30)
postalcode.grid(row = 5, column = 1)


f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

province_label = Label(root, text = "Province")
province_label.grid(row = 4, column = 0)

postalcode_label = Label(root, text = "Postal code")
postalcode_label.grid(row = 5, column = 0)



submit_btn = Button(root, text = "Add record to database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 50)

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 5, padx = 10, ipadx = 77)

select_label = Label(root, text = "Select ID: ")
select_label.grid(row = 9, column = 0, padx = 10, pady = 10)
select_entry = Entry(root, width = 30)
select_entry.grid(row = 9, column = 1, pady = 10)

update_btn = Button(root, text = "Update Record", command = update)
update_btn.grid(row = 10, column = 0, columnspan = 2, pady = (10, 0))

delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 11, column = 0, columnspan = 2, pady = (10, 10), ipadx = 4)

root.mainloop()

