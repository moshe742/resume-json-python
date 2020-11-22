import os

from weasyprint import HTML

from resume_json.template_generator import TemplateGenerator


class ResumeExport(TemplateGenerator):
    def export_pdf(self, file_path, file_name, res_name, theme_name, language='en'):
        html_string = self.create_html(file_path, file_name, theme_name, language)
        pdf_file = os.path.join(file_path, res_name)
        HTML(string=html_string).write_pdf(f'{pdf_file}.pdf')

    def export_html(self, file_path, file_name, res_name, theme_name, language='en'):
        html_data = self.create_html(file_path, file_name, theme_name, language)
        file_path = os.path.join(file_path, res_name)
        with open(f'{file_path}.html', 'w') as f:
            f.write(html_data)
