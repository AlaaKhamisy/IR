value_list = [3,2,9,11,7]
for k in value_list:
    for m in len(value_list):
        hash_value = k % m
choice= int(input("Enter your choosen number:"))
if choice == 1:    
   print("key \t\t\t Hash Value")
   print(k,"\t\t",hash_value)
elif choice == 2:
    value_list.append()
elif choice == 3:
    value_list.update(k) 
elif choice == 4:
    value_list.remove()
elif choice == 5:
    value_list.search(hash_value)           