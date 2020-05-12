
import tkinter as tk 

#Skills Used to complete program: https://www.geeksforgeeks.org/python-gui-tkinter/

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
    w = Patient(first_name, last_name, id, sex)
    temp = 'Unknown'
    if w.get_sex() == 0:
        temp = 'Male'
    elif w.get_sex() == 1:
        temp = 'Female'
    print("FN: "+ w.get_firstname() +", LN: "+ w.get_lastname()+ ", sex: "+ temp + ", ID: " + str(w.get_id()))
    new_w.destroy()

def new_window():
    new_w = tk.Tk(screenName=None,  baseName=None,  className='TK', useTk=1) 
    new_w.title('New Patient') 
    
    # First and Last name entries
    tk.Label(new_w, text='First Name: ').pack()
    entry_FN = tk.Entry(new_w)
    entry_FN.pack()

    tk.Label(new_w, text='Last Name: ').pack()
    entry_LN = tk.Entry(new_w)
    entry_LN.pack()

    # Patient ID entry
    tk.Label(new_w, text='Patient ID: ').pack()
    entry_ID = tk.Entry(new_w)
    entry_ID.pack()
    SEXES = {
        "Male": 0, 
        "Female": 1
    }
    # Radiobuttons for sex
    tk.Label(new_w, text='Sex:').pack()
    sex = tk.IntVar(new_w, 5)
    for (sexes, value) in SEXES.items():
        checkbuttons = tk.Radiobutton(new_w, text=sexes, variable=sex, value=value)
        checkbuttons.pack()

    # Closing buttons
    accept_button = tk.Button(new_w, text='Accept', width=20, command=lambda : create_patient(new_w, entry_FN.get(), entry_LN.get(), entry_ID.get(), sex.get()))
    accept_button.pack()
    cancel_button = tk.Button(new_w, text='Cancel', width=20, command=new_w.destroy)
    cancel_button.pack() 


if __name__ == "__main__":
    main_window = tk.Tk(screenName=None,  baseName=None,  className='TK', useTk=1) 
    main_window.title('Patient Database Creator') 

    # Closing buttons
    new_patient_button = tk.Button(main_window, text='New Patient', height=5, width=15, command=lambda : new_window())
    new_patient_button.pack() 
    exit_button = tk.Button(main_window, text='Exit', height=5, width=15, command=main_window.destroy)
    exit_button.pack()  

    main_window.mainloop() 