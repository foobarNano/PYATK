nums = list(range(1,11))
list_iter = iter(nums)

while True:
    try:
        print(next(list_iter))
    except StopIteration:
        break