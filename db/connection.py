import psycopg2
from decouple import config as env
from typing import List, Tuple

from alembic import command, config

from .seed_data import books


class DatabaseConnection:
    """
    Establish connection and interact with PostgreSQL database
    """

    def __init__(self):
        self.connection = psycopg2.connect(
            host=env("POSTGRES_HOST", default="localhost"),
            database=env("POSTGRES_DB"),
            user=env("POSTGRES_USER", default="postgres"),
            password=env("POSTGRES_PASSWORD"),
            port=env("POSTGRES_PORT", default=5432, cast=int),
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) UNIQUE NOT NULL,
                author VARCHAR(255) NOT NULL,
                content TEXT NOT NULL,
                pages INTEGER NOT NULL,
                created_at TIMESTAMP NOT NULL,
                last_updated TIMESTAMP NOT NULL
            );
            """
        )
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def seed_books(self, data=books) -> None:
        """
        Inserts initial data into books table.
        :param Book data: data to populate book table
        """
        row: list[str] = [
            "title",
            "author",
            "content",
            "pages",
            "created_at",
            "last_updated",
        ]
        for book in data:
            self.cursor.execute(
                """
                INSERT INTO books (title, author, content, pages, created_at, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (title) DO NOTHING
                """,
                ([book[key] for key in row]),
            )
            self.connection.commit()

    def run_migrations(self) -> None:
        """
        This method uses Alembic to run migrations on the database.
        """
        alembic_cfg = config.Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

    def get_book(self, book_id: int) -> Tuple | None:
        """
        Get a specific book
        :param book_id: argument used to get a book
        :return: the data of the book with that id
        """
        self.cursor.execute(
            "SELECT id, title, author, content, pages, created_at, last_updated FROM books WHERE id = %s",
            (book_id,),
        )
        return self.cursor.fetchone()

    def get_books(self) -> List:
        """
        Get all books from db
        :return: all data from the books table
        """
        self.cursor.execute(
            "SELECT id, title, author, content, pages, created_at, last_updated FROM books"
        )
        return self.cursor.fetchall()
