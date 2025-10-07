import math
def task_if12():
    try:
        num1 = float(input("num1 = ")) #введення числел
        num2 = float(input("num2 = "))
        num3 = float(input("num3 = "))
    except:
        print("Повинні бути числа") #повідомлення про помилку якщо введено не число
    else:
        if num1 > num2: #порівняння першого число з другим та позначення найменшого
            min_num = num2
        else:
            min_num = num1
        if num3 < min_num:#порівняння третього число з найменшим з першої пари чисел
            min_num = num3
            
        print("Найменьше число: ", min_num)#виведення найменшого числа

def task_geom_area20():
    try:
        a = 15
        r = 5
        x = float(input("x = "))
        y = float(input("y = "))
    except:
        print("Повинні бути числа")
    else:
        area1 = x**2 + y**2 < r**2 and x > 0 and 0 < y < x #визначення чи знаходится точка в першій області
        area2 = x**2 + y**2 > r**2 and x < 0 and 0 < -x < y and y < a 
        #визначення чи знаходится точка в другій області

        if area1:
            print("Точка в області якак знаходится у колі та обмежена від 0 до 45 градусів")
        elif area2:
            print("Точка в області якак знаходится за колом та обмежена від 90 до 135 градусів і сторонами квадрата")
        else:
            print("Точка не знаходится в областях")
            
def task_series22():
        x = float(input("x = ")) 
        n = 1 #лічильник ітерацій
        s = u = 2.0 #початкові значення суми та члена ряду
        e = 1e-10 #точність обчислення
        while abs(u) > e: #виконується поки член ряду досить великий
            print(u) 
            n += 1
            if (x**(n) * 2**(2 * n + 1)) == 0: #перевірка щоб уникнути ділення на нуль
                break
            u = (math.factorial(2 + n)) / (x**(n) * 2**(2 * n + 1))
            s += u
        else:
            print ("Сума ряду: ",s) 
            return True
        print("Помилка!")
        return False