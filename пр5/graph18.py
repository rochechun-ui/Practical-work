import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class graph18(tkinter.Frame):
    
    def __init__(self, parent):
        super(graph18, self).__init__(parent)
        self.parent = parent
        
        self.pack(fill=tkinter.BOTH, expand=1) #розтягнути фрейм за розмірами вікна
        
        self.grid_rowconfigure(1, weight=1) #налаштування сітки
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.btn1 = tkinter.Button(self, text="Open file", command=self.openfile) #кнопки інтерфейсу
        self.btn2 = tkinter.Button(self, text="Show content", command=self.showmsg)
        self.btn3 = tkinter.Button(self, text="Show plot", command=self.showplot)
        self.btn4 = tkinter.Button(self, text="Create file", command=self.create_file)
        
        self.btn1.grid(row=0, column=0, sticky=tkinter.NSEW) #розміщення кнопок у сітці 
        self.btn2.grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btn3.grid(row=0, column=2, sticky=tkinter.NSEW)
        self.btn4.grid(row=0, column=3, sticky=tkinter.NSEW)
        
        self.text = []  #збереження тексту з файлу
        

        self.drawing = None #полотно графіка 

    def calculate(self): #обчислення масиву t та y за заданими формулами

        T = 1.4
        K = 3.7
        xi = 2.5
        U = 1.0
        
        N = 100 
        T0 = (2 * T) / 50 
        
        self.y_arr = [0.0] * N
        self.t_arr = [0.0] * N
        

        
        A = 2 * (1 - (xi * T0) / T)
        B = ((2 * xi * T0) / T) - 1 - (T0**2)/(T**2)
        C = (K * (T0**2)) / (T**2)

        for k in range(N): #розрахунок y(k)
            self.t_arr[k] = k * T0
            if k < 2:
                self.y_arr[k] = 0.0
            else:
                self.y_arr[k] = A * self.y_arr[k-1] + B * self.y_arr[k-2] + C * U

    def create_file(self): #створення файлу
        self.calculate()
        
        fopen = asksaveasfile(mode='w', defaultextension=".txt",
                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        
        if fopen is None: return
        
        for i in range(len(self.y_arr)):
            t_val = self.t_arr[i]
            y_val = self.y_arr[i]
            fopen.write(f"{t_val:.4f};{y_val:.4f}\n")
            
        fopen.close()
        messagebox.showinfo("Done", "Файл створено")

    def openfile(self): #читання файлу
        fopen = askopenfile(mode='r', defaultextension=".txt",
                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if fopen is None: return
        self.text = fopen.readlines()  
        fopen.close()

    def showmsg(self):
        if not self.text:
            messagebox.showwarning("Warning", "Даних немає")
            return
        content = "".join(self.text[:15]) + "І далі\n" #показати 15 рядків
        messagebox.showinfo("File content", content)

    def showplot(self): #побудування графіка
        x = []
        y = []
        try:
            for line in self.text: 
                words = line.strip().split(';')
                if len(words) >= 2:
                    x.append(float(words[0])) 
                    y.append(float(words[1])) 
            
            if not x: raise ValueError("Даних немає")


            if self.drawing: #видалення старого графіка
                self.drawing.get_tk_widget().destroy()

            fig = Figure(figsize=(5, 4), dpi=100)   #створення нового графіка
            ax = fig.add_subplot(111) 
            
            ax.plot(x, y) 
            ax.grid(True)
            ax.set_title("graph18")
            ax.set_xlabel("Час t, с")
            ax.set_ylabel("ω, рад/с")


            self.drawing = FigureCanvasTkAgg(fig, master=self)
            self.drawing.get_tk_widget().grid(row=1, column=0, columnspan=4, sticky=tkinter.NSEW)
            self.drawing.draw()

        except Exception as e:
            messagebox.showerror("Data ERROR", f"Помилка з даними\n{e}")

if __name__ == "__main__":
    application = tkinter.Tk()
    application.title("lab5-526-v18-Chechun-Ruslan")
    application.geometry("600x500")
    window = graph18(application)
    application.mainloop()