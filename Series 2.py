n = int(input("Enter the last numeber: "))

sum = 0
"""
for x in range(1,n+1,1):
    sum+=x
print(sum)
"""


for x in range(2,n+1,2):
    sum+=x*x
print(sum)
