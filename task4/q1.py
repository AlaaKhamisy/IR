my_dic = {1,  2 , 3}
print(my_dic)
def hash_key(k, m):
    return k % m
m = 7

print(f"The hash value for 3 is {hash_key(3,m)}")
print(f"The hash value for 2 is {hash_key(2,m)}")
print(f"The hash value for 1 is {hash_key(1,m)}")


