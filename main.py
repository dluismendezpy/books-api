from db.connection import DatabaseConnection


def run() -> None:
    with DatabaseConnection() as db:
        db.run_migrations()
        db.seed_books()


if __name__ == "__main__":
    run()
