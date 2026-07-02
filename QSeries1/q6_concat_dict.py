# concatenate Dictionaries using update() method
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print("Concatenation of Dictionaries: ")
print(new_dic)


# using function)
def concate(dic1, dic2, dic3):
    """concate three dictionaries"""
    new_dic.update(dic1)
    new_dic.update(dic2)
    new_dic.update(dic3)
    print("Concatenation of Dictionaries: ")
    print(new_dic)

dic1 = {"Name": "Anushka", "Id": 63, "salary": 40000, "age": 21}
dic2 = {"location": "Phaltan", "Grade": 10}
dic3 = {"Mob_no": 8080579302}
concate(dic1, dic2, dic3)
