from classes import *

s = Child() # 建立Child類別的物件

# 呼叫六個公開的方法，觀察執行結果
# 其中有二個方法會發生例外錯誤
print(s.get_super_public_var())
print(s.get_super_protected_var())
# print(s.get_super_private_var())
print(s.call_super_public_method())
print(s.call_super_protected_method())
# print(s.call_super_private_method())
