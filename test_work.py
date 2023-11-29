list = ['Hello', '2', 'world', ':-)']
new_list = []
for i in range(len(list)):
    if len(list[i]) <= 3:
        new_list.append(list[i])