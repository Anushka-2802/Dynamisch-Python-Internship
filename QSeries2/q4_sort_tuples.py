#sort list of tuple using lambda function in sort method
def sort_list():
        '''Sort list of tuples'''
        subject=[('English', 88),
        ('Science', 90),
        ('Maths', 97),
        ('Social sciences', 82)]
        print(subject)
        subject.sort(key=lambda x:x[1]) #sort list of tuple according to marks
        print("Sorted List of Tuple")
        print(subject)

sort_list()