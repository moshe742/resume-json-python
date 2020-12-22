#!/usr/bin/env python

import logging
import os
import sys

import click

from resume_json import basic_tui
from resume_json.resume_init import ResumeCreate
from resume_json.resume_validate import ResumeValidate
from resume_json.resume_export import ResumeExport
from resume_json.resume_serve import ResumeServe


logger = logging.getLogger(__name__)

logger_stdout = logging.getLogger('stdout')
logger_stdout.setLevel(logging.INFO)
std_out_handler = logging.StreamHandler(sys.stdout)
logger_stdout.addHandler(std_out_handler)


@click.group()
def resume_cli():
    # resume_json = ResumeJson()
    # if args.theme_dir:
    #     if not os.path.isdir(args.theme_dir):
    #         logger.error(f'Error: The theme directory {args.theme_dir} is not a directory...')
    #         sys.exit(1)
    #     elif len(os.listdir(args.theme_dir)) == 0:
    #         logger.warning(f'Warning: {args.theme_dir} theme directory is empty.')
    pass


@resume_cli.command('init')
@click.option('-d', '--directory', default=os.getcwd())
@click.option('-r', '--resume', 'file_name', default='resume.json')
def create(directory: str, file_name: str = 'resume.json') -> None:
    """
    Create the resume.json file.

    :param directory: the full path (not including the file name and extension) to the file
    :param file_name: the file name to be created
    :return: None
    """
    tui = basic_tui.BasicTui()
    resume_json = ResumeCreate(tui)
    resume_json.create(directory, file_name)

@resume_cli.command()
@click.option('-d', '--directory', default=os.getcwd())
@click.option('-r', '--resume', default='resume.json')
@click.option('--schema', default=None)
def validate(directory: str, resume: str, schema: str = None) -> None:
    """
    Validates the correctness of the file according to the schema.

    :param directory: the path to the file
    :param resume: the full path and file name to the file one want to validate
    :param schema: the schema to validate against, if not provided, will be taken from
    the resume.json file
    :return: string of the error in the file or None if the file is valid
    """
    file_validate = f'{directory}/{resume}'

    validate = ResumeValidate()
    result = validate.validate(file_validate, schema)
    if result is None:
        sys.exit(0)
    else:
        logger_stdout.info(f'Your resume-json is not valid!')
        logger_stdout.info(f'The path to the errors on the json is (there could be more):')
        logger_stdout.info(f'Error: {result}')
        sys.exit(1)

@resume_cli.command()
@click.option('-d', '--directory', 'file_path', default=os.getcwd())
@click.option('-r', '--resume', 'json_name', default='resume.json')
@click.option('-e', '--export', 'file_name', default='resume')
@click.option('-t', '--theme', default='even')
@click.option('-f', '--format', 'kind', default='html')
@click.option('-l', '--language', default='en')
@click.option('--theme-dir', default=None)
def export(file_path: str, json_name: str = 'resume', file_name: str = 'resume',
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

@resume_cli.command()
@click.option('-d', '--directory', 'json_file_path', default=os.getcwd())
@click.option('-r', '--resume', 'json_file', default='resume.json')
@click.option('-l', '--language', default='en')
@click.option('--theme-dir', default=None)
def serve(json_file_path: str, json_file: str, language: str = 'en', theme_dir: str = None) -> None:
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
    server = ResumeServe()
    server.serve(json_file_path, json_file, language, theme_dir)


def main():
    logging.basicConfig(format='%(message)s')
    resume_cli()


if __name__ == '__main__':
    main()
