import json

import requests

from . import basic_tui
from .resume_init import ResumeCreate
from .resume_validate import ResumeValidate
from .resume_export import ResumeExport
from .resume_serve import ResumeServe


class ResumeJson:
    def __init__(self, ui=None):
        if ui is None:
            self.ui = basic_tui

    def create(self, file_path: str, file_name: str = 'resume.json') -> None:
        resume_json = ResumeCreate(self.ui)
        resume_json.create(file_path, file_name)

    def validate(self, file_to_validate: str, schema: str = None) -> str:
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
        export = ResumeExport(theme_dir)

        if kind == 'html':
            export.export_html(file_path, json_name, file_name, theme, language)
        elif kind == 'pdf':
            export.export_pdf(file_path, json_name, file_name, theme, language)

    def serve(self, json_file_path: str, json_file: str, language: str = 'en') -> None:
        server = ResumeServe()
        server.serve(json_file_path, json_file, language)
