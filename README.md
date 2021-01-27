# Input Output Tables
Describes a reader interface for input-output tables for Eora data 

To leverage simply use a file downloaded from Eora.

Supports country tables only currently including:
- DomesticTransactions 
- PrimaryInputs

Supports a factory method and can be used like so:

```
if __name__ == "__main__":    
    filepath_1 = sys.argv[1]
    filepath_2 = sys.argv[2]
    table1 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_1)
    table2 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_2)
    df = table2.append(table1)
    print(df)
```

Also supports this where the file path is a folder and reads in all files returning a single dataframe.

```
filepath_1 = sys.argv[1]
table1 = CountryTable(CountryTableSegment.PrimaryInputs, filepath_1)
print(table1.get_dataset(True))
```

Which returns a pandas dataframe. Using extended = True will add year and country columns. In addition the append method will add additional country tables so that you can have an uber country pandas dataframe. Next versions of this will allow directories to be read and country table segments to be created from them.

Currently only supports country tables but will be extended to mrio at a later stage.

Country tables defined using the following schema.

![Country Tables](docs/iotables.png)

Returns a pandas dataframe of a certain type like so (for PrimaryInputs):

![Primary Inputs](docs/primary_inputs.png)
