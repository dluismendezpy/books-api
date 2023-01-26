from datetime import datetime
from json import dumps

from http.server import BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

from constants.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from db.connection import DatabaseConnection
from settings import TEMPLATES_DIR
from utils.rest_data import RestBook


class BooksAPI(BaseHTTPRequestHandler):
    """
    Handle HTTP requests
    """

    def _send_response(self, data, status=HTTP_200_OK):
        """
        Send HTTP response to the client
        :param data: data to be sent in the response body
        :param int status: HTTP status code to be sent in the response headers
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        json_data = dumps(
            data,
            default=lambda x: x.strftime("%Y-%m-%d %H:%M")
            if isinstance(x, datetime)
            else x,
        )
        self.wfile.write(bytes(json_data, "utf8"))

    def _render_template(self, template_name, context, status=HTTP_200_OK):
        """
        Rendering HTML templates.
        :param str template_name: name of the template file to be rendered
        :param dict context: a dictionary containing the variables to be passed to the template for rendering.
        """
        env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        template = env.get_template(template_name)
        rendered_template = template.render(context)

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(rendered_template, "utf8"))

    def do_GET(self):
        """
        Handles the GET request sent to the server
        """
        if self.path.startswith("/api/books"):
            rest = RestBook()
            with DatabaseConnection() as db:
                if self.path == "/api/books":
                    books = db.get_books()
                    self._send_response(data=rest.rest_books(obj=books))
                else:
                    id = self.path.split("/")[-1]
                    if not id.isdigit():
                        self._send_response(
                            data={"error": "Invalid endpoint"},
                            status=HTTP_404_NOT_FOUND,
                        )
                    book = db.get_book(book_id=int(id))
                    if book:
                        self._send_response(data=rest.rest_book(book))
                    else:
                        self._send_response(
                            data={"error": "Book not found"},
                            status=HTTP_404_NOT_FOUND,
                        )
        elif self.path.startswith("/books"):
            rest = RestBook()
            with DatabaseConnection() as db:
                if self.path == "/books":
                    books = db.get_books()
                    self._render_template(
                        template_name="books.html",
                        context={"books": rest.rest_books(obj=books)},
                    )
                elif self.path.startswith("/books/"):
                    path_parts: list[str] = self.path.split("/")
                    if len(path_parts) != 3:
                        self._render_template(
                            template_name="not_found.html",
                            context={"error": "404. Invalid endpoint"},
                            status=HTTP_404_NOT_FOUND,
                        )
                    else:
                        id = self.path.split("/")[-1]
                        if not id.isdigit():
                            self._render_template(
                                template_name="not_found.html",
                                context={"error": "404. Invalid endpoint"},
                                status=HTTP_404_NOT_FOUND,
                            )
                        book = db.get_book(book_id=int(id))
                        if book:
                            self._render_template(
                                template_name="book.html",
                                context={"book": rest.rest_book(obj=book)},
                            )
                        else:
                            self._render_template(
                                template_name="not_found.html",
                                context={"error": "404. Book not found"},
                                status=HTTP_404_NOT_FOUND,
                            )
        else:
            self._send_response(
                data={"error": "Invalid endpoint"}, status=HTTP_404_NOT_FOUND
            )
