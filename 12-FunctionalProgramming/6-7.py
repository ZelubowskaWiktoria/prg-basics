scores = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]


print(list(map(lambda scores: sum(sorted(scores)[1:-1]), scores)))


# or another way to do this with  max()  and min()


arr = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]


print(list(map(lambda x: sum(x) - min(x) - max(x), arr)))