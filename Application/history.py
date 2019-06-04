import datetime
import uuid
import xml.etree.ElementTree as xml
import os
PATH = "./Application/History/"


class History:
    """save History."""

    def save_params(self, text, filename, command, method, system):
        self.command = command
        self.text = text
        if method == 0:
            self.method = "кнопка"
        else:
            self.method = "голос"
        self.system = system
        self.path = filename
        self.id = uuid.uuid4().hex
        now = datetime.datetime.now()
        if not os.path.exists(PATH+"history.xml"):
            self.init_file()
        self.date = now.strftime("%Y-%m-%d %H:%M:%S")

        self.addToXml(self.id,self.text,self.path, self.command, self.method, self.system, self.date)
    def addToXml(self, id, text, filename, command, method, system, date):
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

        self.method = xml.SubElement(self.id, 'method')
        self.method.text = str(method)

        self.system = xml.SubElement(self.id, 'system')
        self.system.text = str(system)

        self.date = xml.SubElement(self.id, 'date')
        self.date.text = str(date)

        tree.write(PATH + "history.xml", encoding="utf-8")

    def init_file(self):
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        test = '<History>\n' \
               '<id ID="testID">\n' \
               '<path>History/testID</path>\n' \
               '<text>texttest</text>\n' \
               '<command>"testCOmand"</command>\n' \
               '<method>20</method>\n' \
               '<system>Google</system>\n' \
               '<date>2019</date>\n' \
               '</id>\n' \
               '</History>\n'
        fd = open(PATH + "history.xml", "w+")
        fd.write(test)
        fd.close()
