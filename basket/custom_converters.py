# https://stackoverflow.com/a/48868140
class NegativeIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value
