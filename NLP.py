from word2num import WordsToNumbers
import spacy
class CodeSpeak():
    def __init__(self,lang):
        self.nlp = spacy.load('en')
        # vars - Dictionary of Variables
        self.wtn = WordsToNumbers()
        self.vars = {}
        # Adding keywords
        self.entities = {
                'input':['accept','get','read','input','fetch'],
                'output':['print','output','display'],
                'mem':['store','save'],
                'variabledest':['into','to'],
                'numbers':['numbers','nums','integer'],
                'string':['string'],
                'sum':['sum','summation'],
                'product':['product'],
                '+':['add','increment'],
                '*':['multiply'],
                '-':['decrement','subtract'],
                '/':['divide'],
                '>':['bigger','larger','greater'],
                '<':['smaller','lesser','shorter'],
                '=':['equal','same']
        }

        self.entsets = {}
        self.lang=lang

        # Assigning Header and Footer depending on Language
        if lang == "C++":
            self.header="#include<iostream.h>\nusing namespace std;\nint main(){\n"
            self.footer="return 0;}"
        elif lang == "Python":
            self.footer=self.header=""
        # Wiping out and initialising content
        self.content = ""

        # Generating entsets from entities
        for i in self.entities:
            self.entsets[i]=set([self.nlp(unicode(w))[0].lemma for w in self.entities[i]])

    # Clear Code Content and Variables
    def wipeout(self):
        self.content = ""
        self.vars = {}

    # Return Code
    def get_code(self):
        return self.header+self.content+self.footer
