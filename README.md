# BookaPI

The Books API project is a web application that allows for interaction with a book database through a RESTful and Html
interface. It provides a set of routes that allow users to easily and quickly retrieve books and configure them.


<div align="center">

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-black?style=flat-square&logo=PostgreSQL)
![Linux](https://img.shields.io/badge/-Linux-black?style=flat-square&logo=Linux)
![macOS](https://img.shields.io/badge/-macOS-black?style=flat-square&logo=macOS)
![Windows](https://img.shields.io/badge/-Windows-black?style=flat-square&logo=Windows)
![.ENV](https://img.shields.io/badge/-.ENV-black?style=flat-square&logo=.ENV)
</div>

## Setup

- ### Clone repo

    ```shell
    git clone https://gitlab.com/luismendezdev/books-api.git
    ```

- ### Create and activate virtual environment

    - #### Linux, MacOS
       ```shell
      virtualenv venv
      source venv/bin/activate
      ```
    - #### Windows Powershell
       ```shell
      virtualenv venv
      venv\Scripts\activate.ps1
      ```

- ### Install dependencies

    - #### Windows Powershell
     ```shell
    pip install -r requirements_dev.txt
    ```

- ### Create a local database using postgresql

- ### Create .env file and your values for:

    ```shell
    POSTGRES_HOST=<YOUR_POSTGRES_HOST>
    POSTGRES_DB=<YOUR_POSTGRES_DB>
    POSTGRES_USER=<YOUR_POSTGRES_USER>
    POSTGRES_PASSWORD=<YOUR_POSTGRES_PASSWORD>
    POSTGRES_PORT=<YOUR_POSTGRES_PORT>
    SERVER_PORT=<YOUR_SERVER_PORT>
    ```

    - #### Also export:

        ```shell
        export POSTGRES_USER=<YOUR_POSTGRES_USER>
        export POSTGRES_PASSWORD=<YOUR_POSTGRES_PASSWORD>
        export POSTGRES_DB=<YOUR_POSTGRES_DB>
        export POSTGRES_PORT=<YOUR_POSTGRES_PORT>
        export SERVER_PORT=<YOUR_SERVER_PORT>
        ```

- ### Run server

    ```shell
    python main.py
    ```

## Docker way

- ### Add env values into .env and export variables

- ### Build and start docker

    ```shell
    docker-compose up --build
    ```

## Usage

- Api

| Description       | Endpoint             |
|-------------------|----------------------|
| Get list of books | /api/books           |
| Get a book        | /api/books/<book_id> |

- Html

| Description       | Endpoint         |
|-------------------|------------------|
| Get list of books | /books           |
| Get a book        | /books/<book_id> |

The URLs are validated. If you try to go to a non-existent route, (e.g. `/api/books/a-books` or `/books/hello`) it will
return a 404 error.
