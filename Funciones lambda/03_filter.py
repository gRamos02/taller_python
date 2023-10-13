#Filter regresa los elementos que cumplan una condicion
nums = [2,3,4,5,6,7,8,9,10,11,12]

nums_2 = list(filter(lambda i:i%2==0,nums))
print(nums_2)


nums_3 = list(filter(lambda i:i%2==0,
                     list(map(lambda i:i*2, nums))))
print(nums_3)
