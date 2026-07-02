def rotate():
    ''' Rotate list by right by k steps '''
    list=[1,2,3,4,5,6,7]
    k=3
    rotated_list=list[-k:]+list[:-k]
    print(rotated_list)
rotate()