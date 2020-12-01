#!/usr/bin/env python

import argparse
import os

from resume_json.json_resume import ResumeJson


def main():
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

    args = parser.parse_args()
    file_path = args.dir
    resume_json = ResumeJson()
    if args.init:
        resume_json.create(file_path, args.resume)
    elif args.validate:
        schema = args.schema
        result = resume_json.validate(args.validate, schema)
        if result is None:
            print(f'Your resume-json is valid!')
        else:
            print(f'Your resume-json is not valid!')
            print(f'The path to the errors on the json is (there could be more):')
            print(f'Error: {result}')
    elif args.export:
        resume_json.export(file_path, args.resume, args.export, args.theme, args.format, args.language)
    elif args.serve:
        resume_json.serve(file_path, args.resume, args.language)


if __name__ == '__main__':
    main()
