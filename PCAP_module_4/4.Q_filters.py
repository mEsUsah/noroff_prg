numbers = (1,2,5,9.15)

def filter_numbers(num):
    nums = (1,5,17)
    if num in nums:
        return True
    else:
        return False

filtered_numbers = filter(filter_numbers, numbers)
for n in filtered_numbers:
    print(n)