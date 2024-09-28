import flames_functions

name1 = input("Enter the first name: \n")
name2 = input("Enter the second name: \n")

count = flames_functions.cancel_and_count(name1, name2)
relation = flames_functions.find_relation(count)
print(f'\n\nThe Relation Between {name1} and {name2} is {relation}')