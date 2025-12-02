# NoSQL

## Learning Objectives
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements
### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) and PyMongo (version 4.8.0)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- Your code should not be executed when imported (by using if __name__ == "__main__":)

## Tasks
0. Write a script that lists all databases in MongoDB.
1. Write a script that creates or uses the database my_db
2. Write a script that inserts a document in the collection school
3. Write a script that lists all documents in the collection school
4. Write a script that lists all documents with name="Holberton school" in the collection school
5. Write a script that displays the number of documents in the collection school
6. Write a script that adds a new attribute to a document in the collection school
7. Write a script that deletes all documents with name="Holberton school" in the collection school
8. Write a Python function that lists all documents in a collection
9. Write a Python function that inserts a new document in a collection based on kwargs
10. Write a Python function that changes all topics of a school document based on the name
11. Write a Python function that returns the list of school having a specific topic
12. Write a Python script that provides some stats about Nginx logs stored in MongoDB