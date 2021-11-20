# The rules are unclear as to whether the cursor number checks the sum of itself, its square, against the target value <k>...
# If the rule exists, as above, one method might be to skip the number in question when its idx in the list of numbers is the same as the count
# skip num if count is idx, don't change the list

list = [10, 12, 5, 13, 17]
k = 17

# ................

count = 0
count1 = 0 # validate num of checks is equal to the number of permutations

try:

    while count <= len(list)-1:
        num = list[count]
        for n in list:
            print(f"Checking if {num} + {n} == {k}...")
            sum = num + n
            if sum == k:
                print(f"{num} at idx ? is a match to k with {n}")
        count += 1

except Exception as e:
    print(f"{count = }, Error {e}")

finally:
    print("Good Job -- if it works...")

n = None


# ............

for n in list:
    for m in list:
        if n + m == 17:
            print(f"{n} + {m} match {k}")
