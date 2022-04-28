names = "acharf,mohaMmid,chaMso, aNes "
name_list = names.split(',')
print(name_list)
print('-----------------------------------')
name_one = name_list[0]
name_two = name_list[1]
name_three = name_list[2]
name_four = name_list[3]
print(name_one)
print(name_two)
print(name_three)
print(name_four)
print('-----------------------------------')

name_one = name_one.title()
name_two = name_two.lower().capitalize().replace('i', 'e')
name_three = name_three.lower().capitalize()
name_four = name_four.strip().lower().capitalize().replace('e', 'i')

print(name_one)
print(name_two)
print(name_three)
print(name_four)