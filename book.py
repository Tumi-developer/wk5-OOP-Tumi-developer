class Book:
    def __init__(self, title, author, isbn, price, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.pages = pages
        self.current_page = 0
    
    def read(self):
        """Simulates reading the book"""
        if self.current_page < self.pages:
            self.current_page += 1
            return f"Reading page {self.current_page} of {self.title}"
        return "You've finished the book!"
    
    def get_info(self):
        """Returns basic information about the book"""
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPrice: ${self.price}\nPages: {self.pages}"
    
    def bookmark(self, page):
        """Adds a bookmark to a specific page"""
        if 0 <= page <= self.pages:
            self.current_page = page
            return f"Bookmarked page {page}"
        return "Invalid page number"

class Ebook(Book):
    def __init__(self, title, author, isbn, price, pages, file_format, file_size):
        super().__init__(title, author, isbn, price, pages)
        self.file_format = file_format
        self.file_size = file_size
        self.battery_level = 100
    
    def read(self):
        """Overrides the read method to include battery consumption"""
        if self.battery_level > 0:
            self.battery_level -= 5
            return super().read() + f"\nBattery level: {self.battery_level}%"
        return "Low battery! Please charge your device."
    
    def charge(self):
        """Charges the ebook reader"""
        self.battery_level = 100
        return "Device fully charged!"
    
    def get_info(self):
        """Overrides get_info to include ebook-specific information"""
        return super().get_info() + f"\nFormat: {self.file_format}\nFile Size: {self.file_size}MB"

# Example usage
if __name__ == "__main__":
    # Create a regular book
    regular_book = Book("The Great Tumisang", "T. Bahumi Africa", "978-0743273565", 15.99, 180)
    print("Regular Book:")
    print(regular_book.get_info())
    print(regular_book.read())
    print(regular_book.bookmark(50))
    print(regular_book.read())
    print("\n" + "="*50 + "\n")
    
    # Create an ebook
    ebook = Ebook("The Great Tumisang", "T. Bahumi Africa", "978-0743273565", 9.99, 180, "PDF", 2.5)
    print("Ebook:")
    print(ebook.get_info())
    print(ebook.read())
    print(ebook.charge()) 