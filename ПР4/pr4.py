import math
import matplotlib.pyplot as plt

class Point_19:

    @property
    def x(self): #геттер для х
        return self.__x

    @x.setter
    def x(self, val): #сеттер для х з перевіркою діапазону
        try:
            if -100 <= val <= 100:
                self.__x = val
            else:
                self.__x = 0
        except ValueError:
            self.__x = 0
            
    @property
    def y(self): #геттер для у
        return self.__y

    @y.setter
    def y(self, val): #сеттер для у з перевіркою діапазону
        try:
            if -100 <= val <= 100:
                self.__y = val
            else:
                self.__y = 0
        except ValueError:
            self.__y = 0
            
    amount_point = 0
    
    @classmethod
    def get_amount_point(cls): #метод який визначає кількість точок
        print("Кількість точок:", cls.amount_point)
        
    def __init__(self, x=0, y=0): #конструктор класу
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y
        Point_19.amount_point += 1
        
    def __del__(self): #деструктор класу
        Point_19.amount_point -= 1
        
    def move(self, dx, dy): #переміщення точки
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __str__(self):
        return f"Point_19(x={self.x}, y={self.y})"
        
def main():         
    point1 = Point_19(68.65, -40.4) #створення трьох точок
    point2 = Point_19(-35.44, -66.38)
    point3 = Point_19(-46.52, 61.45)
    Point_19.get_amount_point()

    dist = math.dist((point1.x, point1.y), (point2.x, point2.y)) #обчислення відстані між першою та другою точками
    print("Відстань між першою та другою точками:", dist)
    
    points = [point1, point2, point3] #збереження списку точок
    start_coords = [(p.x, p.y) for p in points] #початкові координати
    point3.move(-23, -12) #переміщення точки
    print("Нові координати третьої точки:", point3)
    final_coords = [(p.x, p.y) for p in points] #зінцеві координати

    x_start = [c[0] for c in start_coords] #розділення координат на окремі списки для зручності побудови графіка
    y_start = [c[1] for c in start_coords]
    x_final = [c[0] for c in final_coords]
    y_final = [c[1] for c in final_coords]

    plt.subplot(2, 1, 1) #побудова першого графіка
    plt.plot(x_start, y_start, 'bo')
    for i, (x, y) in enumerate(start_coords):
        plt.text(x + 1, y + 1, f'P{i+1}')
    plt.title('До переміщення')
    plt.grid(True)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)

    plt.subplot(2, 1, 2) #побудова другого графіка
    plt.plot(x_final, y_final, 'ro')
    for i, (x, y) in enumerate(final_coords):
        plt.text(x + 1, y + 1, f'P{i+1}')
    plt.title('Після переміщення P3')
    plt.grid(True)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.tight_layout() 

    my_file = open ( "coord.txt", 'w') #запис координат в текстовому файли
    for i,p in enumerate(points):
        my_file.write ( f"{i+1}: {p.x}; {p.y}\n")
    my_file.close ()
    
if __name__ == "__main__":
    main()