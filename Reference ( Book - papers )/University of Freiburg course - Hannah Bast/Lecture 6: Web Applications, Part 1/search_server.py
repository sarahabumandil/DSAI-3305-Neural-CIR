"""
Copyright 2019, University of Freiburg,
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>
Natalie Prange <prange@cs.uni-freiburg.de>
"""

import socket
import sys


class SearchServer:
    """
    A HTTP search server using a q gram index.

    No pre-defined tests are required this time. However, if you add new
    non-trivial methods, you should of course write tests for them.

    Your server should behave like explained in the lecture. For a given
    URL of the form http://<host>:<port>/search.html?q=<query>, your server
    should return a (static) HTML page that displays (1) an input field and a
    search button as shown in the lecture, (2) the query without any URL
    encoding characters and (3) the top-5 entities returned by your q-gram
    index (from exercise sheet 5) for the query.

    In the following, you will find some example URLs, each given with the
    expected query (%QUERY%) and the expected entities (%RESULT%, each in the
    format "<name>;<score>;<description>") that should be displayed by the
    HTML page returned by your server when calling the URL. Note that, as
    usual, the contents of the test cases is important, but not the exact
    syntax. In particular, there is no HTML markup given, as the layout of
    the HTML pages and the presentation of the entities is up to you. Please
    make sure that the HTML page displays at least the given query and the
    names, scores and descriptions of the given entities in the given order
    (descending sorted by scores).

     URL:
      http://<host>:<port>/search.html?q=angel
     RESPONSE:
      %QUERY%:
        angel
      %RESULT%:
       ["Angela Merkel;205;chancellor of Germany from 2005 to 2021",
        "Angelina Jolie;158;American actress (born 1975)",
        "angel;140;supernatural being or spirit in certain religions and\
                mythologies",
        "Angel Falls;90;waterfall in Venezuela; highest uninterrupted \
                waterfall in the world",
        "Angela Davis;70;American political activist, scholar, and author"
       ]

     URL:
      http://<host>:<port>/search.html?q=eyjaffjala
     RESPONSE:
      %QUERY%:
        eyjaffjala
      %RESULT%:
       ["Eyjafjallajökull;76;ice cap in Iceland covering the caldera of a \
                volcano",
        "Eyjafjallajökull;8;2013 film by Alexandre Coffre"
       ]

     URL:
      http://<host>:<port>/search.html?q=The+hitschheiker+guide
     RESPONSE:
      %QUERY%:
       The hitschheiker guide
      %RESULT%:
       ["The Hitchhiker's Guide to the Galaxy pentalogy;44;1979-1992 series\
                of five books by Douglas Adams",
        "The Hitchhiker's Guide to the Galaxy;43;1979 book by Douglas Adams",
        "The Hitchhiker's Guide to the Galaxy;36;2005 film directed by Garth \
                Jennings",
        "The Hitchhiker's Guide to the Galaxy;8;BBC television series",
        "The Hitchhiker's Guide to the Galaxy;7;1984 interactive fiction video\
                game"
       ]
    """

    def __init__(self, port: int):
        """
        Initialize with given port.
        """
        self.port = port

    def run(self):
        """
        Run the server loop: create a socket, and then, in an infinite loop,
        wait for requests and do something with them.
        """
        # Create server socket using IPv4 addresses and TCP.
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow reuse of port if we start program again after a crash.
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Say on which machine and port we want to listen for connections.
        server_address = ("0.0.0.0", self.port)
        server_socket.bind(server_address)
        # Start listening
        server_socket.listen()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    server = SearchServer(port)
    server.run()


if __name__ == "__main__":
    main()
