# my_list = []

# my_list = [ 'pink', 'orange', 'yellow', 'lilac', 'blue' ]

# print(len(my_list))

# print(my_list[0], my_list[2], my_list[-1])

# mixed_list = ["Charly", 30, 5.3, {"marital": "married"}, {"address": "London"} ]

# companies = ["Asda", "Sainsburys", "Waitrose", "Tesco", "Aldi", "Lidl"]

# print(companies)
# print(len(companies))

# len_co = len(companies)
# middle_co = int(len_co / 2)
# print(companies[0], companies[middle_co], companies[-1])

# companies[0] = "M&S"
# print(companies)
# companies.append("Asda")
# print(companies)
# companies.insert(2, "Iceland")
# print(companies)

# print(companies[1].upper())
# # print(' # ,'.join(companies))
# print(companies.index("Aldi"))

# sorted_list = sorted(companies)
# print(sorted_list)
# print(companies[::-1])
# print(companies[3:-1])
# print(companies[0:-3])

# companies.clear()
# del companies

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# extra = ["Python", "SQL"]
# back_end = ['Node','Express', 'MongoDB']
# front_end.extend(extra)
# front_end.extend(back_end)
# tech = front_end
# print(tech)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = sorted(ages)

min = ages[0]
max = ages[-1]
ages.append(min)
ages.append(max)
leng = int(len(ages))
leng_num = leng
middle = int(leng / 2)
mid_num = int(middle)
median = ages[mid_num]
average = sum(ages)/leng_num
print('Median: ', median)
print('Average: ', average)
print('Range: ', max - min)
min_av = abs(min - average)
max_av = abs(max - average)
print('Compare: ', abs(min_av - max_av))