#print dictionary where value is square of the key 
def dic_square():
    square_dic={i:i*i for i in range(1,16)} #dictionary comprehension
    print(square_dic)
dic_square()

#without comprehension
square_dic={}
for i in range(1,16):
    square_dic[i]=i*i
print(square_dic)
