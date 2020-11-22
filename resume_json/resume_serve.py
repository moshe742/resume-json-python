import cherrypy
import json
import os

from resume_json.template_generator import TemplateGenerator


class ServeJson:
    def __init__(self, json_path, json_file):
        self.json_path = json_path
        self.json_file = json_file
        self.template = TemplateGenerator()
        super().__init__()

    @cherrypy.expose
    def index(self, theme='even'):
        html = self.template.create_html(self.json_path, self.json_file, theme)
        return html


class ResumeServe:
    def __init__(self):
        pass

    def serve(self, json_path, json_file):
        cherrypy.quickstart(ServeJson(json_path, json_file))
