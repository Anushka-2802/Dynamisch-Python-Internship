def write_file():
    '''
    Write a list a list to a files
    '''
    with open('myfile.txt','w') as file:
        list1=["Apple", "Mango", "Banana", "Orange"]
        for items in list1:
            file.write(items +"\n")
    print("File updated successfully")
write_file()