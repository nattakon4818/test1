money = int(input("Enter number money withdraw : "))
print()  # มีหรือไม่มีก็ได้

b1000 = money // 1000
money %= 1000

b500 = money // 500
money %= 500

b100 = money // 100
money %= 100

if b1000 > 0:
    print(f"Cash B1000 : {b1000:.1f}")
if b500 > 0:
    print(f"Cash B500  : {b500:.1f}")
if b100 > 0:
    print(f"Cash B100  : {b100:.1f}")