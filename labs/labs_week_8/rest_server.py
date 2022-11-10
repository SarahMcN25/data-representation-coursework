# LABS 08 - This prog creates an application server that will implement a RESTful API. 

from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Creating a dummy array to test function on. 
books=[
        {"id":1, "Title":"Harry Potter", "Author": "JK Rowling", "Price":10000 },
        {"id":2, "Title":"Lord of the Rings", "Author": "J. R. R. Tolkien", "Price":56 },
        {"id":3, "Title":"The Gruffelo", "Author": "Julia Donaldson", "Price":26 }
]

# Var to be used later. 
nextId=4 


# TEST
@app.route('/')
def index():
    return "hello"


# GET ALL BOOKS 
# curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    #return "served by Get All()" #debug

    return jsonify(books)


# FIND BOOK BY ID 
#curl http://127.0.0.1:5000/books/2
@app.route('/books/<int:id>')
def findById(id):
    #return "served by find by id with id " + str(id) # debug

    # Lambda searches through array of books and only return back specific id.
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    # If length is 0 return empty json and error. 
    if len(foundBooks) == 0:
        return jsonify({}), 204

    return jsonify(foundBooks[0])


# CREATE A BOOK
# curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    #return "served by create()" # debug

    global nextId

    # If it's not a json request return error. 
    if not request.json:
        abort(400)

    book = {
        "id":nextId, 
        "Title": request.json["Title"], 
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    # Append to books, up an id and return the json book. 
    books.append(book)
    nextId += 1
    return jsonify(book)


# UPDATE A BOOK
#  curl -X PUT -H "content-type:application/json" -d "{\"Title\":\"new title\", \"Author\":\"different author\", \"Price\":60}"  http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    #return "served by update with id " + str(id) #debug

    # Lamda search. 
    foundBooks = list(filter (lambda t : t["id"]== id, books))

    if len(foundBooks) == 0:
        return jsonify({}), 404

    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']

    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
            
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)


# DELETE A BOOK
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    #return "served by delete with id " + str(id) #debug

    # Lambda search.
    foundBooks = list(filter (lambda t : t["id"]== id, books))

    if len(foundBooks) == 0:
        return jsonify({}), 404

    books.remove(foundBooks[0])

    return jsonify({"done":True})


# CALL MAIN FUNCTION
if __name__ == "__main__":
    app.run(debug=True)