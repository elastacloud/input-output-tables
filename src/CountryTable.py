import enum
from EoraReader import EoraReader
from PrimaryInputs import PrimaryInputs
from DomesticTransactions import DomesticTransactions
from os import listdir
from os.path import isfile, join
import pandas as pd

class CountryTableSegment(enum.Enum):
   DomesticTransations = 1
   PrimaryInputs = 2

class CountryTable(EoraReader):
    def __init__(self, segment, file_path):
        self.segment = segment 
        self.table_class = []
        self.files = self.__get_files(file_path)
        self.__process_files(segment, file_path)
        
    def __get_files(self, path):
        if not isfile(path): return [join(path, f) for f in listdir(path) if isfile(join(path, f))]
        else: return [path]

    def __process_files(self, segment, file_path):
        for file in self.files:
            if segment == CountryTableSegment.DomesticTransations:
                er = DomesticTransactions(file)
                self.table_class.append(er)
            else: 
                er = PrimaryInputs(file)
                self.table_class.append(er)

    def get_dataset(self, extended = False):
        df = pd.DataFrame() # empty df here
        for t_class in self.table_class:
            if not df.empty:
                df = df.append(t_class.get_dataset(extended))
            else: df = t_class.get_dataset(extended)
        self.df = df
        return df

    def append(self, country_table_part):
        return self.table_class.append(country_table_part.table_class)