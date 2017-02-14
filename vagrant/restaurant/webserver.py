from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

## import CRUD operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurant"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Many Places to Eat</h1>"
                output += "<a href=/restaurant/new>New Restaurant</a><br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "<br><a href=/%s/edit>edit</a>" % restaurant.id
                    output += "<br><a href=/%s/delete>delete</a><br>" % restaurant.id
                    output += "<br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurant/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>New Restaurant</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'><input name="new" type="text" ><input type="submit" value="Create"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantId = self.path.split("/")[1]
                restaurant = session.query(Restaurant).filter(Restaurant.id == restaurantId).one()
                restaurantName = restaurant.name
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Edit Restaurant</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/%s/edit'><input value='%s' name="edit" type="text" ><input type="submit" value="Rename"> </form>''' % (restaurantId, restaurantName)
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/delete"):
                restaurantId = self.path.split("/")[1]
                restaurant = session.query(Restaurant).filter(Restaurant.id == restaurantId).one()
                restaurantName = restaurant.name
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h3>Are you sure you want to delete %s ?</h3>" % restaurantName
                output += '''<form method='POST' enctype='multipart/form-data' action='/%s/delete'><input type="submit" value="Delete"> </form>''' % restaurantId
                output += "</body></html>"
                self.wfile.write(output)
                return


            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                output = ""
                output += "<html><body>"
                output += " <h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output

            if self.path.endswith("/restaurant/new"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    newrestaurant = fields.get('new')
                    addrestaurant = Restaurant(name = newrestaurant[0])
                    session.add(addrestaurant)
                    session.commit()

            if self.path.endswith("/edit"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    newRestaurantName = fields.get('edit')

                restaurantId = self.path.split("/")[1]
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                restaurant.name = newRestaurantName[0]
                session.add(restaurant)
                session.commit()

            if self.path.endswith("/delete"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                restaurantId = self.path.split("/")[1]
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                session.delete(restaurant)
                session.commit()

        except:
            pass


def main():
    try:
        port = 8081
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()