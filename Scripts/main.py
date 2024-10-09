from database import DatabaseConnection
from library import Library
from reports import Reports
from menus import main_menu

def main():
    db_config = {
        'dbname': 'your_db_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432'
    }

    with DatabaseConnection(db_config) as db:
        library = Library(db)
        reports = Reports(db)
        main_menu(library, reports)

if __name__ == "__main__":
    main()
