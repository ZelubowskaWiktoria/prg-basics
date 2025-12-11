arr = [4,2,17,21,3,5,1,19]

result = []
for item in arr:
    if item > 4:
        result.append(item)

print(result)

# or we can use this instead:

arr = [4,2,17,21,3,5,1,19]

print(list(filter(lambda x:x>4, arr)))
