#!/usr/bin/env python3
""" Basic Babel setup """

from sys import argv
app = __import__(f'{argv[1]}-app').app


if __name__ == "__main__":
    app.strict_slashes = False
    app.run(host="localhost", port=5000, debug=True)
