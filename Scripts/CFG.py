class CFG(object):
    '''
    Context Free Grammer Implementation,
    Functionality:
        1) Capable of drawing the chain from start to end for a CFG and and string.
        2) Example: cfg = CFG(['S'], {
                            'S':[['0', 'S', '0'], ['0', 'S','1', 'S', '0'], ['']]
                        })
                    dr = cfg.print_derivation('0000010010100', word='0S0')
                    print(dr)

    '''
    def __init__(self, alphabets, rules, ) -> None:
        super().__init__()
        self.alphabets = alphabets
        self.rules = rules
    
    def derive_helper(self, matchword, word = '', ):
        '''
        Left most derivation implementation.
        '''
        try:
            index = min([i for i in [word.find(i) for i in self.alphabets] if i >= 0])
            if len(word) < 20:
                if index != -1:
                    derivations = self.replaceLeftMost(word, index)
                    for k in derivations:
                        chain = self.derive_helper(matchword, k)
                        if chain:
                            # print(k, end=' <== ')
                            chain.append(word)
                            return chain
                elif matchword == word:
                    chain = []
                    chain.append(word)
                    return chain

        except ValueError:
            if matchword == word:
                chain = []
                chain.append(word)
                return chain
        
    def derive(self, matchword, word = ''):
        chain = self.derive_helper(matchword, word)
        return chain

    def print_derivation(self, matchword, word = ''):
        chain = self.derive_helper(matchword, word)
        if chain and len(chain)>0:
            res = ""
            for i in chain:
                res = i + "|"+res
            return res[:-1].replace('|', ' ==> ')

    def print_derivation_automate(self, matchword):
        start_word = [''.join(i) for i in cfg_5a.rules['S']]
        for i in start_word:
            res = self.print_derivation(matchword, i)
            if res:
                print(res)

    def replaceLeftMost(self, word, index):
        if index != -1:
            symbol = word[index]
            return [word[:index]+ ''.join(i)+word[index+1:] for i in self.rules[symbol]]
        else:
            return None



cfg_5a = CFG(['S','P', 'C', 'A', 'Q', 'R', 'X', 'Y', 'B'], {
    'S':[['P', 'C'], ['A', 'Q'], ['A', 'R'], ['']],
    'P':[['X']],
    'C':[['2', 'C'], ['2']],
    'A':[['0', 'A'], ['0'], ['']],
    'Q':[['Y', 'C']],
    'R':[['B', 'Y'],],
    'X':[['0', 'X', '1'], ['0', '1']],
    'Y':[['1', 'Y', '2'], ['1', '2']],
    'B':[['1', 'B'], ['1']]
    })


# res = cfg_5a.print_derivation('0011122', 'AR')
# print(res)

cfg_5a.print_derivation_automate('0011122')