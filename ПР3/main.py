import pr3
choice = int(input("Виберіть від 1 - 2 (0 - вихід): "))
while choice:
    if choice==1:
        pr3.Proc10()
    elif choice==2:
        pr3.Matrix2()
    else:
        print("Неправельний номер!")
    choice = int(input("Виберіть від 1 - 2 (0 - вихід): "))
print("До побачення!") 