import decimal as de   # 載入Decimal模組

# 顯示Decimal浮點數預設的準確位數
print('Decimal浮點數預設的準確位數(包含整數和小數):',
      de.getcontext().prec)

d1 = de.Decimal(
    '12345678901234567890.12345678901234567890')
d2 = de.Decimal('1E-20')
print(d1, '+', d2, '=')
print(d1 + d2)
print()

# 設定Decimal浮點數的準確位數
de.getcontext().prec = 50   # 設定50位小數準確
print('Decimal浮點數的準確位數(包含整數和小數):',
      de.getcontext().prec)
print(d1, '+', d2, '=')
print(d1 + d2)
print()

# Decimal浮點數和一般浮點數以及整數的運算
print('0.123', '+' , d1, '=')
print(0.123 + float(d1))   # 把Decimal浮點數轉成一般浮點數
print()
print('1', '+' , d1, '=')
print(1 + d1)    # Decimal浮點數和整數一起運算
