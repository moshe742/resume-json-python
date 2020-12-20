from http.server import BaseHTTPRequestHandler, HTTPServer

from resume_json.template_generator import TemplateGenerator


class JsonResumeHandler(BaseHTTPRequestHandler):
    """ Handler class for the rendered HTML.
    
    Serve GET HTTP requests with the rendered HTML as bytes.
    """
    def do_GET(self):
        """  """
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(str.encode(self.server.html))

class JsonResumeServer(HTTPServer):
    """ Server class for the HTML render.
    
    Add a new attributes html to the class, which is passed down to the handler.

    :param server_address: a `server_address https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.server_address`_
    :param handler: a `RequestHandlerClass https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.RequestHandlerClass`_
    :param html: the rendered HTML from the TemplateGenerator
    """
    def __init__(self, server_address, handler, html):
        super().__init__(server_address, handler)
        self.html = html


def serve_template(json_path, json_file, language, theme_name, theme_dir):
    """ Serves the template, forever 

    :param json_path: the path to the json to be served
    :param json_file: the json file name including extension
    :param language: the language of the json file
    :param theme_name: the theme name used for the template generator
    :param theme_dir: the user-defined theme directory
    """
    template = TemplateGenerator(theme_dir)
    html = template.create_html(json_path, json_file, theme_name, language)
    server = JsonResumeServer(('localhost', 8080), JsonResumeHandler, html)
    server.serve_forever()

