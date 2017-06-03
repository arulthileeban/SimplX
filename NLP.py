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
                '-':['decrement','subtract'],NLP.py
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
        elif lang == "Perl":
        	self.header="#!/usr/bin/perl\n"
        	self.footer=""
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

    def declare_var(self, vtype, vname, vlength):
        # code_con = Initial Code Contents
        code_con = ""
        if self.lang == "C++":
            # Initialising integers in C++
            if not vtype == "string":
                code_con = code_con + "\t" + vtype + " " + vname
            # Initialising strings in C++
            else:
                code_con += code_con + "\t" + "char" + " " + vname
            # Adding array length
            if(vlength > 1):
                code_con += "[" + str(vlength) + "]"
            # Adding default length of char array (string)
            if vtype == "string":
                code_con += "[50]"
            # Adding semicolon in case of C++
            code_con = code_con + ";"
        elif self.lang == "Python":
            if vlength > 1:
                code_con = code_con + vname + " = []\n"
        elif self.lang == "Perl":
        	if vlength > 1:
                code_con = code_con + "@"+vname + " = ();\n"


        self.content = self.content + code_con + "\n"

    def input_var(self, vtype, vname, vlength):
        # code_con = Initial Code Contents
        code_con = ""
        if self.lang == "C++":
            # Input integers in C++
            if not vtype == "string":
                # Input an array of integers in C++
                if vlength > 1:
                    code_con = code_con + "\t" + "for (int i =0;i<" + str(vlength) + ";i++)"
                    code_con = code_con + "\n\t{" + '\tcout<<"Enter number "<<i<<":";' + "\n\t\tcin>>" + vname + "[i];" + "\n\t}"
                # Input just one integer in C++
                else:
                    code_con = code_con + "\t" + 'cout<<"Enter number :";' + "\n\tcin>>" + vname + ";"
            # Input strings in C++
            else:
                # Input an array of strings/2D array of characters
                if vlength > 1:
                    code_con = code_con + "\t" + "for (int i =0;i<" + str(vlength) + ";i++)"
                    code_con = code_con + "\n\t{" + '\tcout<<"Enter string "<<i<<":";' + "\n\t\tcin>>" + vname + "[i];" + "\n\t}"
                # Input just one string
                else:
                    code_con = code_con + "\t" + 'cout<<"Enter string :";' + "\n\tcin>>" + vname + ";"
        elif self.lang == "Python":
            # Input integers
            if not vtype == "string":
                # Input a list of numbers
                if vlength > 1:
                    code_con = code_con + "for i in xrange(" + str(vlength) + ")"
                    code_con = code_con  + "\n\t" + vname + ".append(input('Enter number'+str(i)))" + "\n"
                # Input one number
                else:
                    code_con = code_con + vname+" = input('Enter number')"
            # Input strings
            else:
                # Input a list of strings
                if vlength > 1:
                    code_con = code_con + "for i in xrange(" + str(vlength) + ")"
                    code_con = code_con + "\n\t" + vname + ".append(raw_input('Enter string'+str(i)))" + "\n"
                # Input one string
                else:
                    code_con = code_con + vname+" = raw_input('Enter string')"
        elif self.lang == "Perl":
        	if vlength==1:
        		code_con += "$"+vname+" = <>;"
        	if vlength>1:
        		code_con += "$n="+str(vlength)+";\nwhile ( $n >0 ){\n"
        		code_con += "$val= <> ;\npush(@"+vname+",val);\n"
        		code_con += "$n = $n - 1;}"


        self.content = self.content + code_con + "\n"

    def print_var(self, vtype, vname, vlength):
        # code_con = Initial Code Contents
        code_con = ""
        if self.lang == "C++":
            # Printing an array in C++
            if vlength > 1:
                code_con = code_con + "\t" + "for (int i =0; i<" + str(vlength) + " ; i++)"
                code_con = code_con + "\n\t{" + '\tcout<<' + vname + '[i];' + "\n\t}"
            # Printing a single element in C++
            else:
                code_con = code_con + "\n cout<<" + vname + ";"
        elif self.lang == "Python":
            # Printing a list in Python
            if vlength > 1:
                code_con = code_con + "for i in xrange(" + str(vlength) + ")"
                code_con = code_con + "\n\tprint" + vname + "[i]" + "\n"
            # Printing a single element in Python
            else:
                code_con = code_con + "print " + vname
        elif self.lang == "Perl":
            code_con += "print "+vname+";\n"

        self.content = self.content + code_con + "\n"

    def smallest(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint small=99999;\n\tfor(int i=0;i<" + str(vlength) + ";i++)"
            func_code += "\n\t\tif(small>" + vname + "[i])\n\t\t\tsmall=" + vname + "[i];\n"
            func_code += "\tcout<<small;\n"
        elif self.lang == "Python":
        	func_code += "min("+vname+")\n"
        elif self.lang == "Perl":
			func_code += "my $min = 9999;\nfor ( @"+vname+" ) {\n$min = $_ if !$min || $_ < $min ;};\nprint $min;\n"


        self.content += func_code + "\n"

    def largest(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint great=-99999;\n\tfor(int i=0;i<" + str(vlength) + ";i++)"
            func_code += "\n\t\tif(great<" + vname + "[i])\n\t\t\tgreat=" + vname + "[i];\n"
            func_code += "\tcout<<great;\n"
        elif self.lang == "Python":
        	func_code += "print min("+vname+")\n"
        elif self.lang == "Perl":
			func_code += "my $max = -9999;\nfor ( @"+vname+" ) {\n$max = $_ if !$max || $_ > $max ;};\nprint $max;\n"

        self.content += func_code + "\n"

    def get_product(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint product=1;\n\tfor(int i=0;i<" + str(vlength) + ";i++)"
            func_code += "\n\t\tproduct*=" + vname + "[i];\n"
            func_code += "\tcout<<product;\n"
        elif self.lang == "Python":
			func_code += "product = 1\nfor i in "+vname+":\n"
			func_code += "\tproduct*=i\n"
			func_code += "print product\n"
        elif self.lang == "Perl":
        	func_code += "my $product = 1;\nfor ( @"+vname+" ) {\n$product *= $_;\n};\n"
        self.content += func_code + ";\n"

    def get_sum(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint sum=0;\n\tfor(int i=0;i<" + str(vlength) + ";i++)"
            func_code += "\n\t\tsum+=" + vname + "[i];\n"
            func_code += "\tcout<<sum;\n"
        elif self.lang == "Python":
			func_code += "sum = 0\nfor i in "+vname+":\n"
			func_code += "\tsum+=i\n"
			func_code += "print sum\n"
        elif self.lang == "Perl":
			func_code += "my $sum = 0;\nfor ( @"+vname+" ) {\n$sum += $_;\n};\n"
}

        self.content += func_code + "\n"

    # Adding Arithmetic operations
    def arithmetix(self, vname, intent, num):
        if num in self.vars:
            vname, num = num, vname
        func_code = ""
        func_code += "\t" + vname + " = " + vname + " " + intent + " " + num
        self.content += func_code + ";\n"
