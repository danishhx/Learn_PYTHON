dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
lst = [dict1, dict2]
result = {}
for dct in lst:
    for key,value in dct.items():
        result[key] = value
print(result)