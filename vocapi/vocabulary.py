from typing import List, Dict, Tuple, Any, Union, Set
import re

class Vocabulary:
    def __init__(self):
        self.global_vocab = set()
        self.global_two_gram_vocab = set()
        self.doc_vocabulary = list(set())
        self.doc_two_gram_vocab = list(set())
        self.is_empty = True
        self.words_docs = list(list())
        self.docs_words_frequency = list(list())
        
    def add_doc(self, text: str):
        all_words_list = re.findall(r'\w+', text)
        words_set = set(all_words_list)
        words_list = list(words_set)
        words_frequency = list()
        for w in words_list:
            count = words_list.count(w)
            words_frequency.append(count)
        self.docs_words_frequency.append(words_frequency)
        self.global_vocab.update(words_set)
        self.words_docs.append( words_list )
        self.is_empty = False

           
         
    def get_vocab(self):      
        return self.global_vocab if not self.is_empty else "Empty"
            
    def get_two_gram_vocab(self):
        return self.global_two_gram_vocab if not self.is_empty else "Empty"
        
    def get_docs_vocab(self):
        return self.words_docs if not self.is_empty else "Empty"
        
    def get_docs_two_gram_vocab(self):
        return self.doc_two_gram_vocab if not self.is_empty else "Empty"
            
        
        
