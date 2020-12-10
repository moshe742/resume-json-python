import typing
from abc import ABC


class UI(ABC):
    """
    Base class as an interface for ui classes for resume json

    One should use this class as a base to know which methods to implement and
    what signatures one should implement, for an actual example look at BasicTui
    below.
    """
    def get_location(self) -> typing.Dict:
        """
        Method to get the location data.
        :return: dict with the location data
        """
        pass

    def get_basics(self) -> typing.Tuple:
        """
        Method for getting the data for all the basic information.

        This method returns a tuple, that is because it holds more information and
        data structures than other places and it's less related to each other.
        Thus the decision was to have it as a tuple to make sure it's still as readable
        as it can be while still easy to work with.

        :return: tuple of the basic data
        """
        pass

    def add_item(self, item: str) -> bool:
        """
        Method to check if the user want to add subject section or leave it blank.

        :param item: the string one wants to ask about
        :return: bool according to the user answer
        """
        pass

    def add_another(self, item: str) -> bool:
        """
        Method to check if the user want to add more data on the subject processed now.

        :param item: the string one wants to ask about
        :return: bool according to the user answer
        """
        pass

    def get_profile(self) -> typing.Dict:
        """
        Method to get the data about the user profile of social networks and such.

        :return: dict with the data about the network
        """
        pass

    def get_position(self) -> typing.Dict:
        """
        Method to get the data about the position of the user.
        :return: dict
        """
        pass

    def get_volunteering(self) -> typing.Dict:
        """
        Method to get information about the volunteering history of the user.
        :return:
        """
        pass

    def add_list_of_items(self, kind: str) -> typing.List[str]:
        """
        Method to get a list of items of kind <kind> (according to the section one is
        filling).
        :param kind:
        :return:
        """
        pass

    def get_education_info(self) -> typing.Dict:
        """
        Method to get the information about the education of the user.
        :return:
        """
        pass

    def get_award(self) -> typing.Dict:
        """
        Method to get the information about an award the user received.
        :return:
        """
        pass

    def get_publication(self) -> typing.Dict:
        """
        Method to get the information about a publication of the user.
        :return:
        """
        pass

    def get_skill(self) -> typing.Dict:
        """
        Method to get a skill of the user.
        :return:
        """
        pass

    def get_language(self) -> typing.Dict:
        """
        Method to get a language the user knows.
        :return:
        """
        pass

    def get_interest(self) -> str:
        """
        Method to get an interest of the user.
        :return:
        """
        pass

    def get_reference(self) -> typing.Dict:
        """
        Method to get a reference/recommendation of the user.
        :return:
        """
        pass

    def get_project(self) -> typing.Dict:
        """
        Method to get information about a project of the user.
        :return:
        """
        pass


class BasicTui(UI):
    """
    A class that implements the UI interface methods.

    This is the class that works as the default implementation for the cli interface
    """
    def get_location(self) -> typing.Dict:
        country = input('country code: ')
        region = input('region: ')
        city = input('city: ')
        address = input('address: ')
        postal_code = input('postal code: ')
        return {
            'country': country,
            'region': region,
            'city': city,
            'address': address,
            'postal_code': postal_code,
        }

    def get_basics(self) -> typing.Tuple:
        full_name = input('full name: ')
        email = input('email: ')
        phone = input('phone: ')
        profession = input('profession: ')
        image = input('image: ')
        url = input('url: ')
        summary = input('summary: ')
        return full_name, profession, image, email, phone, url, summary

    def add_item(self, item: str) -> bool:
        res = input(f'want to add {item}? [no] ').lower()
        return res == 'y' or res == 'yes'

    def add_another(self, item: str) -> bool:
        res = input(f'want to add another {item} [no]? ').lower()
        return res == 'y' or res == 'yes'

    def get_profile(self) -> typing.Dict:
        network = input('network: ')
        username = input('username: ')
        url = input('url: ')
        return {
            'network': network,
            'username': username,
            'url': url
        }

    def get_position(self) -> typing.Dict:
        company_name = input('company name: ')
        location = input('location: ')
        company_description = input('company description: ')
        position = input('position: ')
        company_url = input('company url: ')
        start_date = input('start date [YYYY-mm-dd]: ')
        end_date = input('end date [YYYY-mm-dd]: ')
        summary = input('summary: ')
        return {
            'name': company_name,
            'location': location,
            'description': company_description,
            'position': position,
            'url': company_url,
            'startDate': start_date,
            'endDate': end_date,
            'summary': summary,
        }

    def get_volunteering(self) -> typing.Dict:
        organization = input('volunteering organization: ')
        position = input('volunteering position: ')
        url = input('volunteering organization url: ')
        start_date = input('start date [YYYY-mm-dd]: ')
        end_date = input('end date [YYYY-mm-dd]: ')
        summary = input('summary: ')
        return {
            'organization': organization,
            'position': position,
            'url': url,
            'start_date': start_date,
            'end_date': end_date,
            'summary': summary,
        }

    def add_list_of_items(self, kind: str) -> typing.List[str]:
        items = []
        while self.add_item(kind):
            item = input(f'{kind}: ')
            items.append(item)
        return items

    def get_education_info(self) -> typing.Dict:
        institution = input('institution: ')
        url = input('institution url: ')
        area = input('study subject: ')
        study_type = input('degree type (BA, Bachelor, etc.): ')
        start_date = input('start date [YYYY-mm-dd]: ')
        end_date = input('end date [YYYY-mm-dd]: ')
        gpa = input('gpa: ')
        return {
            'institution': institution,
            'url': url,
            'area': area,
            'study_type': study_type,
            'start_date': start_date,
            'end_date': end_date,
            'gpa': gpa,
        }

    def get_award(self) -> typing.Dict:
        title = input('award title: ')
        award_date = input('date [YYYY-mm-dd]: ')
        awarder = input('awarder: ')
        summary = input('summary: ')
        return {
            'title': title,
            'date': award_date,
            'awarder': awarder,
            'summary': summary,
        }

    def get_publication(self) -> typing.Dict:
        name = input('publication name: ')
        publisher = input('publisher: ')
        release_date = input('release date: ')
        url = input('url: ')
        summary = input('summary: ')
        return {
            'name': name,
            'publisher': publisher,
            'release_date': release_date,
            'url': url,
            'summary': summary,
        }

    def get_skill(self) -> typing.Dict:
        name = input('skill name: ')
        level = input('level: ')
        return {
            'name': name,
            'level': level,
        }

    def get_language(self) -> typing.Dict:
        language = input('language name: ')
        fluency = input('fluency: ')
        return {
            'language': language,
            'fluency': fluency,
        }

    def get_interest(self) -> str:
        return input('interest name: ')

    def get_reference(self) -> typing.Dict:
        name = input('name: ')
        reference = input('reference: ')
        return {
            'name': name,
            'reference': reference,
        }

    def get_project(self) -> typing.Dict:
        project_name = input('project name: ')
        description = input('description: ')
        start_date = input('start date [YYYY-mm-dd]: ')
        end_date = input('end dte [YYYY-mm-dd]: ')
        url = input('url: ')
        entity = input('entity: ')
        project_type = input('type: ')
        return {
            'name': project_name,
            'description': description,
            'start_date': start_date,
            'end_date': end_date,
            'url': url,
            'entity': entity,
            'type': project_type,
        }
