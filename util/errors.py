class RefractiveIndexNotFound(ValueError):
    def __init__(self, media):
        super(RefractiveIndexNotFound, self).__init__(f'Индекс среды "{media}" не найден.')


class InvalidRefractiveIndex(ValueError):
    def __init__(self, message):
        super(InvalidRefractiveIndex, self).__init__(message)


class InvalidArgumentForLens(ValueError):
    def __init__(self, message):
        super(InvalidArgumentForLens, self).__init__(message)


class InvalidArgumentForAngle(ValueError):
    def __init__(self, message):
        super(InvalidArgumentForAngle, self).__init__(message)
