from datetime import datetime
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Name: Your Name")
        self.response.write("<br>") 
        self.response.write("Student ID: Your Student ID")
        self.response.write("<br>")
        self.response.write("Date and Time: " + str(datetime.now()))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)