import sys
import pandas as pd
from PrimaryInputs import PrimaryInputs

# TODO: replace this with test methods
if __name__ == "__main__":    
    filepath_1 = sys.argv[1]
    filepath_2 = sys.argv[2]
    primary_inputs = PrimaryInputs(filepath_1) #"C:\\Users\\rich\\Downloads\\IO_All_2015\\IO_ABW_2015_BasicPrice.txt"
    df = primary_inputs.get_dataset(extended=True)
    primary_inputs1 = PrimaryInputs(filepath_2) # "C:\\Users\\rich\\Downloads\\IO_All_2015\\IO_AFG_2015_BasicPrice.txt"
    df2 = primary_inputs.append(primary_inputs1)
    print(df2)