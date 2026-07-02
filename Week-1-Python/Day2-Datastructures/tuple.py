def display(data):
    print("\nTuple Elements:")

    for i in data:
        print(i, end=" ")

def access_elements(data):

    print("First Element:", data[0])
    print("Last Element:", data[-1])

def count_element(data):

    num = int(input("\nEnter number to count: "))
    print(num, "appears", data.count(num), "times")

def search_element(data):

    num = int(input("\nEnter element to search: "))
    if num in data:
        print(num, "found at index", data.index(num))
    else:
        print("Element not found")

def slicing(data):

    print("\nTuple Slicing:")
    print(data[1:5])


def unpacking(data):

    a, b, c, d, e = data[:5]
    print("\nTuple Unpacking:")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


# Main Tuple
data = (10, 20, 30, 40, 50, 20, 60)
display(data)
access_elements(data)
count_element(data)
search_element(data)
slicing(data)
unpacking(data)