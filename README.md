# Input Output Tables
Describes a reader interface for input-output tables for Eora data 

To leverage simply use a file downloaded from Eora.

Currently supports only Domestic Transactions and can be used like so:

```
transactions = DomesticTransactions("C:\\Users\\rich\\Downloads\\IO_All_2015\\IO_ABW_2015_BasicPrice.txt")
transactions.get_dataset()
```

Which returns a pandas dataframe.

Currently only supports country tables but will be extended to mrio at a later stage.

Country tables defined using the following schema.

[Country Tables](docs/iotables.png)
