def calculate_structure_sum(data_structure):
    sum=0
    a=''
    for i in data_structure:
        a += str(i)
    b=''
    for i in range(len(a)):
        if a[i].isnumeric() == True or a[i].isalpha() == True:
            b += str(a[i])
        else:
            b+=','
    a=b.split(",")

    for i in range(len(a)):
        if a[i].isnumeric():
            sum+=int(a[i])
        elif a[i].isalpha():
            sum+=len(a[i])
        else:
            sum += len(a[i])
    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

