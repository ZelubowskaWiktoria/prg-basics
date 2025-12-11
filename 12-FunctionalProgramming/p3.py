arr = [3,4,5,6] # [6,8,10,12]

result = list(map(lambda x:x*2, arr))

result =  list(result)

print(result)


# to do this in one line:

arr = [3,4,5,6] # [6,8,10,12]

print(list(map(lambda x:x*2, arr)))