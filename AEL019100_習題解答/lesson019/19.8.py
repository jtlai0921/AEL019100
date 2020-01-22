import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = set(random.sample(letters, 10))
t = set(random.sample(letters, 10))
u = set(random.sample(letters, 10))

interset_s_t = s & t
interset_s_u = s & u
interset_t_u = t & u
interset_s_t_u = s & t & u
union_s_t_u = s | t | u

print('沒有被挑到的字母：', set(letters) - union_s_t_u)
print('被挑到一次的字母：', union_s_t_u - interset_s_t - interset_s_u - interset_t_u)
print('被挑到二次的字母：', (interset_s_t | interset_s_u | interset_t_u) - interset_s_t_u)
print('被挑到三次的字母：', interset_s_t_u)
