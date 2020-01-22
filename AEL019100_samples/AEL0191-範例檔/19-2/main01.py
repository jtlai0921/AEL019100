d1 = {'id':5, 'name':'john', 'age':18, 8:'a number', (1, 2):100}
d2 = {}   # 建立空的dict資料組

# 利用dict()內建函式建立dict資料組，請留意參數的格式
d3 = dict(id=5, name='john', age=18)

print(d1['id'])
print(d1[8])
print(d1[(1, 2)])
print(d3['name'])
print(d3['age'])
