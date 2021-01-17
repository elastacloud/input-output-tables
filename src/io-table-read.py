import abc
import os
import pandas as pd
import numpy as np

class EoraReader(abc.ABC):
    def __init__(self, file_path, coords):
        self.coords = coords
        self.file_path = file_path
        self.file = self.__read_header__()
        
    def __firstline__(self, first_line):
        # walk the first string by using the ; delimeter 
        header = first_line[0:60]
        header_tokens = header.split(';')
        year_pos = header_tokens[0].index("Year: ") + len("Year: ")
        self.year = int(header_tokens[0][year_pos:year_pos + 4])
        unit_pos = header_tokens[1].index("Unit: ") + len("Unit: ")
        self.unit = header_tokens[1][unit_pos::]
        self.type = header_tokens[2][1::]
        self.eora_version = float(''.join([char if (char.isnumeric() or char == ".") else "" for char in header_tokens[3]]).strip())
        self.countries = first_line[first_line.index(str(self.eora_version)) + len(str(self.eora_version))::].strip().split('\t')
        self.country = max(set(self.countries), key = self.countries.count) 
    
    def __read_header__(self):
        f = open(self.file_path, "r")
        first_line = f.readline()
        self.__firstline__(first_line)
        self.country_codes = f.readline().strip().split('\t')
        self.industry_header = f.readline().strip().split('\t')
        self.industries = f.readline().strip().split('\t')
        return f

    @abc.abstractmethod
    def get_dataset(self):
        return

class DomesticTransactions(EoraReader):
    def __init__(self, file_path):
        super().__init__(file_path, 0)

    def get_dataset(self):
        """
        Returns a pandas dataframe containing domestic transactions from the input-output table 
        """
        domestic_transaction_coefficients = []
        industry_count = self.industry_header.count("Industries")
        print(industry_count)
        for i in range(0, industry_count):
            domestic_transaction_coefficients.append(self.file.readline().strip().split('\t')[4:(4 + industry_count)])
        numpy_data = np.array(domestic_transaction_coefficients)
        df = pd.DataFrame(data = numpy_data, index = self.industries[0:industry_count])
        df.columns = self.industries[0:industry_count]
        return df