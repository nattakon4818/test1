amount = float(input("Enter amount : "))
rate = float(input("Enter rate : ")) / 100
year = int(input("Enter year : "))

fv = amount * (1 + rate) ** year

print(f"Future value = {fv}")