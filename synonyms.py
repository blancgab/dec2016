'''Baby Names
Each year, the government releases a list of the 10000 most common
baby names and their frequencies. The only problem is that some names
have multiple spellings, i.e. "John" and "Jonathan". Given two lists,
one of names/frequencies and and the other of pair of equivalent
names, write an algorithm to print a new list of the true frequency
of each name.
'''
class NameSet:
    def __init__(self,name,freq=0):
        self.name = name
        self.freq = freq
        self.synonyms = set([name])

    def merge(self,other_ns):        
        self.synonyms = self.synonyms.union(other_ns.synonyms)
        self.freq += other_ns.freq
        
def synonym_map(syn_array,name_freqs):
    smap = {}
    for n1,n2 in syn_array:
        if n1 not in smap:
            smap[n1] = NameSet(n1)
        if n2 not in smap:
            smap[n2] = NameSet(n2)

        # Merge into a single NameSet
        smap[n1].merge(smap[n2])
        for syn in smap[n2].synonyms:
            smap[syn] = smap[n1]
    
    for name,freq in name_freqs:
        if name not in smap:
            smap[name] = NameSet(name)
        smap[name].freq += freq
    
    truenames = set(smap.values())
    return truenames

if __name__ == '__main__':
    synonyms = [
        ('John','Jon'),
        ('Jonathan','Johnathan'),
        ('Jon','Jonathan'),
        ('Bill','William'),
        ('William','Willy')]

    name_freqs = [
        ('Alex',12),
        ('John',2),
        ('Jon',5),
        ('Richard',3),
        ('Jonathan',1),
        ('Johnathan',0),
        ('Bill',3),
        ('William',1),
        ('Willy',20),
        ('Gabriel',1),
        ('Nate',1)]

    truenames = synonym_map(synonyms,name_freqs)
    
    for tn in truenames:
        print ('{}: {} -- Synonyms: {}'.format(tn.name,tn.freq,list(tn.synonyms)))

