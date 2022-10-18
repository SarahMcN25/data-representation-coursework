# This prog analyses info from API and returns the average count of books

from lab_functions_file import get_all_books

books = get_all_books()
total = 0
count = 0
for book in books:
    # print(books) # debug
    total += book["Price"]
    count += 1

print ("average of ", count, "books is ", total/count )