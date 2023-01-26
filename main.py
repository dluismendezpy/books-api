from http.server import HTTPServer

from db.connection import DatabaseConnection
from settings import SERVER_PORT
from views.BooksAPI import BooksAPI


def run(
    server_class=HTTPServer, book_class=BooksAPI, port: int = SERVER_PORT
) -> None:
    """
    Initializes the HTTP server
    :param server_class: class to use for the HTTP server
    :param book_class: class to use as the request handler
    :param int port: port number to run the server on
    """

    # Run migrations using alembic and seeder database with initial values
    with DatabaseConnection() as db:
        db.run_migrations()
        db.seed_books()

    server_address: tuple[str, int] = ("", port)
    http: HTTPServer = server_class(server_address, book_class)
    print(
        f"\nStarting development server at: http://localhost:{port}\nQuit the server with CONTROL-C"
    )
    http.serve_forever()


if __name__ == "__main__":
    run()
