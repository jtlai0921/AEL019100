import decimal as dec

dec.getcontext().prec = 100
d1 = dec.Decimal('2')
d2 = dec.Decimal('0.5')

ans = d1 ** d2
print('2開根號的結果', ans)
