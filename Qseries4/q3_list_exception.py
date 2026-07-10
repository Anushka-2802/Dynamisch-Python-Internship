def access_element():
   '''
   Accessing an element of a list using index.

   Raises:
    IndexError:
        If index is out of range.

    ValueError:
        If user enters invalid input.
    '''
   try:
        list1 = [12, 13, 24, 35, 46]
        index = int(input("Enter index: "))
        print("Element:", list1[index])

   except IndexError:
        print("Error: Index is out of range")

   except ValueError:
        print("Error: Please enter a valid integer")

access_element()