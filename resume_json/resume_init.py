import json


class ResumeCreate:
    def __init__(self, ui):
        self.ui = ui

    def get_profiles(self):
        profiles = []

        while self.ui.add_another('social network account'):
            network, username, url = self.ui.get_profile()

            profiles.append({
                'network': network,
                'username': username,
                'url': url,
            })

        return profiles

    def get_position(self):
        position = self.ui.get_position()

        return {
            'name': position['name'],
            'location': position['location'],
            'description': position['description'],
            'position': position['position'],
            'url': position['url'],
            'startDate': position['startDate'],
            'endDate': position['endDate'],
            'summary': position['summary'],
        }

    def get_work_history(self):
        work_history = []

        position = self.get_position()
        position['highlights'] = self.ui.add_list_of_items('highlight')
        work_history.append(position)

        while self.ui.add_item('work'):
            position = self.get_position()
            position['highlights'] = self.ui.add_list_of_items('highlight')
            work_history.append(position)
        return work_history

    def get_volunteering_history(self):
        volunteering_history = []
        if self.ui.add_item('volunteering'):
            volunteer = self.ui.get_volunteering()
            volunteer['highlights'] = self.ui.add_list_of_items('highlight')
            volunteering_history.append(volunteer)
            while self.ui.add_another('volunteering'):
                volunteer = self.ui.get_volunteering()
                highlights = self.ui.add_list_of_items('highlight')
                volunteering_history.append({
                    'organization': volunteer['organization'],
                    'position': volunteer['position'],
                    'url': volunteer['url'],
                    'startDate': volunteer['start_date'],
                    'endDate': volunteer['end_date'],
                    'summary': volunteer['summary'],
                    'highlights': highlights
                })
        return volunteering_history

    def get_education_info(self):
        education_info = []

        while self.ui.add_item('education'):
            education_info = []

            education = self.ui.get_education_info()
            courses = self.ui.add_list_of_items('course')

            education_info.append({
                'institution': education['institution'],
                'url': education['url'],
                'area': education['area'],
                'studyType': education['study_type'],
                'startDate': education['start_date'],
                'endDate': education['end_date'],
                'gpa': education['gpa'],
                'courses': courses
            })

        return education_info

    def get_awards(self):
        awards = []

        while self.ui.add_item('award'):
            award = self.ui.get_award()
            awards.append({
                'title': award['title'],
                'date': award['date'],
                'awarder': award['awarder'],
                'summary': award['summary'],
            })

        return awards

    def get_publications(self):
        publications = []

        while self.ui.add_item('publication'):
            publication = self.ui.get_publication()
            publications.append({
                'name': publication['name'],
                'publisher': publication['publisher'],
                'releaseDate': publication['release_date'],
                'url': publication['url'],
                'summary': publication['summary'],
            })

        return publications

    def get_skills(self):
        skills = []

        while self.ui.add_item('skill'):
            skill = self.ui.get_skill()
            keywords = self.ui.add_list_of_items('keyword')
            skills.append({
                'name': skill['name'],
                'level': skill['level'],
                'keywords': keywords,
            })

        return skills

    def get_languages(self):
        languages = []

        while self.ui.add_item('language'):
            language = self.ui.get_language()
            languages.append({
                'language': language['language'],
                'fluency': language['fluency'],
            })

        return languages

    def get_interests(self):
        interests = []

        while self.ui.add_item('interest'):
            interest_name = self.ui.get_interest()
            keywords = self.ui.add_list_of_items('keyword')
            interests.append({
                'name': interest_name,
                'keywords': keywords,
            })

        return interests

    def get_references(self):
        references = []

        while self.ui.add_item('reference'):
            name, reference = self.ui.get_reference()
            references.append({
                'name': name,
                'reference': reference
            })

        return references

    def get_projects(self):
        projects = []
        while self.ui.add_item('project'):
            project = self.ui.get_project()

            highlights = self.ui.add_list_of_items('highlight')
            keywords = self.ui.add_list_of_items('keyword')
            roles = self.ui.add_list_of_items('role')

            projects.append({
                'name': project['name'],
                'description': project['description'],
                'highlights': highlights,
                'keywords': keywords,
                'startDate': project['start_date'],
                'endDate': project['end_date'],
                'url': project['url'],
                'entity': project['entity'],
                'type': project['type'],
                'roles': roles
            })

        return projects

    def create(self, file_path, file_name='resume.json'):
        country, region, city, address, postal_code = self.ui.get_location()
        full_name, profession, image, email, phone, url, summary = self.ui.get_basics()
        profiles = self.get_profiles()
        work_history = self.get_work_history()
        volunteering = self.get_volunteering_history()
        education = self.get_education_info()
        awards = self.get_awards()
        publications = self.get_publications()
        skills = self.get_skills()
        languages = self.get_languages()
        interests = self.get_interests()
        references = self.get_references()
        projects = self.get_projects()

        template = {
            "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
            "basics": {
                "name": f"{full_name}",
                "label": f"{profession}",
                "image": f"{image}",
                "email": f"{email}",
                "phone": f"{phone}",
                "url": f"{url}",
                "summary": f"{summary}",
                "location": {
                    "address": f"{address}",
                    "postalCode": f"{postal_code}",
                    "city": f"{city}",
                    "countryCode": f"{country}",
                    "region": f"{region}"
                },
                "profiles": profiles
            },
            "work": work_history,
            "volunteer": volunteering,
            "education": education,
            "awards": awards,
            "publications": publications,
            "skills": skills,
            "languages": languages,
            "interests": interests,
            "references": references,
            "projects": projects,
            "meta": {
                "canonical": "https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json",
                "version": "v1.0.0",
                "lastModified": "2017-12-24T15:53:00"
            }
        }
        with open(f'{file_path}/{file_name}', 'w') as f:
            json.dump(template, f, indent=4)
