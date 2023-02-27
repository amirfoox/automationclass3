list1 = list(range(0, 100))
print(list1)

# print(all(list1))  # if all elements of the list are true
print(f"all = {all(list1)}, False because list1[0]={list1[0]}")
print(f"any = {all(list1)}")   # any of those are different

list1[0] = 100
print(f"all = {all(list1)}")

nums = [0, 2, 4, 12, 32, 99, 102]
# check if all the numbers are even in this list:
all_even = all(num % 2 == 0 for num in nums)  # the remainder is zero, meaning the number is even
any_odd = any(num % 2 for num in nums)
print(f"all_even = {all_even}")
print(f"at least one odd = {any_odd}")


