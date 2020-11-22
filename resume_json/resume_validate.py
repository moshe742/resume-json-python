import jsonschema


class ResumeValidate:
    def __init__(self):
        pass

    def validate(self, file_to_validate, schema):
        try:
            res = jsonschema.validate(file_to_validate, schema)
            return res
        except jsonschema.exceptions.ValidationError as ex:
            validation_error = []
            for item in ex.path:
                validation_error.append(str(item))
        return '.'.join(validation_error)
