# Question 1: Managing Book Titles Using Lists
# Creating the initial list of books
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Initial list of books:", books)

# Adding two new books to the collection
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")
print("After adding new arrivals:", books)

# Removing a book that got damaged
books.remove("Moby Dick")
print("After removing the damaged book:", books)

# Sorting the books alphabetically for easier searching
books.sort()
print("Final sorted book catalog:", books)

# Question 2: Storing Borrower Details Using Tuples
# Creating a tuple with borrower personal details
borrower = ("John Doe", "B1023", "2025-10-15")

# Displaying tuple length using len()
print("Total number of data fields:", len(borrower))
# Iterating through the tuple elements using a loop
print("Borrower Profile Details:")
for field in borrower:
    print(f"- {field}")

# Attempting to modify a tuple element to observe behavior
try:
    borrower[1] = "B9999"
except TypeError as error:
    print("\nObservation on modification attempt:", error)
    
# Question 3: Tuple Packing and Unpacking
# Tuple Packing: bundling title, author, and year
book_info = ("The Alchemist", "Paulo Coelho", 1988)

# Tuple Unpacking: extracting values into distinct variables
title, author, year = book_info

# Displaying unpacked variables in a formatted structure
print(f"Title: {title}")
print(f"Author: {author}")
print(f"Publication Year: {year}")

# Question 4: Slicing and Indexing Weekly Statistics
# Weekly borrowing stats from Week 1 to Week 7
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original borrowing statistics:", borrowed_books)
# Extracting Week 2 to Week 5 records using slicing [start:stop]
week2_to_week5 = borrowed_books[1:5]

# Updating Week 1 count to 20 using zero-based indexing
borrowed_books[0] = 20

# Displaying updated records
print("Updated borrowing statistics:", borrowed_books)
print("Extracted records (Week 2 to Week 5):", week2_to_week5)