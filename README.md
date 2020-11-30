# resume-json-python
This project is to be able to work with [json resume](https://jsonresume.org/),
I implemented here all their features as far as I know, so please file bugs and
feature requests.

## installation and usage

### using docker
You can use docker to run this script for all it's glory.

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

To use the command line tool you should use the option you want for
what you want to do.

For help use -h or --help as in

    $ ./resume-cli.py -h # or --help

#### creating the resume.json
You can create the json with

    $ ./resume-cli.py --init
It will prompt you with questions on all related fields you can put on the json
and at the end will create the json file to work with, the default json name is
resume.json that will appear on the working directory

If you want to change the default name you can use the -r or --resume and add the
file name you want for the file

    $ ./resume-cli.py --init -r <file_name>

If you want to controll the directory to put the file you can use -d or --dir

    $ ./resume-cli.py --init -d <path/to_dir/>
Of course you can use it with or without -r

If you want to validate your resume.json you created you can do so with the
following command

#### validating the json
    $ ./resume-cli.py --validate <path/to/file/file_name>
It will validate with the schema in the url embedded in the resume file created.
If you want to validate with another schema you can do so by providing a schema flag
like so

    $ ./resume-cli.py --validate <path/to/file/file_name> --schema <relative/path/to/schema>
Just remember that the schema directory path is relative to your working directory

#### exporting the resume to html/pdf
You can export the resume after you are done with the json to html or pdf with the
-e or --export flag, it will default to html file and will create it on the working
directory

    $ ./resume-cli.py -e <file_name>
If you want it created on another directory you can use -d/--dir

    $ ./resume-cli.py -e <file_name> -d </path/to/dir>
To export the file to pdf you need to use the flag -f or --format like so

    $ ./resume-cli.py -e <file_name> -f pdf
It can have for now pdf or html as an argument.

The default theme is called even (the same as the one on the original project), if
you want to change it to one of the other themes you can do so with the flag -t or
--theme

    $ ./resume-cli.py -e <file_name> -t stackoverflow
The themes implemented here are: cora, even, macchiato, short and stackoverflow and
you should call them as written here.

#### serving the file from a web server localy
You can serve the json data from a web server localy to see how it looks like before
you export it to html (pdf will look a bit different, so I recommend to check it by
exporting to pdf and not by looking on the html version).

You can use the flags -S or --serve as shown here

    $ ./resume-cli.py -S -r </path/tojson/file/to/show>
Now you can see the result on your browser at the url http://localhost:8080/ and it
will show the default theme which is even.

If you want to see another theme you can do so by going to the same url and add the
query string ?theme=theme_name so to see the theme short for exampe you need to go to
http://localhost:8080/?theme=short

### language support
The default language attribute for all of the html is english, if you want to change
it you can do so with the -l or --language flag and the language code like so

    $ ./resume-cli.py -l he ... # for Hebrew