# If file does not exist 'w' will create a new file.
# If this file already exists it will be overwritten.
with open('createdfiles/doc1.txt', 'w') as file:
          file.write("This is a document created via python!")

with open('createdfiles/doc2.txt', 'w') as file:
          file.write("This is another document created via python!")