
import pytest
from ansible.utils.helpers import object_to_dict

class InvalidType:
    pass


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def test_basic_usage():
    person = Person("Alice", 30, "Wonderland")
    result = object_to_dict(person)
    assert result == {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

def test_excluding_attributes():
    person = Person("Alice", 30, "Wonderland")
    result = object_to_dict(person, exclude=["city"])
    assert result == {'name': 'Alice', 'age': 30}

class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

def test_custom_object():
    book = Book("1984", "George Orwell", 1949)
    result = object_to_dict(book)
    assert result == {'title': '1984', 'author': 'George Orwell', 'published_year': 1949}

def test_excluding_specific_attribute():
    book = Book("1984", "George Orwell", 1949)
    result = object_to_dict(book, exclude=["published_year"])
    assert result == {'title': '1984', 'author': 'George Orwell'}