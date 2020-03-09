lucky_numbers = [42, 8, 15, 16, 23, 4]
friends =["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print (friends)
friends.extend(lucky_numbers)
print(friends)

friends =["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Rhythm")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.clear()
print(friends)

friends =["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

print(friends.index("Oscar"))

friends =["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)