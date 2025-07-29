book = []
book.append("learn c")
book.append("learn c++")
book.append("learn java")
book.append("learn python")
print(book)

book.pop()
print("Now the top book is: ",book[-1] )    #First in last out
book.pop()
print("Now the top book is: ",book[-1] )
book.pop()
print("Now the top book is: ",book[-1] )
book.pop()
if not book:
    print("No book left")