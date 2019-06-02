import datetime
import uuid
import xml.etree.ElementTree as xml

PATH = "./Application/History/"


class History:
    """save History."""

    def save_params(self, text, filename, command, similarity, system):
        self.command = command
        self.text = text
        self.similarity = similarity
        self.system = system
        self.path = filename
        self.id = uuid.uuid4().hex
        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d %H:%M:%S")

        self.addToXml(self.id, self.text, self.path, self.command, self.similarity, self.system, self.date)

    def addToXml(self, id, text, filename, command, similarity, system, date):
        tree = xml.ElementTree(file=PATH + "history.xml")
        root = tree.getroot()

        attrib = {'ID': str(id)}
        self.id = xml.SubElement(root, "id", attrib)
        self.id.tail = "\n      "

        self.text = xml.SubElement(self.id, 'path')
        self.text.text = str(filename)

        self.text = xml.SubElement(self.id, 'text')
        self.text.text = str(text)

        self.command = xml.SubElement(self.id, 'command')
        self.command.text = str(command)

        self.similarity = xml.SubElement(self.id, 'similarity')
        self.similarity.text = str(similarity)

        self.system = xml.SubElement(self.id, 'system')
        self.system.text = str(system)

        self.date = xml.SubElement(self.id, 'date')
        self.date.text = str(date)

        tree.write(PATH + "history.xml", encoding="utf-8")
