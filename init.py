from application import app
from data import *

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()