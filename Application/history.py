import uuid, datetime
import xml.etree.ElementTree as xml

PATH = "History/"


class History(object):
    """save History."""

    def save_params(self, text,command, similarity, system):
        self.command = command
        self.text = text
        self.similarity = similarity
        self.system = system
        self.id = uuid.uuid4().hex
        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d %H:%M:%S")

        self.addToXml(self.id,self.text,self.command,self.similarity,self.system,self.date)

    def addToXml(self, id, text,command, similarity, system, date):
        tree = xml.ElementTree(file="Application/History/history.xml")
        root = tree.getroot()

        attrib = {'ID': str(id)}
        self.id = xml.SubElement(root,"id",attrib)
        self.id.tail = "\n      "

        self.text = xml.SubElement(self.id,'text')
        self.text.text = str(text)
        self.text.tail = "\n      "

        self.command = xml.SubElement(self.id,'command')
        self.command.text = str(command)
        self.command.tail = "\n      "

        self.similarity = xml.SubElement(self.id, 'similarity')
        self.similarity.text = str(similarity)
        self.command.tail = "\n      "

        self.system = xml.SubElement(self.id, 'system')
        self.system.text = str(system)
        self.command.tail = "\n      "

        self.date = xml.SubElement(self.id, 'date')
        self.date.text = str(date)
        self.command.tail = "\n      "

        tree.write("Application/History/history.xml")


