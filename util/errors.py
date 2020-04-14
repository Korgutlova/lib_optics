class RefractiveIndexNotFound(Exception):
    def __init__(self, media):
        super(RefractiveIndexNotFound, self).__init__(f'Индекс среды "{media}" не найден.')


class InvalidArgumentForLens(ValueError):
    def __init__(self, message):
        super(InvalidArgumentForLens, self).__init__(message)
