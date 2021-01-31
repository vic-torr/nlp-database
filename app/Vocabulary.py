from typing import List, Dict, Tuple, Any, Union, Set


class Vocabulary:
    global_vocab = set()
    global_two_gram_vocab = set()
    doc_vocabulary = List[Set]
    doc_two_gram_vocab = List[Set]

    def __init__(self):
        pass
    
    def add_doc(self, text: str):
        pass   
         
    def get_vocab(self):
        return self.global_vocab
        
    def get_two_gram_vocab(self):
        return self.global_two_gram_vocab
        
    def get_docs_vocab(self):
        return self.doc_vocabulary
        
    def get_docs_two_gram_vocab(self):
        return self.doc_two_gram_vocab
        
        
        
