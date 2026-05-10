"""
Copyright 2022, University of Freiburg
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Claudius Korzen <korzen@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>
Natalie Prange <prange@cs.uni-freiburg.de>
"""

import sys


class SearchServer:
    """
    Your server should behave like explained in the lecture and ES7. For a
    given URL of the form http://<host>:<port>/api?q=<query>, your server
    should return the matches for <query> as a valid JSON object.

    The web application should be dynamic, by using JavaScript and the jQuery
    library. The URL of the search page should be
    http://<host>:<port>/search.html, just like for ES6. The matches should now
    be displayed automatically after each keystroke (so that an explicit search
    button is no longer necessary), and they should be obtained via your own
    API described above. As for ES6, you should display up to 5 matches.
    """

    def __init__(self, port: int):
        """
        Initializes a simple HTTP search server
        """
        self.port = port

    def run(self):
        """
        Start the webserver and handle requests.

        In the following, you will find some example URLs, each given with the
        expected JSON output. Note that, as usual, the contents of the test cases
        is important, but not the exact syntax.

        URL:
          http://<host>:<port>/api?q=angel
        RESPONSE:
          {
            "query": "angel",
            "results": [
              {
                "name": "Angela Merkel",
                "score": 206,
                "description": "chancellor of Germany from 2005 to 2021"
              },
              {
                "name": "Angelina Jolie",
                "score": 159,
                "description": "American actress (born 1975)"
              },
              {
                "name": "angel",
                "score": 140,
                "description": "supernatural being or spirit in certain religions and mythologies"
              },
              {
                "name": "Angel Falls",
                "score": 90,
                "description": "waterfall in Venezuela; highest uninterrupted waterfall in the world"
              },
              {
                "name": "Angela Davis",
                "score": 70,
                "description": "American political activist, scholar, and author"
              }
            ]
          }

        URL:
          http://<host>:<port>/api?q=eyj%C3%A4fja
        RESPONSE:
          {
            "query": "eyjäfja",
            "results": [
              {
                "name": "Eyjafjallajökull",
                "score": 76,
                "description": "ice cap in Iceland covering the caldera of a volcano"
              },
              {
                "name": "Eyjafjarðarsveit",
                "score": 20,
                "description": "municipality of Iceland"
              },
              {
                "name": "Eyjafjallajökull",
                "score": 8,
                "description": "2013 film by Alexandre Coffre"
              }
            ]
          }

        URL:
          http://<host>:<port>/api?q=%C3%B6ster
        RESPONSE:
          {
            "query": "öster",
            "results": [
              {
                "name": "Östersund",
                "score": 81,
                "description": "urban area in Östersund Municipality, Sweden"
              },
              {
                "name": "Östergötland County",
                "score": 69,
                "description": "county (län) in Sweden"
              },
              {
                "name": "Östergötland",
                "score": 49,
                "description": "historical province in Sweden"
              },
              {
                "name": "Östersunds FK",
                "score": 42,
                "description": "association football club in Östersund, Sweden"
              },
              {
                "name": "Österreichischer Rundfunk",
                "score": 39,
                "description": "Austrian public broadcaster"
              }
            ]
          }
        """
        # TODO: add your code
        # pass

    def url_decode(self, string: str):
        """
        Decode an URL-encoded UTF-8 string, as explained in the lecture.
        Don't forget to also decode a "+" (plus sign) to a space (" ")!

        >>> s = SearchServer(0, None)
        >>> s.url_decode("nirwana")
        'nirwana'
        >>> s.url_decode("the+m%C3%A4trix")
        'the mätrix'
        >>> s.url_decode("Mikr%C3%B6soft+Windos")
        'Mikrösoft Windos'
        >>> s.url_decode("The+hitschheiker%20guide")
        'The hitschheiker guide'
        """
        # TODO: add your code
        # pass


def main():
    """
    Parse the command line arguments, build the Qgram Index and start the
    server.
    """
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <file> <port> "
              " [--use-synonyms] [--party-pooper]")
        sys.exit()

    file_name = sys.argv[1]
    port = int(sys.argv[2])
    use_synonyms = "--use-synonyms" in sys.argv
    party_pooper = "--party-pooper" in sys.argv

    s = SearchServer(port)
    s.run()


if __name__ == "__main__":
    main()
