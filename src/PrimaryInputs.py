import abc
import os
import pandas as pd
import numpy as np
from EoraReader import EoraReader

class PrimaryInputs(EoraReader):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.df = None

    def get_dataset(self, extended = False):
        """
        Returns a pandas dataframe containing domestic transactions from the input-output table 
        """
        value_add_coefficients = []
        primary_inputs = []
        industry_count = self.industry_header.count("Industries")
        primary_inputs_pos = 0
        line = self.file.readline().strip().split('\t')
        while line[2] != "Primary Inputs":
            line = self.file.readline().strip().split('\t')
        while line[2] == "Primary Inputs":
            primary_inputs.append(line[3])
            value_add_coefficients.append(line[4:(4 + industry_count)])
            line = self.file.readline().strip().split('\t')
        numpy_data = np.array(value_add_coefficients)
        df = pd.DataFrame(data = numpy_data, index = primary_inputs)
        df.columns = self.industries[0:industry_count]
        if extended:
            df.loc[:, 'year'] = self.year
            df.loc[:, 'country'] = self.country
        self.df = df
        self.extended = extended
        return df

    def append(self, country_table_part):
        """ Used to append two domestic country tables together """
        if country_table_part.df == None: country_table_part.get_dataset(self.extended)
        self.df = self.df.append(country_table_part.df)
        return self.df