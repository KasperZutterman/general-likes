from sqlite_utils import Database
import sqlite3
from datetime import date
import sys

db = Database(sqlite3.connect("./general-likes.db"))

likes = db["general_likes"]
likes.insert({
    "id": sys.argv[1],
    "liked_url": sys.argv[2],
    "liked_date": sys.argv[3],
}, pk="id")

print(sys.argv[1], sys.argv[2], sys.argv[3])