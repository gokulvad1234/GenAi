import re
import string
import contractions
from textblob import TextBlob
import emoji

class TextNormalization:

    def __init__(self,data):
        self.data = data
        self.start()

    def start(self):
        print(
            "1.Removing Spaces\n2.Removing Special Character\n3.Removing Punctuations\n4.Correcting the words\n5.Expanding the words\n6.Convert to Lowercase"
        )
        choice = input("Do you want to clean data?").lower()
        if choice == "yes":
            self.converting_lower()
            self.expanding_words()
            self.correcting_the_words()
            self.removing_spaces()
            self.removing_punctuations()
            self.removing_emojis()
            return self.data
        else:
            return False
        
    def converting_lower(self):
        self.data = self.data.lower()

    def removing_spaces(self):
        self.data = re.sub(r'\s{2,}','',self.data)
    
    def removing_punctuations(self):
        var = string.punctuation
        self.data = re.sub(f'[{var}]',' ',self.data)

    def correcting_the_words(self):
        self.data = contractions.fix(self.data)

    def expanding_words(self):
        Obj_Textblob = TextBlob(self.data).correct()
        self.data = str(Obj_Textblob)
    
    def removing_emojis(self):
        self.data = emoji.replace_emoji(self.data,'>')
        

data = "I havv a smal gardn with beutiful flowrs.The wather is sunny, and the birds are singng.I am learnig about txt normalizaton and spell corection."
obj  = TextNormalization(data)
print(obj.data)