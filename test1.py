a, b = input('Nhập vào giá trị a và b của phương trình ax + b = 0: ').split()
a = int(a); b = int(b)

while True:
    if (a == 0) and (b != 0):
        print('Phuong trinh vo nghiem.')
        break
    elif (a ==0) and (b == 0):
        print('Phuong trinh co vo so nghiem.')
        break
    else:
        print('Nghiem cua phuong trinh la ', round(-b/a,2))
        break