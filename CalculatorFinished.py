import random
import tkinter as tk
from tkinter import ttk

""" Funkcia na detekciu prvočísiel """
def is_prime(N: int) -> bool:
    
    if not isinstance(N, int) or N <= 1:
        return False
    elif N == 2:
        return True
    elif N % 2 == 0:
        return False
    else:
        ukazovatel = 3
        while ukazovatel * ukazovatel <= N:
            if N % ukazovatel == 0:
                return False
            ukazovatel += 2       
    return True

""" Funkcia na faktorizáciu čísiel """
def factorize(N: int) -> list[int]:

    if not isinstance(N, int):
         raise ValueError("Nedefinovaný vstup - iba celé čísla")
    else:
        factors = []
        if N < 0:
            factors.append(-1)
            N *= -1
            
        ukazovatel = 2
        while ukazovatel * ukazovatel <= N:
            if N % ukazovatel == 0:
                factors.append(ukazovatel)
                N //= ukazovatel
            else:
                ukazovatel += 1

        if N > 1:
            factors.append(N)

    return factors

""" Funkcia pre Legendrov symbol """
def Legendre(A: int, P: int) -> int:

    if not isinstance(A, int):
        raise ValueError("Nedefinovaný vstup - iba celé čísla")

    if not is_prime(P) or P == 2:
        raise ValueError("Nedefinovaný vstup - menovateľ musí byť nepárne prvočíslo")

    if A % P == 0:
        return 0

    if A == 1:
        return 1

    if A == -1:
        return int((-1)**((P-1)/2))
    
    if A == 2:
        return int((-1)**((P**2 -1)/8))

    factors = factorize(A)

    if -1 in factors:
        A *= -1
        return Legendre(-1, P) * Legendre(A, P)

    if A != (A % P):
        return Legendre(A % P, P)
    
    if len(factorize(A)) > 1:
        legendre_product = 1
        for factor in factors:
            legendre_product *= Legendre(factor, P)
        return legendre_product

    quad_recip = int((-1)**(((A-1)*(P-1))/4))

    return quad_recip * Legendre(P, A)

""" Funkcia pre Jacobiho symbol """
def Jacobi(A: int, N: int) -> int:

    if not isinstance(A, int) or not isinstance(N, int):
        raise ValueError("Nedefinovaný vstup - iba celé čísla")

    if N <= 0 or N % 2 == 0:
        raise ValueError("N musí byť nenulové nepárne kladné číslo")

    if A % N == 0:
        return 0

    if A == 1:
        return 1

    if A == -1:
        return int((-1)**((P-1)/2))

    if A == 2:
        return int((-1)**((N**2 -1)/8))

    if A != (A % N):
        return Jacobi(A % N, N)

    parity = 0

    while A % 2 == 0:
        parity += 1
        A //= 2

    factors = factorize(N)

    result_1 = 1
    
    if parity > 0:
        for factor in factors:
            result_1 *= Legendre(2, factor)
        result_1 = result_1**parity

    if A == 1:
        return result_1
    else:
        result_2 = ((-1)**(((A-1)*(N-1))/4)) * Jacobi(N, A)

    result = int(result_1 * result_2)

    return result

""" Funkcia pre Solovay-Strassenov test """
def Sol_Stra_test(N: int, iterations: int) -> bool:
    
    if N < 2 or N % 2 == 0:
        return "N je zložené číslo"

    if N == 2:
        return "N je pravdepodobne prvočíslo"

    for _ in range(iterations):
        
        num = random.randint(2, N)
        
        jacobi_symbol = Jacobi(num, N)
        
        modular_exponentiation = pow(num, (N - 1) // 2, N)

        if jacobi_symbol % N != modular_exponentiation % N:
            return "N je zložené číslo"

    return "N je pravdepodobne prvočíslo"

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

        self.calculate_button = tk.Button(self.tab1, text="Vypočítať", command=self.calculate_legendre)
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx=(10, 10))

        self.clear_button = tk.Button(self.tab1, text="Zmazať", command=lambda: self.clear_entry(1))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab1, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output1 = tk.Text(self.tab1, width="30", height="0.5", font=("Arial", 10))
        self.output1.grid(column=1, row=4, pady=(10, 10), padx=(10, 10))

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

        self.calculate_button = tk.Button(self.tab2, text="Vypočítať", command=self.calculate_jacobi)
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx=(10, 10))
        
        self.clear_button = tk.Button(self.tab2, text="Zmazať", command=lambda: self.clear_entry(2))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab2, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output2 = tk.Text(self.tab2, width="30", height="0.5", font=("Arial", 10))
        self.output2.grid(column=1, row=4, pady=(10, 10), padx=(10, 10))

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

        self.calculate_button = tk.Button(self.tab3, text="Vypočítať", command=self.calculate_sol_stra)
        self.calculate_button.grid(column=1, row=3, pady=(10, 10), padx=(10, 10))

        self.clear_button = tk.Button(self.tab3, text="Zmazať", command=lambda: self.clear_entry(3))
        self.clear_button.grid(column=0, row=3, pady=(10, 10), padx = (10,10))

        self.label_text = tk.Label(self.tab3, text="Výsledok:", font=("Arial", 10))
        self.label_text.grid(column=0, row=4, pady=(10, 12), padx = (10,10))
        
        self.output3 = tk.Text(self.tab3, width="30", height="0.5", font=("Arial", 10))
        self.output3.grid(column=1, row=4, pady=(10, 10), padx=(10, 10))

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

    def calculate_legendre(self):
        try:
            A = int(self.entry1.get())
            P = int(self.entry2.get())
            result = Legendre(A, P)
            self.output1.delete(1.0, tk.END)
            self.output1.insert(tk.END, str(result))
        except ValueError as e:
            self.output1.delete(1.0, tk.END)
            self.output1.insert(tk.END, str(e))

    def calculate_jacobi(self):
        try:
            A = int(self.entry3.get())
            N = int(self.entry4.get())
            result = Jacobi(A, N)
            self.output2.delete(1.0, tk.END)
            self.output2.insert(tk.END, str(result))
        except ValueError as e:
            self.output2.delete(1.0, tk.END)
            self.output2.insert(tk.END, str(e))

    def calculate_sol_stra(self):
        try:
            N = int(self.entry5.get())
            iterations = int(self.entry6.get())
            result = Sol_Stra_test(N, iterations)
            self.output3.delete(1.0, tk.END)
            self.output3.insert(tk.END, str(result))
        except ValueError as e:
            self.output3.delete(1.0, tk.END)
            self.output3.insert(tk.END, str(e))

if __name__ == '__main__':
    root = tk.Tk()
    MyGUI(root)
    root.mainloop()
