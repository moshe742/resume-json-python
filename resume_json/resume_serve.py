from pathlib import Path

import cherrypy

from resume_json.template_generator import TemplateGenerator


class ServeJson:
    """
    The class to work with cherrypy to serve the json
    """
    def __init__(self, json_path_and_name: Path, language: str = 'en', theme_dir: str = None):
        """
        The initiation of the data needed to serve the json as html
        :param json_path_and_name: the path to the json resume
        :param language: the language code of the resume
        """
        self.json_path_and_name = json_path_and_name
        self.template = TemplateGenerator(theme_dir)
        self.language = language

    @cherrypy.expose
    def index(self, theme: str = 'even') -> str:
        """
        The resume here is displayed with the theme selected

        If one want to use another theme one can add ?theme=<theme_name> to the url
        :param theme: the theme to use on the resume
        :return: the HTML as a string
        """
        html = self.template.create_html(self.json_path_and_name, theme, self.language)
        return html


class ResumeServe:
    def __init__(self):
        pass

    def serve(self, json_path: str, json_file: str, language: str = 'en', theme_dir: str = None) -> None:
        """
        Here I start the cherrypy to serve the resume json.

        :param json_path: the path to the json to be served
        :param json_file: the json file name including extension
        :param language: the language of the json file
        :param theme_dir: the path to theme directory to work with
        :return: None
        """
        json_path_and_name = Path(json_path, json_file)
        cherrypy.quickstart(ServeJson(json_path_and_name, language, theme_dir))
