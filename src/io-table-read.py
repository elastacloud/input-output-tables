import sys
import pandas as pd
from CountryTable import CountryTable
from CountryTable import CountryTableSegment

# TODO: replace this with test methods
if __name__ == "__main__":    
    filepath_1 = sys.argv[1]
    table1 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_1)
    print(table1.get_dataset(True))
