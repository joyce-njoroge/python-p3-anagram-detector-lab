# your code goes here!
class Anagram:
   def __init__(self, word):
      self.word = word.lower()
      

   def match(self, words):
       match = []
       for word in words:
           if len(word) == len(self.word) and word.lower() != self.word:
                if sorted(word.lower()) == sorted(self.word):
                   match.append(word)
       return match   
            
word = Anagram("Word")  
word = (['enlists', 'google', 'inlets', 'banana'])    