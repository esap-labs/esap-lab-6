from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from shutil import copyfile
import cgi
import cv2

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _serve_ui(self):
        global cell_count
        self.wfile.write("<html><body>")
        # TODO: Display cell count on top of the image
	self.wfile.write("<form method='POST'><input type='image' src='image.png'/>")
        self.wfile.write("</form></html>")

    def do_GET(self):
        self._set_headers()

        if self.path == "/image.png" :
            # TODO: serve image

        else :
            # anything except image.png is our html UI
            self._serve_ui();

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        x = int(postvars['x'][0])
        y = int(postvars['y'][0])
        print ("x " , x , " y " , y)

        # TODO: increment a cell_count variable
        
        image = cv2.imread('image.png')

        # TODO: draw 'X' in red at coordinades x,y
 
        cv2.imwrite('image.png',image)

        self._set_headers()
        self._serve_ui();

        
def run(server_class=HTTPServer, handler_class=S, port=8000):

    #global cell_count 
    #cell_count = 0

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

