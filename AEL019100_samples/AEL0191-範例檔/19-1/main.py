import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = set(random.sample(letters, 10))
t = set(random.sample(letters, 10))

print('沒有被挑到的字母：', set(letters) - (s | t))
print('被挑到一次的字母：', s ^ t)
print('被挑到二次的字母：', s & t)
