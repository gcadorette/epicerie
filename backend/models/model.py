from dataclasses import dataclass
from helper.generator import Generator

@dataclass
class Model:
    id: str
    def __init__(self):
        self.id = Generator.generate_id(self)

    def to_csv_string(self):
        return ",".join([str(x) for x in list(self.__dict__.values())[:-1]]) + "\n"
