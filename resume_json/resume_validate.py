import jsonschema
import typing


class ResumeValidate:
    def validate(self, file_to_validate: str, schema: typing.Dict) -> typing.Union[None, str]:
        """
        Validate the json according to the schema.

        Validating the schema with jsonschema. If one want to validate more things such as making
        sure all the dates are in the past or that the education places names are written correctly
        one can inherit this class, use the function and add their logic for enhancement as needed.

        :param file_to_validate: the path and file name one want to validate
        :param schema: the schema to validate against
        :return: None if valid, the path in the json of the mistake found if validation failed.
        """
        try:
            res = jsonschema.validate(file_to_validate, schema)
            return res
        except jsonschema.exceptions.ValidationError as ex:
            validation_error = []
            for item in ex.path:
                validation_error.append(str(item))
        return '.'.join(validation_error)
