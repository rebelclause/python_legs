# ................


# 18:55

import copy # or make a copy on the fly using a list comprehension
list = [1, 2, 3, 4, 5] # expected [120, 60, 40, 30, 24]

##tmp_list = copy.deepcopy(list)
tmp_list = []
tmp_list_1 = [x for x in list]

print(tmp_list)
print(tmp_list_1)

product: float = 1
products = []
count: int = 0

# ................

##product = [i * x for x in list for i in list] # if x != list[x]
print(f"{product} of length {len(products)}")

for ix, x in enumerate(list):
    tmp_list = [x for x in list]
    tmp_list[ix] = 1
    print(f"{tmp_list=}")
##    print(f"{ix=}")
    for iy, y in enumerate(list):

        if iy == ix:
            count += 1
            print(f"{count=}, {ix=}, {iy=}")
            # new list absent the value at iy == ix
            for i in tmp_list:
                product = product * i
    products.append(product)
    product = 1

print(f"{products=} of length {len(products)}")

##19:47 ten minute break

##20:12
