a = 'Саша тут'
b = a.split(' ')
b.reverse()
d = '!' + ' ! '.join(b) + '!'
print(d)

a = 'Саша тут'.split()
print(f'!{a[1]} ! {a[0]}!')

a = 'Саша тут'
lst_a = a.split()
rev = '!' + a.replace(lst_a[1], lst_a[0]).replace(lst_a[0], lst_a[1], 1) + '!'
rev2 = rev.replace(' ', ' ! ')
print(rev2)
