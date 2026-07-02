def add_key():
    dic1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    dic2 = {"a": 2, "b": 4, "e": 5, "f": 9}
    new_dic = {}
    for key, values in dic1.items():
        if key in dic2:
            new_dic[key] = values + dic2[key]
        else:
            new_dic[key] = values
    # for remaining keys
    for key, values in dic2.items():
        if key not in new_dic:
            new_dic[key] = values
    print(new_dic)

add_key()

# counter class import from collections
# counter supports arithmetic operations(+,-)
from collections import Counter

d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
d2 = {"a": 2, "b": 4, "e": 5, "f": 9}
new_d = Counter(d1) + Counter(d2)
print(new_d)
