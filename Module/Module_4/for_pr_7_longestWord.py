fileName = "file_2.txt"
# Open the file in read-only mode. In this case, we're simply reading the contents of the file.
with open(fileName, 'r') as givenfilecontent:
    # Get all the words in a file using the read(), split() functions
    # Store it in a variable
    wrds = givenfilecontent.read().split()
# Calculate the maximum length of all words using the max(), len() functions
# by passing the above words list key= len as the arguments.
# Store it in another variable
max = len(max(wrds, key=len))
# Get all the words which are having the maximum length
# using the list comprehension and store it in another variable
rslt = [word for word in wrds if len(word) == max]
# Print the above result
print(*rslt)