#create new list of colours that contains l letter
colours=["red","pink","blue","yellow","purple"]
newlist=[x for x in colours if "l" in x]
print("New_colours list: ",end=" ")
print(newlist)

marks=[12,20,14,13,16,18,17]
new_marks=[y for y in marks if y > 13]
print("New_marks list: ",new_marks)
