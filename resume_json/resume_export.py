import os

from weasyprint import HTML

from .template_generator import TemplateGenerator


class ResumeExport(TemplateGenerator):
    """
    Export methods for json resume
    """
    def export_pdf(self, file_path: str, file_name: str, res_name: str, theme_name: str,
                   language: str = 'en') -> None:
        """
        Export the json resume to pdf.

        Export the resume to PDF format.

        :param file_path: the path to save the file at
        :param file_name: the name of the json file
        :param res_name: the resultant file name
        :param theme_name: the name of the theme to use for creating the pdf
        :param language: the language code of the resume
        :return: None
        """
        html_string = self.create_html(file_path, file_name, theme_name, language)
        pdf_file = os.path.join(file_path, res_name)
        HTML(string=html_string).write_pdf(f'{pdf_file}.pdf')

    def export_html(self, file_path: str, file_name: str, res_name: str, theme_name: str,
                    language: str = 'en'):
        """
        Export the file to HTML

        Create the html version of the resume and save it to where the user specified.
        :param file_path: the path to save the html file
        :param file_name: the resume json file name to work with
        :param res_name: the result file name to create
        :param theme_name: the theme name to implement on the resume
        :param language: the language code of the resume
        :return: None
        """
        html_data = self.create_html(file_path, file_name, theme_name, language)
        file_path = os.path.join(file_path, res_name)
        with open(f'{file_path}.html', 'w') as f:
            f.write(html_data)
