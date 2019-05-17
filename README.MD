# Entity Extraction

Extract Information from Invoices.
Invoice Number, Invoice Date, Purchase Order Number, Line Item details (quantity, sku, name, price, etc), Invoice Total, Payment terms.

## Requirements and Installation

It is done in Python 3.7, MacOS. In order to run these scripts, you'll need the following libraries.

* re
* os
* glob
* pdfminer

## Running

### Convert pdfs to text files

First we need the files in text format. Here I have implimented only for documents and not for scanned pdfs:

```bash
python pdfconverter.py
```

Files will be generated for each pdf file in the folder "text_format"

### Getting the relevant information

Now we need to get the information from these files. Since I don't have a large dataset, I have decided not to go for an ML solution. But I have implimented a crude regex solution with line scanner.

``` bash
python extract.py
```

This should show the respective outputs

### Adding new invoice formats

If the need arises to add new invoice formats, the code can be modified for every new invoice in the database and get information (entities) from them.
