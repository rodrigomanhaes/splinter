from splinter.exceptions import ElementDoesNotExist


class ElementList(list):
    def __init__(self, list, context=None, driver=None):
        self.extend(list)
        self.context = context
        self.driver = driver

    def __getitem__(self, index):
        try:
            return super(ElementList, self).__getitem__(index)
        except IndexError:
            raise ElementDoesNotExist('element does not exist')

    @property
    def first(self):
        return self[0]

    @property
    def last(self):
        return self[-1]

    def find_by_css(self, element):
        return self.driver.find_by_css(element)

    def is_empty(self):
        return len(self) == 0

    def __getattr__(self, name):
        try:
            return getattr(self.first, name)
        except (ElementDoesNotExist, AttributeError):
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
