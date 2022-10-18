# This prog pulls/pushes info from API 

import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

# Lab 4.3 - Gets all books from API
def get_all_books():
    response = requests.get(url)
    return response.json()

# Lab 4.4 - Get single book info from API
def get_book_by_id(id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    return response.json()

# Lab 4.5 - Creating a book to push to API
def create_book(book):
    # A way of doing it simply as issue between dict and json
    response = requests.post(url, json=book)

    # Another way of doing above line - making headers and seperating data out. 
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    
    return response.json()

# Lab 4.6 - Updating a books info
def update_book(id, book_diff):
    update_url = url + "/" + str(id)
    response = requests.put(update_url, json=book_diff)
    return response.json()

# Lab 4.7 - Deleting a book from API
def delete_book(id):
    delete_url = url + "/" + str(id)
    response = requests.delete(delete_url)
    return response.json()
   
# Lab 4.8 - Calling main method to test all functions
if __name__ == "__main__":
    book= {
        'Author':"test",
        'Title':"test title",
        "Price": 123789
    }
    book_diff= {
        "Price": 123
    }
    #print(get_all_books())
    #print(get_book_by_id(1))
    #print (delete_book(109))
    #print (create_book(book))
    #print (update_book(1, book_diff))