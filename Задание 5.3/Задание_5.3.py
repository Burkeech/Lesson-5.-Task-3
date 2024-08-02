x = int(input("Минимальная сумма инвестиций - ")) 
mike = int(input("Майкл - "))
ivan = int(input("Иван - "))
if (mike >= x) and (ivan >= x):
    print(2)
elif  (mike >= x) and (ivan <= x):   
    print("Mike")
elif  (mike <= x) and (ivan >= x):   
    print("Ivan")
elif  (mike + ivan) >= x:   
    print(1)
elif  (mike <= x) and (ivan <= x):   
    print(0)