class DNAStrand:
    def __init__(self, sequence):
        self.sequence = sequence

    def isValidDNA(self):
        correct = ['A', 'T', 'C', 'G']
        for t in self.sequence:
            if t not in correct:
                return False
        return True

    def complementWC(self):
        intscd = ''
        for t in self.sequence:
            if t == 'A':
                intscd += 'T'
            elif t == 'T':
                intscd += 'A'
            elif t == 'C':
                intscd += 'G'
            elif t == 'G':
                intscd += 'C'
        return intscd

    def palindromeWC(self):
        reverse = ''
        for i in range(len(self.sequence)-1, -1, -1):
            reverse += self.sequence[i]
        return reverse

    def containsSequence(self, seq):
        if seq in self.sequence:
            return True
        else:
            return False

    def __str__(self):
        return self.sequence + '\n                        ' + self.complementWC()

dna = DNAStrand('ATCGCG')


def summarise(dna):
    print("Original DNA Sequence: ", dna)
    if dna.isValidDNA():
        print("Is valid")
        print("Complement: ", dna.complementWC())
        print("WC Palindrome: ", dna.palindromeWC())
    else:
        print("Not Valid DNA")


summarise(dna)