#using filter and lambda find out intersection
def intersection():
    '''Print common element from both list'''
    list1=[1, 2, 3, 5, 7, 8, 9, 10]
    list2=[1, 2, 4, 8, 9]
    result=list(filter(lambda x: x in list2,list1))
    print(result)
intersection()
