nums = input('Podaj liczby: ')
nlist = nums.split(',')

for n in nlist:
    nmin = n
    break
nmax = nmin

for n in nlist:
    if (n < nmin): nmin = n
    if (n > nmax): nmax = n

print('MIN: ', nmin)
print('MAX: ', nmax)
