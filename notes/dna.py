version = '1.0'

def complement(seq):
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join([d.get(nt, 'N') for nt in seq])

def reverse_complement(seq):
    return complement(seq)[::-1]

if __name__ == '__main__':
    seq = input('Enter a DNA sequence: ')
    cseq = complement(seq)
    print(f'Complement: {cseq}')