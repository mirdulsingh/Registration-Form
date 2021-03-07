import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.geometry('400x400')
win.title('Resgistration Form')


# Create lable
name_lable = ttk.Label(win, text= 'Enter your name : ')
name_lable.grid(row=0, column=0,sticky=tk.W,padx=40, pady=18)

email_lable = ttk.Label(win, text= 'Enter your e-mail address :')
email_lable.grid(row=1, column=0,sticky=tk.W,padx=40, pady=18)


age_lable = ttk.Label(win, text= 'Enter your age :' )
age_lable.grid(row=2, column=0, sticky=tk.W,padx=40, pady=18)


gender_lable = ttk.Label(win, text= 'Select your gender :' )
gender_lable.grid(row=3, column=0, sticky=tk.W,padx=40, pady=18)


user_lable = ttk.Label(win, text= 'Select your type :' )
user_lable.grid(row=4, column=0, sticky=tk.W,padx=40, pady=18)


# Create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=18, textvariable = name_var)
name_entrybox.grid(row=0,column=1,padx=40, pady=18)


email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=18, textvariable = email_var)
email_entrybox.grid(row=1,column=1,padx=40, pady=18)


age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=18, textvariable = age_var)
age_entrybox.grid(row=2,column=1,padx=40, pady=18)


# Create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width= 14, textvariable= gender_var, state = 'readonly')
gender_combobox['values'] = ('Select','Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row= 3, column=1,padx=40, pady=18)




# Create Radio Button
user_var = tk.StringVar()
button1 = ttk.Radiobutton(win, text='Student', value='Student', variable=user_var)
button1.grid(row=4,column=1,padx=40, pady=18)

button2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=user_var)
button2.grid(row=4,column=2,padx=40, pady=18)


# Check Button
check_var = tk.IntVar()
checkbtn1 = ttk.Checkbutton(win, text='Subscribe...!!! if you are new here', variable=check_var)
checkbtn1.grid(row=5,columnspan=4, sticky=tk.W,padx=40, pady=18)


# Submit Button
def action():
    username = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get() 
    user_type = user_var.get()
    if check_var.get() == 0:
        subscribed = 'No'
    subscribed = 'Yes'

    # Write to CSV file
    with open('file.csv', 'a',newline='') as f:
        dict_writer = DictWriter(f,fieldnames=['User Name','User Email Address','User Age','User Gender','User Type','Subscribe'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'User Name' : username,
            'User Email Address': user_email,
            'User Age': user_age,
            'User Gender': user_gender,
            'User Type': user_type,
            'Subscribe': subscribed
        })
    
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)


submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=8,column=0,sticky=tk.W)


win.mainloop()