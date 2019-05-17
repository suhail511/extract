
def metadata_vermont(lines):
    print("Invoice number : " + lines[24][:-1])
    print("Invoice Date : " + lines[22][:-1])
    print("Purchase Order Number : " + lines[25][:-1])
    print("Invoice Total : " + lines[388][1:-1])
    print("Payment terms : NA" )
    print("")

def metadata_oracle(lines):
    print("Invoice number : " + lines[13][:-1])
    print("Invoice Date : " + lines[14][:-1])
    print("Purchase Order Number : " + lines[15][:-1])
    print("Invoice Total : " + lines[128][1:-1])
    print("Payment terms : NA" )
    print("")

def metadata_asian_pacific(lines):
    print("Invoice number : " + lines[54][:-1])
    print("Invoice Date : " + lines[50][:-1])
    print("Purchase Order Number : NA")
    print("Invoice Total : " + lines[65][1:-1])
    print("Payment terms : NA" )
    print("")

def metadata_bears(lines):
    print("Invoice number : " + lines[18][:-1])
    print("Invoice Date : " + lines[19][:-1])
    print("Purchase Order Number : NA")
    print("Invoice Total : " + lines[58][:-1])
    print("Payment terms : " + lines[62][:-1] + lines[63][:-1])
    print("")

def metadata_airport(lines):
    print("Invoice number : " + lines[14][:-1])
    print("Invoice Date : " + lines[47][:-1])
    print("Purchase Order Number : " + lines[5][3:-1])
    print("Invoice Total : " + lines[65][1:-1])
    print("Payment terms : NA" )
    print("")
