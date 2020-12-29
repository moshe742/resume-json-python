# resume-json-python
This project is to be able to work with [json resume](https://jsonresume.org/),
As far as I can tell, all its features have been implemented here.
Please file bugs and feature requests as you find them or think of them :).

## installation and usage

### using docker
You can use docker to run this script for all its glory.

Once You can use docker run this command to build

    $ docker build -t image_name .
And then

    $ docker run -it image_name bash
You will be prompted with the command line from inside the docker and you can go from
here to usage and start using resume-cli.

### installing from pip
If you prefer to install it on your local machine just run the following command

    $ pip install resume-json-cli
### usage
I assume you use docker for the explanations below, adjust as needed if you
installed via pip.

If you just downloaded the repository you can use the functionality with
`python -m resume_json` from the root directory.

#### usage through docker
To use the command line tool you should use the option you want for
what you want to do.

For help use -h or --help as in

    $ ./resume-cli.py -h # or --help

### global options
One have two global options that come before the subcommands (init, validate, export
and save), those are the -r/--resume and -d/--dir options. So to use them you should
put right before the subcommand like so

    $ ./resume-cli.py -r your_file_name ...
    # or
    $ ./resume-cli.py -d /path/to/file
    # or
    $ ./resume-cli.py -d /path/to/file -r file_name

#### creating the resume.json
You can create the json with

    $ ./resume-cli.py init
It will prompt you with questions on all related fields you can put on the json
and at the end will create the json file to work with, the default json name is
resume.json that will appear on the working directory

If you want to change the default name you can use the -r or --resume and add the
file name you want for the file

    $ ./resume-cli.py -r <file_name> init

If you want to controll the directory to put the file you can use -d or --dir

    $ ./resume-cli.py -d <path/to_dir/> init
Of course, you can use it with or without -r/--resume

If you want to validate your resume.json you created you can do so with the
following command

#### validating the json
    $ ./resume-cli.py -d </path/to/resume/ -r <file_name> validate
It will validate with the schema in the url embedded in the resume file created.
If you want to validate with another schema you can do so by providing a schema flag
like so

    $ ./resume-cli.py -d </path/to/resume/ -r <file_name> validate --schema <relative/path/to/schema>
Just remember that the schema directory path is relative to your working directory

#### exporting the resume to html/pdf
You can export the resume after you are done with the json to html or pdf with the
export subcommand, it will default to html file and will create it on the working
directory

    $ ./resume-cli.py export
If you want it created on another directory you can use -d/--dir

    $ ./resume-cli.py -d </path/to/dir> export
To control the name of the exported file use -e or --file-name

    $ ./resume-cli.py export -e my_awesome_resume.json
To export the file to pdf you need to use the flag -f or --format like so

    $ ./resume-cli.py export -f pdf
It can have for now pdf or html as an argument.

The default theme is called even (the same as the one on the original project), if
you want to change it to one of the other themes you can do so with the flag -t or
--theme

    $ ./resume-cli.py export -t stackoverflow
The themes implemented here are: cora, even, macchiato, short and stackoverflow and
you should call them as written here.

You can use your own themes if you want, just use the flag `--theme-dir` to give the
system the path to your themes dir. Just remember to use your theme with the `-t`
flag

    $ ./resume-cli.py export -t my_awesome_theme --theme-dir /path/to/theme/dir # or relative path

#### serving the file from a web server localy
You can serve the json data from a web server localy to see how it looks like before
you export it to html (pdf will look a bit different, so I recommend to check it by
exporting to pdf and not by looking on the html version).

You can use the subcommand `serve` as shown here

    $ ./resume-cli.py -r </path/tojson/file/to/show> serve
Now you can see the result on your browser at the url http://localhost:8080/ and it
will show the default theme which is even.

If you want to see another theme you can do so by going to the same url and add the
query string ?theme=theme_name so to see the theme short for example you need to go to
http://localhost:8080/?theme=short

As mentioned above, you can use the --theme-dir to serve your own theme here too.
Just remember to append `?theme=your_theme_name` to the url

### language support
The default language attribute for all of the html is english, if you want to change
it you can do so with the -l or --language flag and the language code like so

    $ ./resume-cli.py ... -l he ... # for Hebrew