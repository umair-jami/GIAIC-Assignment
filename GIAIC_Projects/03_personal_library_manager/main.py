import json
import streamlit as st

class BookCollection:
    def __init__(self):
        self.storage_file = "books_data.json"
        self.book_list = self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def add_book(self, title, author, year, genre, read):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read,
        }
        self.book_list.append(new_book)
        self.save_to_file()

    def delete_book(self, title):
        self.book_list = [book for book in self.book_list if book["title"].lower() != title.lower()]
        self.save_to_file()

    def update_book(self, original_title, title, author, year, genre, read):
        for book in self.book_list:
            if book["title"].lower() == original_title.lower():
                book["title"] = title
                book["author"] = author
                book["year"] = year
                book["genre"] = genre
                book["read"] = read
                break
        self.save_to_file()

    def search_books(self, term):
        term = term.lower()
        return [book for book in self.book_list if term in book["title"].lower() or term in book["author"].lower()]

    def get_reading_stats(self):
        total = len(self.book_list)
        read = sum(book["read"] for book in self.book_list)
        return total, read, (read / total * 100) if total > 0 else 0


# Streamlit Interface
st.set_page_config(page_title="📚 Book Collection Manager", layout="centered")
st.title("📚 Book Collection Manager")

book_manager = BookCollection()

menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search", "Update", "Delete", "Reading Progress"])

if menu == "Add Book":
    st.header("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")
    if st.button("Add Book"):
        if title and author:
            book_manager.add_book(title, author, year, genre, read)
            st.success("Book added successfully!")
        else:
            st.warning("Please enter at least the title and author.")

elif menu == "View Books":
    st.header("📖 All Books")
    books = book_manager.book_list
    if books:
        for idx, book in enumerate(books, 1):
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.markdown(f"**{idx}. {book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
    else:
        st.info("No books in your collection yet.")

elif menu == "Search":
    st.header("🔍 Search Books")
    term = st.text_input("Search by Title or Author")
    if term:
        found = book_manager.search_books(term)
        if found:
            for book in found:
                status = "✅ Read" if book["read"] else "❌ Unread"
                st.markdown(f"- **{book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
        else:
            st.warning("No matching books found.")

elif menu == "Update":
    st.header("✏️ Update Book Details")
    titles = [book["title"] for book in book_manager.book_list]
    if titles:
        selected_title = st.selectbox("Select a book to update", titles)
        book = next((b for b in book_manager.book_list if b["title"] == selected_title), None)
        if book:
            title = st.text_input("New Title", value=book["title"])
            author = st.text_input("New Author", value=book["author"])
            year = st.text_input("New Year", value=book["year"])
            genre = st.text_input("New Genre", value=book["genre"])
            read = st.checkbox("Read", value=book["read"])
            if st.button("Update Book"):
                book_manager.update_book(selected_title, title, author, year, genre, read)
                st.success("Book updated successfully!")
    else:
        st.info("No books to update.")

elif menu == "Delete":
    st.header("🗑️ Delete a Book")
    titles = [book["title"] for book in book_manager.book_list]
    if titles:
        selected_title = st.selectbox("Select a book to delete", titles)
        if st.button("Delete Book"):
            book_manager.delete_book(selected_title)
            st.success("Book deleted successfully!")
    else:
        st.info("No books to delete.")

elif menu == "Reading Progress":
    st.header("📊 Reading Progress")
    total, read, percent = book_manager.get_reading_stats()
    st.write(f"Total Books: **{total}**")
    st.write(f"Books Read: **{read}**")
    st.progress(percent / 100)
    st.write(f"Reading Completion: **{percent:.2f}%**")
