#to remove an item from a set if it is present

my_set={1,3,5,7,9,'A','B','C','D'}
my_set.discard('B')      
print(my_set)
my_set.discard('F')      #returns the set unchanged if the element is not present
print(my_set)