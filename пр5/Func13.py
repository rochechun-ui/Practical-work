import tkinter
from tkinter import messagebox

class func13(tkinter.Frame):
    
    def __init__(self, parent):
        super(func13, self).__init__(parent)
        self.parent = parent

        self.pack(fill=tkinter.BOTH, expand=1) #розтягнути фрейм за розмірами вікна
        self.grid_rowconfigure(0, weight=1) #налаштування сітки
        self.grid_columnconfigure(0, weight=1)


        self.lbl = tkinter.Label(self, text="Введіть 10 цілих чисел (>1) через кому:")
        
        
        self.entry_data = tkinter.Entry(self) #поле введення 

        
        self.btn = tkinter.Button(self, text="Розрахувати кількість простих чисел", command=self.calculate_func13) #командна кнопка

        
        self.res_str = tkinter.StringVar() #змінна для результату
        self.lbl_res = tkinter.Label(self, textvariable=self.res_str)

        
        self.lbl.grid(row=0, column=0, sticky = tkinter.NSEW) #розміщення віджетів у сітці 
        self.entry_data.grid(row=1, column=0, sticky=tkinter.NSEW, padx=50)
        self.btn.grid(row=2, column=0, sticky=tkinter.NSEW, padx=50, pady=5)
        self.lbl_res.grid(row=3, column=0, sticky=tkinter.NSEW, pady=5)

    def is_prime(self, n): #перевірка на просте число 
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def calculate_func13(self):
        try:
            
            get_text = self.entry_data.get() #зчитування з поля введення
            str_parts = get_text.split(',')
            if len(str_parts) != 10: #перевірка кількості
                messagebox.showwarning("Warning", "Має бути рівно 10 чисел!")
                return
            
            for i in str_parts: #перевірка чи числа більше 1
                num = int(i.strip()) 
                if num <= 1 :
                    messagebox.showwarning("Warning", "Числа повинні бути більше 1!")
                    return
            
            count = 0
            for i in str_parts: #рахунок простих чисел
                num = int(i.strip()) 
                if self.is_prime(num):
                    count += 1
            
            self.res_str.set(f"Простих чисел: {count}") #виведення результату

        except ValueError:
            messagebox.showerror("Data ERROR", "Введіть коректні цілі числа через кому!")

if __name__ == "__main__":
    application = tkinter.Tk()
    application.title("Func13")
    application.geometry("500x150")
    window = func13(application)
    application.mainloop()