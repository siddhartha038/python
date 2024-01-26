marks = [45,25,65]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])

if 45 in marks:
    print("Yes it is in the list")
else:
    print("No its not present in the list")
    
print(marks[0:2:2])
#The above line is the concept of the jump indexing

lst=[ i for i in range(5) if i%2==0]
print(lst)
    