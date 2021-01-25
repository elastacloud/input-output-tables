import sys
import pandas as pd
from CountryTable import CountryTable
from CountryTable import CountryTableSegment

# TODO: replace this with test methods
if __name__ == "__main__":    
    filepath_1 = sys.argv[1]
    filepath_2 = sys.argv[2]
    table1 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_1)
    table2 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_2)
    df = table2.append(table1)
    print(df)
    