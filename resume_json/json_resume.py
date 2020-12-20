import json

import requests

from . import basic_tui
from .resume_init import ResumeCreate
from .resume_validate import ResumeValidate
from .resume_export import ResumeExport
from .resume_serve import serve_template


class ResumeJson:
    """
    The class that is responsible for all the functionality of this package

    With this class one can create the json.resume, validate it, export it to files of other
    types and watch it through a browser.
    """
    def __init__(self, ui=None):
        """
        Creating the object of ResumeJson

        Assuming ui as the terminal one can use the default implementation of this module
        but if one want to use their implementation or use some kind of other UI (for
        example graphical one) one can send their object while using the same API as
        basic_tui
        :param ui:
        """
        if ui is None:
            self.ui = basic_tui
        else:
            self.ui = ui

    def create(self, file_path: str, file_name: str = 'resume.json') -> None:
        """
        Create the resume.json file.

        :param file_path: the full path (not including the file name and extension) to the file
        :param file_name: the file name to be created
        :return: None
        """
        resume_json = ResumeCreate(self.ui)
        resume_json.create(file_path, file_name)

    def validate(self, file_to_validate: str, schema: str = None) -> str:
        """
        Validates the correctness of the file according to the schema.

        :param file_to_validate: the full path and file name to the file one want to validate
        :param schema: the schema to validate against, if not provided, will be taken from
        the resume.json file
        :return: string of the error in the file or None if the file is valid
        """
        with open(file_to_validate) as f:
            file_validate = json.load(f)

        if schema is None:
            schema_url = file_validate['$schema']
            res = requests.get(schema_url)
            schema = json.loads(res.text)
        validate = ResumeValidate()
        return validate.validate(file_validate, schema)

    def export(self, file_path: str, json_name: str = 'resume', file_name: str = 'resume',
               theme: str = 'even', kind: str = 'html', language: str = 'en', theme_dir: str = None) -> None:
        """
        Export the file to other formats

        This method exports the json to HTML by default, on the working directory assuming
        the file name to be resume.json, the theme to be `even` and the language to be English.
        One can change all those defaults by providing the relevant parameters.

        :param file_path: the file path where the json will be found, defaults to the working
        directory
        :param json_name: the name of the resume.json file one want to work on, defaults to resume
        :param file_name: the name of the exported file, defaults to resume
        :param theme: the theme one want the file to be in. can be one of ['even', 'cora', 'macchiato', 'short',
        'stackoverflow']
        :param kind: The type of file. Can be one of ['pdf', 'html'], defaults to html.
        :param language: The language of the file as a two letter code, defaults to en.
        :param theme_dir: the path to theme directory to work with
        :return: None
        """
        export = ResumeExport(theme_dir)

        if kind == 'html':
            export.export_html(file_path, json_name, file_name, theme, language)
        elif kind == 'pdf':
            export.export_pdf(file_path, json_name, file_name, theme, language)

    def serve(self, json_file_path: str, json_file: str, language: str = 'en', theme_dir: str = None) -> None:
        """
        Method to enable serving the file on localhost through the browser

        This method will create a cherrypy server on the local machine to serve the
        ones json resume and enable one to see their resume on the browser

        :param json_file_path: the path to the resume.json
        :param json_file: the name of the json resume file with extension
        :param language: the language two letter code to use while serving the html
        :param theme_dir: the path to theme directory to work with
        :return: None
        """
        serve_template(json_file_path, json_file, language, "even", theme_dir)
