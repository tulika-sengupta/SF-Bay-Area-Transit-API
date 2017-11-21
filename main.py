import webapp2
from TransitAPI import findAgency


class Home(webapp2.RequestHandler):
    """A GET Request Handler"""
    def get(self):
        """Receives a GET request"""
        self.response.write('Hello, DevelopHerDevelopHim Viewers!')


class Slack511(webapp2.RequestHandler):
    """A POST Request Handler"""

    def post(self):
        """Receives a POST request"""
        stopCode = self.request.get('text')
        findAgency(stopCode, self)


app = webapp2.WSGIApplication([
                        (r'/', Home),
                        (r'/slack511', Slack511)
                        ],
                        debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()