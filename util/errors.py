class RefractiveIndexNotFound(ValueError):
    def __init__(self, message):
        super(RefractiveIndexNotFound, self).__init__(message)


class InvalidRefractiveIndex(ValueError):
    def __init__(self, message):
        super(InvalidRefractiveIndex, self).__init__(message)


class InvalidArgumentForLens(ValueError):
    def __init__(self, message):
        super(InvalidArgumentForLens, self).__init__(message)


class InvalidArgumentForAngle(ValueError):
    def __init__(self, message):
        super(InvalidArgumentForAngle, self).__init__(message)


class InvalidArgumentStyleGraphic(ValueError):
    def __init__(self, message):
        super(InvalidArgumentStyleGraphic, self).__init__(message)


class NotEnoughKnownValuesForLensGraphic(AttributeError):
    def __init__(self, message):
        super(NotEnoughKnownValuesForLensGraphic, self).__init__(message)


class MissingObjectHeight(AttributeError):
    def __init__(self, message):
        super(MissingObjectHeight, self).__init__(message)