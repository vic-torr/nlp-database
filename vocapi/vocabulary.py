from typing import List, Dict, Tuple, Any, Union, Set
import re

class Vocabulary:
    def __init__(self):
        self.global_vocab = set()
        self.global_two_gram_vocab = set()
        self.doc_vocabulary = List[Set]
        self.doc_two_gram_vocab = List[Set]
        self.is_empty = True
        self.words_docs = list()
        self.docs_words_frequency = list(list)
        
    def add_doc(self, text: str):
        all_words_list = re.findall(r'\w+', text)
        words_set = set(all_words_list)
        words_list = list(words_set)
        words_frequency = list()
        for w in words_list:
            words_frequency.append(words_list.count(w))
        self.docs_words_frequency.append(words_frequency)
        self.global_vocab.add(words_set)
        self.words_docs.append( words_list )
           
         
    def get_vocab(self):      
        return self.global_vocab if not is_empty else "Empty"
            
    def get_two_gram_vocab(self):
        return self.global_two_gram_vocab if not is_empty else "Empty"
        
    def get_docs_vocab(self):
        return self.doc_vocabulary if not is_empty else "Empty"
        
    def get_docs_two_gram_vocab(self):
        return self.doc_two_gram_vocab if not is_empty else "Empty"
            
        
        
