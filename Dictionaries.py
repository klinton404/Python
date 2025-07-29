studentID = {
    "101" : "Klinton",
    "102" : "Suvash",
    "103" : "Shimul",
}

print(studentID["101"])
print(studentID.get("102"))
print(studentID.get("106"))
print(studentID.get("103", "Not a valid key"))
print(studentID.get("106", "Not a valid key"))