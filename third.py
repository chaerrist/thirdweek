# my_set = set([5, 8, 3, 7, 1, "h"])
# print(my_set)

# set_tmp = set("hello")
# print(set_tmp)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

# print(my_set | set_item) 
print(my_set & set_item)

print(my_set)
my_set.remove(5)
print(my_set)