class window:
    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
        return self._data.get(name)

    def __setattr__(self, name, value):
        self._data[name] = value

class Dataset:
    def __init__(self, element):
        self.element = element

    def __getattr__(self, name):
        return self.element.getAttribute('data-' + name)

    def __setattr__(self, name, value):
        self.element.setAttribute('data-' + name, value)

class Element:

    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.dataset = Dataset(self)
        self.attributes = {}

    def appendChild(self, element):
        self.children.append(element)

    def setAttribute(self, name, value):
        self.attributes[name] = value

    def getAttribute(self, name):
        return self.attributes.get(name)

class Document:
    def __init__(self):
        self._data = {}
        self._id = {}

    def __getattr__(self, name):
        return self._data.get(name)

    def __setattr__(self, name, value):
        self._data[name] = value

    def createElement(self, tag,id):
        self._data[id] = tag
        self._id[id] = Element(tag)
        return self._data.get(id)

    def getElementById(self, element_id):
        return self._id.get(element_id)