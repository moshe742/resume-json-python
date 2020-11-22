from setuptools import setup, find_packages


setup(
    maintainer='moshe nahmias',
    maintainer_email='moshegrey@gmail.com',
    name='resume-cli-python',
    version='0.1.0',
    packages=find_packages(),
    description='',
    long_description='',
    long_description_content_type='text/markdown',
    url='',
    license='',
    include_package_data=True,
    python_requires='>=3.6',
    # project_urls={'bug_tracker': '', 'documentation': ''}
    entry_points={
        'console_scripts': [
            'resume-cli=resume_json.resume_cli:main',
        ]
    }
)
