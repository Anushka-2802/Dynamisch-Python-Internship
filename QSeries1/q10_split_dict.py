def split_dic():
    ''' split a given dictionary of lists into lists of dictionaries'''
    
    data = {"Science": [88, 89, 62, 95], "Language": [77, 78, 84, 80]}
    New = []
    for i in range(len(data["Science"])):
        new_dic = {}
        new_dic["Science"] = data["Science"][i]
        new_dic["Language"] = data["Language"][i]
        New.append(new_dic)
    print(New)

split_dic()
