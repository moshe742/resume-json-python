import json
import logging
import typing

import jsonschema
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ResumeValidate:
    def validate(self, file_to_validate: str, schema: typing.Dict = None) -> typing.Union[None, str]:
        """
        Validate the json according to the schema.

        Validating the schema with jsonschema. If one want to validate more things such as making
        sure all the dates are in the past or that the education places names are written correctly
        one can inherit this class, use the function and add their logic for enhancement as needed.

        :param file_to_validate: the path and file name one want to validate
        :param schema: the schema to validate against
        :return: None if valid, the path in the json of the mistake found if validation failed.
        """
        with open(f'{file_to_validate}') as f:
            file_validate = json.load(f)
        if schema is None:
            schema_url = file_validate['$schema']
            res = requests.get(schema_url)
            schema = json.loads(res.text)
        try:
            res = jsonschema.validate(file_to_validate, schema)
            return res
        except jsonschema.exceptions.ValidationError as ex:
            validation_error = []
            logger.error(ex.message)
            for item in ex.path:
                validation_error.append(str(item))
        return '.'.join(validation_error)
