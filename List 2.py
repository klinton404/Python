subjects = ["c", "c++","java","python","css"]
print(len(subjects))
subjects.append("ios")     # adding
print(subjects)

subjects.insert(2,"os")
print(subjects)

subjects.remove("css")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()    # remove last element
print(subjects)

subject2 = subjects.copy()
print(subject2)

subjects.clear()
print(subject2)