import logging
from datetime import datetime as dt
import json
import os
import typing
import sys

from jinja2 import Environment, PackageLoader, FileSystemLoader, ChoiceLoader, select_autoescape
from jinja2.exceptions import TemplateNotFound

logger = logging.getLogger(__name__)


class TemplateGenerator:
    """
    Class to create the HTML template
    """
    def __init__(self, theme_dir=None):
        loaders = [PackageLoader('resume_json', 'templates')]
        if theme_dir:
            loaders.insert(0, FileSystemLoader(theme_dir))

        self.env = Environment(
            loader=ChoiceLoader(loaders),
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
        """
        Filter to get the full date in the format %d %B %Y

        :param value: the date as written in the json, in the format %Y-%m-%d
        :return: the date in the format %d %B %Y
        """
        date_value = dt.strptime(value, '%Y-%m-%d')
        return date_value.strftime('%d %B %Y')

    def get_year_from_date(self, value: str) -> typing.Union[int, str]:
        """
        Filter to get the year from the date
        :param value: the date to get the year from in the format %Y-%m-%d
        :return: the year as an int or string
        """
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
        """
        Filter to format the date according to the theme selected

        :param value: the date in the format %Y-%m-%d
        :return: the date in the format of the theme
        """
        date_time_format = {
            'macchiato': '%m/%Y',
            'even': '%b %Y',
            'cora': '%b %Y',
            'stackoverflow': '%B %Y',
            'short': '%b %Y',
        }
        try:
            date_value = dt.strptime(value, '%Y-%m-%d')
            return date_value.strftime(date_time_format[self.theme] if self.theme in date_time_format else "%Y-%m-%d")
        except ValueError:
            pass
        except TypeError:
            return ''

        try:
            date_value = dt.strptime(value, '%Y-%m')
            return date_value.strftime(date_time_format[self.theme] if self.theme in date_time_format else "%Y-%m-%d")
        except ValueError:
            pass

        return value

    def create_html(self, file_path: str, file_name: str, theme_name: str,
                    language: str = 'en') -> str:
        """
        Creating the HTML according to the theme selected

        :param file_path: the path to the json file
        :param file_name: the name of the json file including extension
        :param theme_name: the name of the theme
        :param language: the language code of the json resume
        :return: the HTML as string
        """
        self.theme = theme_name
        try:
            template = self.env.get_template(f'{self.theme}.html')
        except TemplateNotFound:
            logger.warning(f'Warning: {self.theme} template was not found, using default theme even.')
            template = self.env.get_template('even.html')
        file_path_and_name = os.path.join(file_path, file_name)
        with open(file_path_and_name) as f:
            resume_dict = json.load(f)
        return template.render(resume=resume_dict, lang=language)
