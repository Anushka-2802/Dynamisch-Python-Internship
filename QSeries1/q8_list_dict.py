def map_list():
    '''Map two lists into dictionary'''
    list1=[1,2,3,4,5,6,7,8]
    list2=[1,4,9,16,25,36,49,64]
    result={}
    for i in range(len(list1)): 
        result[list1[i]]=list2[i] # create key value pair
    print(result)
map_list()

#using Zip() map two lists
list1=[1,2,3,4,5,6,7,8]
list2=[1,4,9,16,25,36,49,64]
new_dic=dict(zip(list1,list2))
print(new_dic)

