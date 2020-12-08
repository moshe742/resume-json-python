from datetime import datetime as dt
import json
import os
import typing

from jinja2 import Environment, PackageLoader, select_autoescape


class TemplateGenerator:
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader('resume_json', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.theme_name = {
            'even': 'even',
            'cora': 'cora',
            'macchiato': 'macchiato',
            'stackoverflow': 'stackoverflow',
            'short': 'short',
            'mine': 'mine',
        }
        self.theme = None
        self.env.filters['datetime_format'] = self.datetime_format
        self.env.filters['get_year'] = self.get_year_from_date
        self.env.filters['get_full_date'] = self.get_full_date

    def get_full_date(self, value: str) -> str:
        date_value = dt.strptime(value, '%Y-%m-%d')
        return date_value.strftime('%d %B %Y')

    def get_year_from_date(self, value: str) -> typing.Union[int, str]:
        try:
            date_value = dt.strptime(value, '%Y-%m-%d')
            return date_value.year
        except ValueError:
            pass

        try:
            date_value = dt.strptime(value, '%Y-%m')
            return date_value.year
        except ValueError:
            pass
        return value

    def datetime_format(self, value: str) -> str:
        date_time_format = {
            'macchiato': '%m/%Y',
            'even': '%b %Y',
            'cora': '%b %Y',
            'stackoverflow': '%B %Y',
            'short': '%b %Y',
        }
        try:
            date_value = dt.strptime(value, '%Y-%m-%d')
            return date_value.strftime(date_time_format[self.theme])
        except ValueError:
            pass
        except TypeError:
            return ''

        try:
            date_value = dt.strptime(value, '%Y-%m')
            return date_value.strftime(date_time_format[self.theme])
        except ValueError:
            pass

        return value

    def create_html(self, file_path: str, file_name: str, theme_name: str,
                    language: str = 'en') -> str:
        self.theme = self.theme_name[theme_name]
        template = self.env.get_template(f'{self.theme}.html')
        file_path_and_name = os.path.join(file_path, file_name)
        with open(file_path_and_name) as f:
            resume_dict = json.load(f)
        return template.render(resume=resume_dict, lang=language)
