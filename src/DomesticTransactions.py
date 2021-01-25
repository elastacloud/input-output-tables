import abc
import os
import pandas as pd
import numpy as np
from EoraReader import EoraReader

class DomesticTransactions(EoraReader):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.df = None

    def get_dataset(self, extended = False):
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