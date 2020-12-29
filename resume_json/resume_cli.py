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
@click.option('-r', '--resume', 'resume_file_name', default='resume.json')
@click.option('-d', '--dir', 'directory', default=os.getcwd())
@click.pass_context
def resume_cli(ctx, resume_file_name, directory):
    ctx.ensure_object(dict)
    ctx.obj['resume_file_name'] = resume_file_name
    ctx.obj['directory'] = directory


@resume_cli.command('init')
@click.pass_context
def create(ctx: click.core.Context) -> None:
    """
    Create the resume.json file.

    :param ctx: the Context object from click to pass the parent command parameters
    :return: None
    """
    tui = basic_tui.BasicTui()
    resume_json = ResumeCreate(tui)
    resume_json.create(ctx.obj['directory'], ctx.obj['resume_file_name'])


@resume_cli.command()
@click.option('--schema', default=None)
@click.pass_context
def validate(ctx: click.core.Context, schema: str = None) -> None:
    """
    Validates the correctness of the file according to the schema.

    :param ctx: the Context object from click to pass the parent command parameters
    :param schema: the schema to validate against, if not provided, will be taken from
    the resume.json file
    :return: string of the error in the file or None if the file is valid
    """
    file_validate = f'{ctx.obj["directory"]}/{ctx.obj["resume_file_name"]}'

    resume_validate = ResumeValidate()
    result = resume_validate.validate(file_validate, schema)
    if result is None:
        sys.exit(0)
    else:
        logger_stdout.info(f'Your resume-json is not valid!')
        logger_stdout.info(f'The path to the errors on the json is (there could be more):')
        logger_stdout.info(f'Error: {result}')
        sys.exit(1)


@resume_cli.command()
@click.option('-e', '--file-name', 'file_name', default='resume')
@click.option('-t', '--theme', default='even')
@click.option('-f', '--format', 'kind', default='html')
@click.option('-l', '--language', default='en')
@click.option('--theme-dir', default=None)
@click.option('--export-dir', 'export_dir', default=os.getcwd())
@click.pass_context
def export(ctx: click.core.Context, file_name: str = 'resume', theme: str = 'even', kind: str = 'html', language: str = 'en',
           theme_dir: str = None, export_dir: str = None) -> None:
    """
    Export the file to other formats

    This method exports the json to HTML by default, on the working directory assuming
    the file name to be resume.json, the theme to be `even` and the language to be English.
    One can change all those defaults by providing the relevant parameters.

    :param ctx: the Context object from click to pass the parent command parameters
    :param file_name: the name of the exported file, defaults to resume
    :param theme: the theme one want the file to be in. can be one of ['even', 'cora', 'macchiato', 'short',
    'stackoverflow']
    :param kind: The type of file. Can be one of ['pdf', 'html'], defaults to html.
    :param language: The language of the file as a two letter code, defaults to en.
    :param theme_dir: the path to theme directory to work with
    :param export_dir: the directory to create the exported file at
    :return: None
    """
    resume_export = ResumeExport(theme_dir)

    if kind == 'html':
        resume_export.export_html(ctx.obj['directory'], ctx.obj['resume_file_name'], export_dir, file_name, theme, language)
    elif kind == 'pdf':
        resume_export.export_pdf(ctx.obj['directory'], ctx.obj['resume_file_name'], export_dir, file_name, theme, language)


@resume_cli.command()
@click.option('-l', '--language', default='en')
@click.option('--theme-dir', default=None)
@click.pass_context
def serve(ctx: click.core.Context, language: str = 'en', theme_dir: str = None) -> None:
    """
    Method to enable serving the file on localhost through the browser

    This method will create a cherrypy server on the local machine to serve the
    ones json resume and enable one to see their resume on the browser

    :param ctx: the Context object from click to pass the parent command parameters
    :param language: the language two letter code to use while serving the html
    :param theme_dir: the path to theme directory to work with
    :return: None
    """
    server = ResumeServe()
    server.serve(ctx.obj['directory'], ctx.obj['resume_file_name'], language, theme_dir)


def main():
    logging.basicConfig(format='%(message)s')
    resume_cli()


if __name__ == '__main__':
    main()
