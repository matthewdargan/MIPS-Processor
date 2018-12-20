import csv
import sys

def bin2hex(s):
    b = ''.join(s.split(' '))
    n = int((len(b) - 1) / 4) + 1
    if 'x' in b:
        return 'x' * n
    return "{:x}".format(int(b, 2)).zfill(n)

def print_usage():
    print("Usage: {} <alu|regfile|cpu>".format(sys.argv[0]))
    print()
    print("\tTakes the logisim output on standard input and writes decoded version to standard output.")
    print("\tThe first argument states what circuit produced the input.")
    sys.exit(-1)

class OutputFormatException(Exception):
    pass

class OutputFormat:
    def __init__(self, typ, headers, bitwidths):
        self.typ = typ
        assert len(headers) == len(bitwidths)
        self.headers = headers
        self.bitwidths = bitwidths

    def validate(self, values):
        if not (len(values) == len(self.bitwidths)):
                raise OutputFormatException("incorrect number of values: {0} instead of {1}".format(len(values), len(self.bitwidths)))

        # checks assuming positive integer interpretation
        for i in range(0, len(values)):
            if not (values[i] < 2**self.bitwidths[i]):
                raise OutputFormatException("incorrect bitwidth in item {0} of {1}".format(i, values))

    def header(self, wtr):
        wtr.writerow(self.headers)

def get_test_format(typ):
    if typ == 'alu':
        return OutputFormat('alu', ["Test #", "OF", "Eq", "Result"], [8,1,1,32])  
    elif typ == 'regfile':
        return OutputFormat('regfile', ["Test #", "$s0 Value", "$s1 Value", "$s2 Value", "$ra Value", "$sp Value", "Read Data 1", "Read Data 2"], [8, 32, 32, 32, 32, 32, 32, 32])
    elif typ == 'cpu':
       return OutputFormat('cpu',  ['$s0 Value', '$s1 Value', '$s2 Value', '$ra Value', '$sp Value', 'Time Step', 'Fetch Addr', 'Instruction'], [32,32,32,32,32,8,32,32])
    else:
       return None

def main():
    if len(sys.argv) < 2:
        print_usage()

    typ = sys.argv[1]
    rdr = csv.reader(sys.stdin, delimiter='\t')
    wtr = csv.writer(sys.stdout, delimiter='\t')
    
    if not headers(wtr, typ):
        print_usage()

    for row in rdr:
        wtr.writerow([bin2hex(b) for b in row])

if __name__ == '__main__':
    main()
