from setuptools import setup, find_packages

from resume_json import VERSION


def get_license():
    with open('LICENSE') as f:
        return f.read()


def get_long_description():
    with open('README.md') as fh:
        return fh.read()


LICENSE = get_license()

long_description = get_long_description()

setup(
    maintainer='Moshe Nahmias',
    maintainer_email='moshegrey@gmail.com',
    name='resume-json-cli',
    version=VERSION,
    packages=find_packages(),
    description='A project to work with resume json',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/moshe742/resume-json-python',
    include_package_data=True,
    python_requires='>=3.6',
    project_urls={
        'bug_tracker': 'https://github.com/moshe742/resume-json-python/issues',
        # 'documentation': '',
    },
    entry_points={
        'console_scripts': [
            'resume_cli=resume_json.resume_cli:main',
        ]
    },
    install_requires=['Jinja2', 'jsonschema', 'requests', 'WeasyPrint', 'cherrypy'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ]
)
