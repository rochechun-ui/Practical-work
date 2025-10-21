import numpy as np

def swap(x,y):
    return y,x #міняє місцями x і y

def procedure(data):
    a,b,c,d = data #розпаковуємо список у змінні
    a,b = swap(a,b)
    c,d = swap(c,d)
    b,c = swap(b,c)
    return[a,b,c,d] #повертаємо оновлений список

def Proc10():
    a = float(input("A = ")) #введення чисел
    b = float(input("B = "))
    c = float(input("C = "))
    d = float(input("D = "))    
    initial_data = [a, b, c, d] #створення списка із введених чисел
    result = procedure(initial_data) #виклик функції 
    print("A =",result[0],",B =",result[1],",C =",result[2],",D =",result[3])

   
def Matrix2():
    
    def process_file(filename):
            matrix = np.loadtxt(filename) #завантаження матриці з файлу
            m,n = matrix.shape #визначення кількості рядів та стовпців
            k = int(input("Введіть номер стовпця:"))
            if 1 <= k <= n: #перевірка чи є стовпець з номером k
                k_column = matrix[:, k - 1 ] #вибір стовпця з номером k
                k_sum = np.sum(k_column) #вичеслення суми з стовпця
                k_product = np.prod(k_column) #вичеслення добутку з стовпця
            else:
                print("Помилка")
            matrix_eye = np.eye(m, n) #створення одиничної матриці з значенням рядів та стовпців з заданої матриці 
            matrix_sum = matrix + matrix_eye #сума заданої матриці з одиничній матрицей 
            return k_sum,k_product,matrix_sum,k
                
    file = 'matrix.txt' #вибір файлу
    k_sum,k_product,matrix_sum,k = process_file(file)
    print("Сума стовпця",k,":",k_sum)
    print("Добуток стовпця",k,":",k_product)
    print("Сума заданої та одиничної матриць:\n",matrix_sum)