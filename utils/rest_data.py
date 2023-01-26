from typing import Dict, List

from entities.book import Book


class RestBook:
    """
    Convert a book object or list into a format that can be easily
    serialized and returned in a Rest API response.
    """

    def rest_books(self, obj: List[Book]) -> List[Dict]:
        """
        Transforms a list of book objects into a list of dictionaries
        :param List[Book] obj: list of book objects to be transformed
        :return: list of dictionaries representing the book objects
        """
        books = [
            {
                "id": id,
                "title": title,
                "author": author,
                "content": content,
                "pages": pages,
                "created_at": created_at,
                "last_updated": last_updated,
            }
            for id, title, author, content, pages, created_at, last_updated in obj
        ]

        return books

    def rest_book(self, obj: Book) -> Dict:
        """
        Transforms a book object into a dictionary.
        :param Book obj: a book object to be transformed.
        :return Dict: dictionary representing the book object.
        """
        id, title, author, content, pages, created_at, last_updated = obj
        book = {
            "id": id,
            "title": title,
            "author": author,
            "content": content,
            "pages": pages,
            "created_at": created_at,
            "last_updated": last_updated,
        }

        return book
