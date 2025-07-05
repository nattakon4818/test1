VAT = 7      

net_price = int(input("Enter net price product : "))

price = net_price / (1 + VAT / 100)
vat   = net_price - price

# แสดงผลลัพธ์ด้วย f‑string
print(f"Price product : {price:.1f}")
print(f"Vat product : {vat:.1f}")