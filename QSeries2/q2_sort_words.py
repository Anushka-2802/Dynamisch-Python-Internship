#take a hyphen-separated sequence and using split(),sort()and join() method sort sequence 
#display sorted hyphen-separated sequence

def sort_sequence():
    sequence = input("Enter hyphen-separated sequence:")
    word_list = sequence.split("-")
    word_list.sort()
    sorted_sequence = "-".join(word_list)
    print(sorted_sequence)

sort_sequence()


