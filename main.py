
file_name= "Python_Lesson.PY"
file_upper= file_name.upper()
file_lower = file_name.lower()
starts_with_python = file_name.startswith("Python")
ends_with_py = file_name.endswith("PY")
file_extension = file_name[-2:]
print(file_extension)  # Виведе "PY"
book = {"title": "Python Basics", "author": "Alex Smith", "year": 2024}

book_year = book.pop("year")
book_pages = book.get("pages")

print(book_year)  # 2024
print(book_pages)  # 0
print(book)  # словарь уже без ключа "year"
cat = {
    "nick": "Whiskers",
    "age": 3,
    "characteristics": ["игривый", "ласковый"]
}

cat_age = cat.get("age")
cat_name = cat.get("nick")

cat.update({"color": "серый", "is_active": True})

print(cat_name)
print(cat_age)
print(cat)