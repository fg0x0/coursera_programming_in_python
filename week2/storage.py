import os
import tempfile
import argparse
import json


def load_db(file):
    """Load database from file"""
    # Create database file if not exists
    if not os.path.isfile(file):
        with open(file, "w") as f:
            json.dump(dict(), f)
        return dict()

    with open(file, "r") as f:
        return json.load(f)


def save_db(file, db):
    """Save database to file"""
    with open(file, "w") as f:
        json.dump(db, f)


def main():
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()

    # Temporary file for database
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    db = load_db(storage_path)

    # Get value by key
    if not args.val:
        if args.key in db:
            print(", ".join(db[args.key]))
        else:
            print("")
    # Add value to key
    else:
        if args.key in db:
            db[args.key].append(args.val)
        else:
            db[args.key] = [args.val]

    save_db(storage_path, db)


if __name__ == '__main__':
    main()
