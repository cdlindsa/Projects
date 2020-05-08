
import tkinter as tk 
from tkinter import *

#https://www.geeksforgeeks.org/python-gui-tkinter/

class Patient:
    def __init__(self, first_name = '', last_name = '', id = '', sex = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.id = id

# Getters for return values and setters for a future editing option

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_id(self, id):
        self.id = id
    
    def set_sex(self, sex):
        self.sex = sex

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_id(self):
        return self.id
    
    def get_sex(self):
        return self.sex

def create_patient(new_w, first_name = '', last_name = '', id = '', sex = ''):
    new_w.destroy()

def new_window():
    new_w = tk.Tk(screenName=None,  baseName=None,  className='TK', useTk=1) 
    new_w.title('New Patient') 
    
    # First and Last name entries
    Label(new_w, text='First Name: ').grid(row=0)
    entry_FN = Entry(new_w).grid(row=0, column=1)
    Label(new_w, text='Last Name: ').grid(row=1)
    entry_LN = Entry(new_w).grid(row=1, column=1)
    Label(new_w, text='Patient ID: ').grid(row=2)
    entry_LN = Entry(new_w).grid(row=2, column=1)

    # Checkboxes
    Label(new_w, text='Sex:').grid(row=3)
    male = IntVar()
    female = IntVar()
    Checkbutton(new_w, text='Male', variable=male).grid(row=4, column=0, sticky=W)
    Checkbutton(new_w, text='Female', variable=female).grid(row=4, column=1, sticky=W)
    
    # Closing buttons
    accept_button = tk.Button(new_w, text='Accept', width=20, command=lambda : create_patient(new_w)).grid(row=5, column=0) 
    cancel_button = tk.Button(new_w, text='Cancel', width=20, command=new_w.destroy).grid(row=5, column=1) 


if __name__ == "__main__":
    main_window = tk.Tk(screenName=None,  baseName=None,  className='TK', useTk=1) 
    main_window.title('Patient Database Creator') 

    # Closing buttons
    new_patient_button = tk.Button(main_window, text='New Patient', height=5, width=15, command= lambda : new_window()).grid(row=5, column=0) 
    exit_button = tk.Button(main_window, text='Exit', height=5, width=15, command=main_window.destroy).grid(row=5, column=1) 


    main_window.mainloop() 