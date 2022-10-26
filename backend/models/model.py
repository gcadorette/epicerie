from dataclasses import dataclass
from helper.generator import Generator

@dataclass
class Model:
    guid: str
    def __init__(self, guid):
        self.guid = guid if guid else Generator.generate_id(self)

    def to_csv_string(self):
        return ",".join([str(x) for x in self.__dict__.values()]) + "\n"
