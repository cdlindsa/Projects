import tkinter as tk 

#Skills Used to complete program: https://www.geeksforgeeks.org/python-gui-tkinter/

class Patient:
    def __init__(self, first_name, last_name, id, sex):
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
    sex_final = 'Unknown'
    if sex == 0:
        sex_final = 'Male'
    elif sex == 1:
        sex_final = 'Female'
    w = Patient(first_name, last_name, id, sex_final)
    into_the_db(w)
    new_w.destroy()

def into_the_db(w):
        print("FN: "+ w.get_firstname() +", LN: "+ w.get_lastname() + ", sex: "+ w.get_sex() + ", ID: " + w.get_id())

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

    # Radiobuttons for sex
    SEXES = {"Male": 0, "Female": 1}
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

class MainWindow(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.root.title('Patient Database Creator') 
        
    def setup(self): 
        # Closing buttons
        self.new_patient_button = tk.Button(self.root, text='New Patient', height=5, width=15, command=lambda : new_window())
        self.new_patient_button.grid(row = 0, column = 0, padx=5, pady=5) 
        self.export_button = tk.Button(self.root, text='Export CSV', height=5, width=15, command=self.root.destroy)
        self.export_button.grid(row = 0, column = 1, padx=5, pady=5)  
        self.exit_button = tk.Button(self.root, text='Exit', height=5, width=32, command=self.root.destroy)
        self.exit_button.grid(row = 1, columnspan=2, padx=5, pady=5) 


if __name__ == "__main__":
    root = tk.Tk() 
    main_window = MainWindow(root)
    main_window.setup() 
    root.mainloop() 