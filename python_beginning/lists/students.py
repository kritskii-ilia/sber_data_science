from audioop import reverse


students = []
students += ['Ivan', 'Petr', 'Sergey']
students += ['Egor']
students += 'Olga'
print(students)

if 'Sasha' not in students:
    print('Sasha not in students')

del students[2]
print(students)

sorted_students = sorted(students)
print(sorted_students)

students.sort()
print(students)

print(max(students))
print(min(students))


print(list(reversed(students)))

students.reverse()
print(students)

print(students[::-1])


in_dex = students.index('Petr')
print(in_dex)


a = [1, 2, 3]
b = a
# значения списка b? такое же, как и a

a[1] = 10
# значения списка b? [1, 10, 3]

b[0] = 20
# значения списка a? [20, 10, 3]

a = [5, 6]
# значения списка b? Такое же, тк а присвоили новое значение, b = [20, 10, 3]
print(b)
print(a)
