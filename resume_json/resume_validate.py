import json
import logging
from pathlib import Path
import typing

import jsonschema
import requests


logger = logging.getLogger(__name__)


class ResumeValidate:
    def validate(self, file_to_validate_path: str, file_name: str, schema: typing.Dict = None) -> typing.Union[None, str]:
        """
        Validate the json according to the schema.

        Validating the schema with jsonschema. If one want to validate more things such as making
        sure all the dates are in the past or that the education places names are written correctly
        one can inherit this class, use the function and add their logic for enhancement as needed.

        :param file_to_validate_path: the path of the file one want to validate
        :param file_name: the name of the file one want to validate
        :param schema: the schema to validate against
        :return: None if valid, the path in the json of the mistake found if validation failed.
        """
        path = Path(file_to_validate_path, file_name)
        with open(path) as f:
            file_validate = json.load(f)
        if schema is None:
            logger.info('Info: schema was not provided, check from file')
            schema_url = file_validate['$schema']
            res = requests.get(schema_url)
            schema = json.loads(res.text)
        try:
            logger.info('Info: validating file')
            res = jsonschema.validate(file_validate, schema)
            return res
        except jsonschema.exceptions.ValidationError as ex:
            validation_error = []
            for item in ex.path:
                validation_error.append(str(item))
        return '.'.join(validation_error)
