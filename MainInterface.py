import tkinter as tk
from tkinter import ttk

class MyGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulačka - Teória čísiel")
        self.root.geometry("700x350")

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 13))
        self.style.configure('TNotebook.Tab', font=('Arial', 11))

        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text='Legenrov symbol')
        self.tabControl.add(self.tab2, text='Jacobiho symbol')
        self.tabControl.add(self.tab3, text='Solovay-Strassenov test')
        self.tabControl.pack(expand=1, fill='both')

        """ Tab 1 """
        ttk.Label(self.tab1, text='Legenrov symbol').grid(column=0, row=0, padx=30, pady=15)

        self.label1 = tk.Label(self.tab1, text="Vložte čitateľ:", font=('Arial', 10))
        self.label1.grid(column=0, row=1, pady=(10, 12), padx = (10,10))
        
        self.entry1 = tk.Entry(self.tab1)
        self.entry1.grid(column=1, row=1, pady=(10, 10), padx = (10,10))
        
        self.label2 = tk.Label(self.tab1, text="Vložte menovateľ:", font=('Arial', 10))
        self.label2.grid(column=0, row=2, pady=(10, 12), padx = (10,10))
        
        self.entry2 = tk.Entry(self.tab1)
        self.entry2.grid(column=1, row=2, pady=(10, 10), padx = (10,10))

        self.calculate_button = tk.Button(self.tab1, text="Vypočítať")
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx = (10,10))

        self.clear_button = tk.Button(self.tab1, text="Zmazať", command=lambda: self.clear_entry(1))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab1, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output = tk.Text(self.tab1, width="20", height = "0.5", font=("Arial", 10))
        self.output.grid(column=1, row=4, pady=(10, 10), padx = (10,10))

        """ Tab 2 """
        ttk.Label(self.tab2, text='Jacobiho symbol').grid(column=0, row=0, padx=30, pady=15)

        self.label1 = tk.Label(self.tab2, text="Vložte čitateľ:", font=('Arial', 10))
        self.label1.grid(column=0, row=1, pady=(10, 12), padx = (10,10))
        
        self.entry3 = tk.Entry(self.tab2)
        self.entry3.grid(column=1, row=1, pady=(10, 10), padx = (10,10))
        
        self.label2 = tk.Label(self.tab2, text="Vložte menovateľ:", font=('Arial', 10))
        self.label2.grid(column=0, row=2, pady=(10, 12), padx = (10,10))
        
        self.entry4 = tk.Entry(self.tab2)
        self.entry4.grid(column=1, row=2, pady=(10, 10), padx = (10,10))

        self.calculate_button = tk.Button(self.tab2, text="Vypočítať")
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx = (10,10))
        
        self.clear_button = tk.Button(self.tab2, text="Zmazať", command=lambda: self.clear_entry(2))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab2, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output = tk.Text(self.tab2, width="20", height = "0.5", font=("Arial", 10))
        self.output.grid(column=1, row=4, pady=(10, 10), padx = (10,10))

        """ Tab 3 """
        ttk.Label(self.tab3, text='Solovay-Strassenov test').grid(column=0, row=0, padx=30, pady=15)

        self.label1 = tk.Label(self.tab3, text="Vložte číslo:", font=('Arial', 10))
        self.label1.grid(column=0, row=1, pady=(10, 12), padx = (10,10))
        
        self.entry5 = tk.Entry(self.tab3)
        self.entry5.grid(column=1, row=1, pady=(10, 10), padx = (10,10))
        
        self.label2 = tk.Label(self.tab3, text="Vložte počet iterácií:", font=('Arial', 10))
        self.label2.grid(column=0, row=2, pady=(10, 12), padx = (10,10))
        
        self.entry6 = tk.Entry(self.tab3)
        self.entry6.grid(column=1, row=2, pady=(10, 10), padx = (10,10))

        self.calculate_button = tk.Button(self.tab3, text="Vypočítať")
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx = (10,10))

        self.clear_button = tk.Button(self.tab3, text="Zmazať", command=lambda: self.clear_entry(3))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab3, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output = tk.Text(self.tab3, width="20", height = "0.5", font=("Arial", 10))
        self.output.grid(column=1, row=4, pady=(10, 10), padx = (10,10))

    def clear_entry(self, tab_num):
        if tab_num == 1:
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
        elif tab_num == 2:
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
        elif tab_num == 3:
            self.entry5.delete(0, tk.END)
            self.entry6.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    MyGUI(root)
    root.mainloop()
