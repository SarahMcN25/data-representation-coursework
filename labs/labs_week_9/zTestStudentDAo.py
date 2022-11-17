# This prog uses zClassStudentDAO to make changes on a DB using sql commands in a python script.
# Based on week 9 labs

from zClassStudentDAO import studentDAO

#create
latestid = studentDAO.create(('mark', 45))

# find by id
result = studentDAO.findByID(latestid)
print ("test create and find by id")
print (result)

#update
studentDAO.update(('Fred',21,latestid))
result = studentDAO.findByID(latestid)
print("test update")
print (result)

# get all 
print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

# delete
studentDAO.delete(latestid)