nums = list(range(1,11))

for n in nums: print(n)

list_iter = iter(nums)

while True:
    try:
        print(next(list_iter))
    except StopIteration:
        break