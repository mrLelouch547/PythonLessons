class MissingParameterError(Exception):
    pass
class InvalidParameterError(Exception):
    def __init__(self,name):
       self.name  = name
       name  = '"Invalid class parameter: name"'
class InvalidAgeError(InvalidParameterError):
    pass
class InvalidSoundError(InvalidParameterError):
    pass


