#List for Student Marks
Marks=[55,45,78,56,86,59,60,72,68,90,77,69]
#Slicing
print(Marks[:]) 
print(Marks[1:8])
print(Marks[1:-1]) # negative indexing
print(Marks[1:8:2]) # start end Jumping 
print(Marks[::8]) # starting and end element
print(Marks[1::])
Marks[5]=60

# Print Alternative number from list 
List=[1,2,3,4,5,6,7,8,9,10]
print(List)
print(List[1:10:2])

#check weather item present in list 
def colours(text):
        if char in text:
            print(char,"present in list at index",text.index(char))
        else:
            print("Not present")
char=str(input("Enter colour name you want to search:"))
text=["Yellow","Pink","Green","Red","Blue","Purple"]
colours(text)

#methods of list
def methods(fruit, num_list, num_tuple):
    print("Original List:")
    print(fruit)

    fruit.insert(0, "Apple")
    fruit.append("Mango")

    fruit.extend(num_list)
    fruit.extend(num_tuple)

    print("\nUpdated List:")
    print(fruit)

    num_list.remove(4)
    num_list.pop(1)
    print(num_list)

fruit = ["Papaya", "Banana", "Grapes", "Watermelon", "Kiwi"]
num_list = [1, 2, 3, 4]
num_tuple = (5, 6, 7)
methods(fruit, num_list, num_tuple)




