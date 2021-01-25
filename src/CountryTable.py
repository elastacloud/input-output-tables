import enum
from EoraReader import EoraReader
from PrimaryInputs import PrimaryInputs
from DomesticTransactions import DomesticTransactions

class CountryTableSegment(enum.Enum):
   DomesticTransations = 1
   PrimaryInputs = 2

class CountryTable(EoraReader):
    def __init__(self, segment, file_path):
        self.segment = segment 
        self.table_class = None
        if segment == CountryTableSegment.DomesticTransations:
            self.table_class = DomesticTransactions(file_path)
        else: self.table_class = PrimaryInputs(file_path)

    def get_dataset(self, extended = False):
        return self.table_class.get_dataset(extended)

    def append(self, country_table_part):
        return self.table_class.append(country_table_part.table_class)