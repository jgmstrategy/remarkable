"""Manage the database files"""

import argparse

from remarkable.backend.server.app import db, flask_app


def create_db():
    db.create_all()


def reset_db():
    db.drop_all()
    create_db()


ACTION_CHOICES = {"reset": reset_db, "create": create_db}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="Database Manager",
        description="Manage the database files",
        epilog="Please run on the same server as the database",
    )
    parser.add_argument(
        "action",
        choices=list(ACTION_CHOICES),
        help="What action to take with this script",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    with flask_app.app_context():
        args = parse_arguments()
        ACTION_CHOICES[args.action]()
