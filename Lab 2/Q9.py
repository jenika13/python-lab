#to find index of an item of a tuple

tuple_1 = ("apple","orange","mango","cherry","strawberry","grapes","banana","pineapple")

#to find index of an item of which value is passed
print(tuple_1.index("cherry"))

#finding index of an item starting from given index 
print(tuple_1.index("pineapple",4))

#finding index of an item between the given indices
print(tuple_1.index("strawberry",2,6))

#finding index of an item from user input
x = input("Enter an item of tuple : ")
print(tuple_1.index(x))