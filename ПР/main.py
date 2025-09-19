import math

def task_integer4():
    try: #Перевірка на помилки
        A = int(input("A > B \nA = "))
        B = int(input("B = "))
        if A <= B :#Перевірка чи А більше В
            print("А повинна бути більше В")
            return
    except:#Повідомлення про помилку
        print("Числа повинні бути цілими")   
    else:#Якщо немає помилок
        result = A//B #Ділення без запису десятків
        print(result) 
        
def task2_32():
    try:
        x = float(input("x = "))
    except:
        print("Повинно бути число")
    else:
        try:
            numerator = math.sin(3 * x + math.pi) ** 3 + 2 ** (1 - x)
            denominator = math.tan(abs(x)) * math.sin(math.radians(18))
            addend1 = numerator / denominator
            addend2 = 1/3 * math.log2(abs(x))
            y = addend1 + addend2
        except:
            print("Помилка")
        else:
            print(y)
            
def task_boolean24():
    try:
        A = float(input("A ≠ 0 \nA = "))
        if A == 0:
            print("Помилка")        
            return
        B = float(input("B = "))
        C = float(input("C = "))        
    except:
        print("Повинно бути число")
    else:
        D = B ** 2 - 4 * A * C
        result = D >= 0
        print(result)
