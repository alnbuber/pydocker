import numpy as np
import pandas as pd

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import json
from io import BytesIO
from urllib.parse import urlparse

def computeSomething():
        dates = pd.date_range(start='1992-12-01', end='2020-09-01', freq='M')
        df = pd.DataFrame(np.random.randn(dates.size, 4), index=dates, columns=list('ABCD'))

        # print(df)
        result = df.to_string()
        return result.encode(encoding='utf_8')

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        urlPath = urlparse(self.path).path
        print(urlparse(self.path))

        if urlPath == "/nada":
            self.wfile.write(
                b"Nothing should be done"
            )

        elif urlPath == "/test":

            urlQuery, urlParam = urlparse(self.path).query.split('=')

            if urlQuery == "num" and urlParam != None :
                self.wfile.write(
                    computeSomething()
                )

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()