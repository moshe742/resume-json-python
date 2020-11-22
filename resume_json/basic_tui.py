def get_location():
    country = input('country code: ')
    region = input('region: ')
    city = input('city: ')
    address = input('address: ')
    postal_code = input('postal code: ')
    return country, region, city, address, postal_code


def get_basics():
    full_name = input('full name: ')
    email = input('email: ')
    phone = input('phone: ')
    profession = input('profession: ')
    image = input('image: ')
    url = input('url: ')
    summary = input('summary: ')
    return full_name, profession, image, email, phone, url, summary


def add_item(item):
    res = input(f'want to add {item}? [no] ').lower()
    return res == 'y' or res == 'yes'


def add_another(item):
    res = input(f'want to add another {item} [no]? ').lower()
    return res == 'y' or res == 'yes'


def get_profile():
    network = input('network: ')
    username = input('username: ')
    url = input('url: ')
    return network, username, url


def get_position():
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


def get_volunteering():
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


def add_list_of_items(kind):
    items = []
    while add_item(kind):
        item = input(f'{kind}: ')
        items.append(item)
    return items


def get_education_info():
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


def get_award():
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


def get_publication():
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


def get_skill():
    name = input('skill name: ')
    level = input('level: ')
    return {
        'name': name,
        'level': level,
    }


def get_language():
    language = input('language name: ')
    fluency = input('fluency: ')
    return {
        'language': language,
        'fluency': fluency,
    }


def get_interest():
    return input('interest name: ')


def get_reference():
    name = input('name: ')
    reference = input('reference: ')
    return name, reference


def get_project():
    project_name = input('project name: ')
    desciption = input('description: ')
    start_date = input('start date [YYYY-mm-dd]: ')
    end_date = input('end dte [YYYY-mm-dd]: ')
    url = input('url: ')
    entity = input('entity: ')
    project_type = input('type: ')
    return {
        'name': project_name,
        'description': desciption,
        'start_date': start_date,
        'end_date': end_date,
        'url': url,
        'entity': entity,
        'type': project_type,
    }
