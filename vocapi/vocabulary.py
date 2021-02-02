from typing import List, Dict, Tuple, Any, Union, Set
import re
import copy
class Vocabulary:
    def __init__(self):
        self.global_vocab = set()
        self.global_freq = dict()
        self.global_two_gram_vocab = set()
        self.doc_vocabulary = list(set())
        self.doc_two_gram_vocab = list(set())
        self.is_empty = True
        self.words_docs = list(list())
        self.docs_words_frequency_list = list(list())
        self.docs_words_frequency = list(dict())
        
    def add_doc(self, text: str):
        all_words_list = re.findall(r'\w+', text)
        all_words_list = [word.lower() for word in all_words_list]
        words_set = set(all_words_list)
        words_list = list(words_set)
        words_frequency = dict.fromkeys(words_list,0)
        update_frequency = copy.copy(words_frequency)
        update_frequency.update(self.global_freq)
        for w in words_frequency:
            count = all_words_list.count(w)
            update_frequency[w] += count
            words_frequency[w] += count
        self.docs_words_frequency.append(words_frequency)
        self.global_vocab.update(words_set)
        self.words_docs.append( words_list )
        self.is_empty = False
        self.global_freq.update(update_frequency)
           
         
    def get_vocab(self):      
        return sorted(self.global_freq.items()) if not self.is_empty else "Empty"
            
    def get_two_gram_vocab(self):
        return self.global_two_gram_vocab if not self.is_empty else "Empty"
        
    def get_docs_vocab(self):
        return self.words_docs if not self.is_empty else "Empty"
        
    def get_docs_two_gram_vocab(self):
        return self.doc_two_gram_vocab if not self.is_empty else "Empty"
            
        
        
