import pr2
choice = int(input("Виберіть від 1 - 3 (0 - вихід): "))
while choice:
    if choice==1:
        pr2.task_if12()
    elif choice==2:
        pr2.task_geom_area20()
    elif choice==3:
        pr2.task_series22()
    else:
        print("Неправельний номер!")
    choice = int(input("Виберіть від 1 - 3 (0 - вихід): "))
print("До побачення!") 