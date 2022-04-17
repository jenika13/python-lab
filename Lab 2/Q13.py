#to generate all sublist of a list

#function to generate all sublists
def sublist():
    list1=[[]]
    for i in range(len(my_list)+1):
        for j in range(i+1,len(my_list)+1):
            sub=my_list[i:j]
            list1.append(sub)
    return list1

#to input a list and print the sublists
my_list=[]
n=int(input("Enter number of elements in the list : "))
print("The elements are : ")
for i in range(n):
    ele=int(input(""))
    my_list.append(ele)
print("The sublists of list {} are {}".format(my_list,sublist()))