#!/usr/bin/env python

import argparse
import logging
import os
import sys

from .json_resume import ResumeJson

logger = logging.getLogger(__name__)

logger_stdout = logging.getLogger('stdout')
logger_stdout.setLevel(logging.INFO)
std_out_handler = logging.StreamHandler(sys.stdout)
logger_stdout.addHandler(std_out_handler)


def parsing_arguments() -> argparse.Namespace:
    """
    This function is to parse the arguments coming from cmd.

    :return: argparse.Namespace object with all the arguments from the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version')
    parser.add_argument('-t', '--theme', metavar='theme name', type=str,
                        default='even')
    # file type extension, used by `export`
    parser.add_argument('-f', '--format', metavar='file type extension', type=str,
                        default='html')
    parser.add_argument('-r', '--resume', metavar='resume filename', type=str,
                        default='resume.json')
    parser.add_argument('-p', '--port', metavar='port', type=str)
    parser.add_argument('-s', '--silent', metavar='True/False', type=bool, default=False)
    parser.add_argument('-d', '--dir', metavar='path', default=os.getcwd())
    parser.add_argument('--schema', metavar='relative/path')
    parser.add_argument('--init', action='store_true')
    parser.add_argument('-v', '--validate', metavar='file/to/validate')
    parser.add_argument('-e', '--export', metavar='file name')
    parser.add_argument('-S', '--serve', action='store_true')
    parser.add_argument('-l', '--language', metavar='language code', default='en')
    parser.add_argument('--theme-dir', metavar="path")

    return parser.parse_args()


def resume_cli():
    args = parsing_arguments()
    file_path = args.dir
    resume_json = ResumeJson()
    if args.theme_dir:
        if not os.path.isdir(args.theme_dir):
            logger.error(f'Error: The theme directory {args.theme_dir} is not a directory...')
            sys.exit(1)
        elif len(os.listdir(args.theme_dir)) == 0:
            logger.warning(f'Warning: {args.theme_dir} theme directory is empty.')

    if args.init:
        resume_json.create(file_path, args.resume)
    elif args.validate:
        schema = args.schema
        result = resume_json.validate(args.validate, schema)
        if result is None:
            sys.exit(0)
        else:
            # TODO: should be stdout
            logger_stdout.info(f'Your resume-json is not valid!')
            logger_stdout.info(f'The path to the errors on the json is (there could be more):')
            logger_stdout.info(f'Error: {result}')
            sys.exit(1)
    elif args.export:
        resume_json.export(file_path, args.resume, args.export, args.theme, args.format, args.language, args.theme_dir)
    elif args.serve:
        resume_json.serve(file_path, args.resume, args.language, args.theme_dir)
    else:
        # TODO: print help message
        pass


def main():
    logging.basicConfig(format='%(message)s')
    resume_cli()


if __name__ == '__main__':
    main()
