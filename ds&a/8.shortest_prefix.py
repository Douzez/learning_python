"""
Shortest unique prefix.

Given a list of words, for each word find the shortest unique prefix. 
You can assume a word will not be a substring of another word 
(i.e. 'play' and 'playing' won't be in the same words list)

Example:
input:      ['joma', 'jack', 'john', 'teodore']
poutput:    ['jom', 'ja', 'joh', 't']

Use TRIEs usually when thinking in prefixes or strings 
A TRIE is basically a tree and for each children  theres a counter.
It helps to determine given these words how many words have we passed into certain letters so far
and we will be using these nodes as a references if we can use it as a unique prefix.

1. joma  2. jack 3. john   4. teodore
     -->   (NODE)
            /   \
         (j=3)  (t=1)
        /     \    \
      (o=2) (a=1)  (...)
     /   \       \  
  (m=0) (h=1)   (c=1)
   /      \       /
(a=1)    (n=1)  (k=0)

To get the unique prefix go through each Node in the TRIE, so keep going until you see a 1.

Time complexity: 1st you need to build the TRIE   ===> O(n)  --> Linear
    Because you have to go through all the words 

Space: O(n) need to go through all words to build the TRIE
"""


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node.children:
                curr_node.children[w] = Node()
            curr_node = curr_node.children[w]
            curr_node.count += 1
    
    def unique_pref(self, word):
        curr_node = self.root
        prefix = ''

        for w in word:
            if curr_node.count == 1:
                return prefix
            else:
                curr_node = curr_node.children[w]
                prefix += w
        
        return prefix

def get_unique_pref(words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    unique_pref = []
    for word in words:
        unique_pref.append(trie.unique_pref(word))
    
    return unique_pref

words = ['joma', 'jack', 'john', 'teodore']
print(get_unique_pref(words)) 
