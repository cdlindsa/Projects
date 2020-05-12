import tkinter as tk
import sys

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

class NewPatient(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.title('New Patient')
        self.new_patient_setup(root) 

    def new_patient_setup(self, root): 
        # First and Last name entries
        self.FN_label = tk.Label(root, text='First Name: ').grid(row = 0, column = 0, sticky=tk.W)
        self.entry_FN = tk.Entry(root)
        self.entry_FN.grid(row = 0, column = 1)
        self.LN_label = tk.Label(root, text='Last Name: ').grid(row = 1, column = 0, sticky=tk.W)
        self.entry_LN = tk.Entry(root)
        self.entry_LN.grid(row = 1, column = 1)

        # Patient ID entry
        self.ID_label = tk.Label(root, text='Patient ID: ').grid(row = 2, column = 0, sticky=tk.W)
        self.entry_ID = tk.Entry(root)
        self.entry_ID.grid(row = 2, column = 1)

        # Radiobuttons for sex
        self.SEXES = {"Male": 0, "Female": 1}
        self.sex_label = tk.Label(root, text='Sex:').grid(row = 3, column = 0, sticky=tk.W)
        self.sex = tk.IntVar(root, sys.maxsize)
        self.create_radiobuttons(root, self.sex, self.SEXES)
        
        # Closing buttons
        self.accept_button = tk.Button(root, text='Accept', width=20, command=lambda : self.create_patient(root, self.entry_FN.get(), self.entry_LN.get(), self.entry_ID.get(), self.sex.get()))
        self.accept_button.grid(row = 6, column = 0)
        self.cancel_button = tk.Button(root, text='Cancel', width=20, command=root.destroy)
        self.cancel_button.grid(row = 6, column = 1)
    
    # Helper Functions
    def create_radiobuttons(self, root, variable, labels):
        for (key, value) in labels.items():
            self.variable = variable
            self.checkbuttons = tk.Radiobutton(root, text=key, variable=self.variable, value=value)
            self.checkbuttons.grid(sticky=tk.W)

    def create_patient(self, root, first_name = '', last_name = '', id = '', sex = ''):
        sex_final = 'Unknown'
        if sex == 0:
            sex_final = 'Male'
        elif sex == 1:
            sex_final = 'Female'
        w = Patient(first_name, last_name, id, sex_final)
        self.into_the_db(w)
        root.destroy()

    def into_the_db(self, w):
            print("FN: "+ w.get_firstname() +", LN: "+ w.get_lastname() + ", sex: "+ w.get_sex() + ", ID: " + w.get_id())

class MainWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.title('Patient Database Creator') 
        
    def setup(self): 
        # Closing buttons
        self.new_patient_button = tk.Button(self.root, text='New Patient', height=5, width=15, command=lambda : NewPatient(tk.Tk()))
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