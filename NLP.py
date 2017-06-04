from word2num import WordsToNumbers
import spacy


class CodeSpeak():
    def __init__(self, lang):
        self.nlp = spacy.load('en')
        # vars - Dictionary of Variables
        self.wtn = WordsToNumbers()
        self.vars = {}
        self.program = []
        self.prog_count = -1
        # Adding keywords
        self.entities = {
            'input': ['accept', 'get', 'read', 'input', 'fetch'],
            'output': ['print', 'output', 'display'],
            'mem': ['store', 'save'],
            'variabledest': ['into', 'to'],
            'numbers': ['numbers', 'nums', 'integer'],
            'string': ['string'],
            'sum': ['sum', 'summation'],
            'product': ['product'],
            '+': ['add', 'increment'],
            '*': ['multiply'],
            '-': ['decrement', 'subtract'],
            '/': ['divide'],
            '>': ['bigger', 'larger', 'greater'],
            '<': ['smaller', 'lesser', 'shorter'],
            '=': ['equal', 'same']
        }

        self.entsets = {}
        self.lang = lang

        # Assigning Header and Footer depending on Language
        if lang == "C++":
            self.header = "#include<iostream.h>\nusing namespace std;\nint main(){\n"
            self.footer = "return 0;}"
        elif lang == "Python":
            self.footer = self.header = ""
        elif lang == "Perl":
            self.header = "#!/usr/bin/perl\n"
            self.footer = ""
        # Wiping out and initialising content
        self.content = ""

        # Generating entsets from entities
        for i in self.entities:
            self.entsets[i] = set(
                [self.nlp(unicode(w))[0].lemma for w in self.entities[i]])

    # Clear Code Content and Variables
    def wipeout(self):
        self.content = ""
        self.vars = {}
        self.program = []
        self.prog_count = -1


    # Return Code
    def get_code(self):
        return self.header + self.content + self.footer

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
                code_con = code_con + "@" + vname + " = ();\n"
        self.content = self.content + code_con + "\n"

    def input_var(self, vtype, vname, vlength):
        # code_con = Initial Code Contents
        code_con = ""
        if self.lang == "C++":
            # Input integers in C++
            if not vtype == "string":
                # Input an array of integers in C++
                if vlength > 1:
                    code_con = code_con + "\t" + \
                        "for (int i =0;i<" + str(vlength) + ";i++)"
                    code_con = code_con + \
                        "\n\t{" + '\tcout<<"Enter number "<<i<<":";' + \
                        "\n\t\tcin>>" + vname + "[i];" + "\n\t}"
                # Input just one integer in C++
                else:
                    code_con = code_con + "\t" + 'cout<<"Enter number :";' + "\n\tcin>>" + vname + ";"
            # Input strings in C++
            else:
                # Input an array of strings/2D array of characters
                if vlength > 1:
                    code_con = code_con + "\t" + \
                        "for (int i =0;i<" + str(vlength) + ";i++)"
                    code_con = code_con + \
                        "\n\t{" + '\tcout<<"Enter string "<<i<<":";' + \
                        "\n\t\tcin>>" + vname + "[i];" + "\n\t}"
                # Input just one string
                else:
                    code_con = code_con + "\t" + 'cout<<"Enter string :";' + "\n\tcin>>" + vname + ";"
        elif self.lang == "Python":
            # Input integers
            if not vtype == "string":
                # Input a list of numbers
                if vlength > 1:
                    code_con = code_con + \
                        "for i in xrange(" + str(vlength) + ")"
                    code_con = code_con + "\n\t" + vname + \
                        ".append(input('Enter number'+str(i)))" + "\n"
                # Input one number
                else:
                    code_con = code_con + vname + " = input('Enter number')"
            # Input strings
            else:
                # Input a list of strings
                if vlength > 1:
                    code_con = code_con + \
                        "for i in xrange(" + str(vlength) + ")"
                    code_con = code_con + "\n\t" + vname + \
                        ".append(raw_input('Enter string'+str(i)))" + "\n"
                # Input one string
                else:
                    code_con = code_con + vname + \
                        " = raw_input('Enter string')"
        elif self.lang == "Perl":
            if vlength == 1:
                code_con += "$" + vname + " = <>;"
            if vlength > 1:
                code_con += "$n=" + str(vlength) + ";\nwhile ( $n >0 ){\n"
                code_con += "$val= <> ;\npush(@" + vname + ",val);\n"
                code_con += "$n = $n - 1;}"

        self.content = self.content + code_con + "\n"

    def print_var(self, vtype, vname, vlength):
        # code_con = Initial Code Contents
        code_con = ""
        if self.lang == "C++":
            # Printing an array in C++
            if vlength > 1:
                code_con = code_con + "\t" + \
                    "for (int i =0; i<" + str(vlength) + " ; i++)"
                code_con = code_con + \
                    "\n\t{" + '\tcout<<' + vname + '[i];' + "\n\t}"
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
            code_con += "print " + vname + ";\n"

        self.content = self.content + code_con + "\n"

    def smallest(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint small=99999;\n\tfor(int i=0;i<" + \
                str(vlength) + ";i++)"
            func_code += "\n\t\tif(small>" + vname + \
                "[i])\n\t\t\tsmall=" + vname + "[i];\n"
            func_code += "\tcout<<small;\n"
        elif self.lang == "Python":
            func_code += "min(" + vname + ")\n"
        elif self.lang == "Perl":
            func_code += "my $min = 9999;\nfor ( @" + vname + \
                " ) {\n$min = $_ if !$min || $_ < $min ;};\nprint $min;\n"

        self.content += func_code + "\n"

    def largest(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint great=-99999;\n\tfor(int i=0;i<" + \
                str(vlength) + ";i++)"
            func_code += "\n\t\tif(great<" + vname + \
                "[i])\n\t\t\tgreat=" + vname + "[i];\n"
            func_code += "\tcout<<great;\n"
        elif self.lang == "Python":
            func_code += "print min(" + vname + ")\n"
        elif self.lang == "Perl":
            func_code += "my $max = -9999;\nfor ( @" + vname + \
                " ) {\n$max = $_ if !$max || $_ > $max ;};\nprint $max;\n"

        self.content += func_code + "\n"

    def get_product(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint product=1;\n\tfor(int i=0;i<" + \
                str(vlength) + ";i++)"
            func_code += "\n\t\tproduct*=" + vname + "[i];\n"
            func_code += "\tcout<<product;\n"
        elif self.lang == "Python":
            func_code += "product = 1\nfor i in " + vname + ":\n"
            func_code += "\tproduct*=i\n"
            func_code += "print product\n"
        elif self.lang == "Perl":
            func_code += "my $product = 1;\nfor ( @" + \
                vname + " ) {\n$product *= $_;\n};\n"
        self.content += func_code + ";\n"

    def get_sum(self, vtype, vname, vlength):
        # func_code = Initial Code Contents
        func_code = ""
        if self.lang == "C++":
            func_code += "\tint sum=0;\n\tfor(int i=0;i<" + \
                str(vlength) + ";i++)"
            func_code += "\n\t\tsum+=" + vname + "[i];\n"
            func_code += "\tcout<<sum;\n"
        elif self.lang == "Python":
            func_code += "sum = 0\nfor i in " + vname + ":\n"
            func_code += "\tsum+=i\n"
            func_code += "print sum\n"
        elif self.lang == "Perl":
            func_code += "my $sum = 0;\nfor ( @" + \
                vname + " ) {\n$sum += $_;\n};\n"

        self.content += func_code + "\n"

    def functions(self, func, vname, vtype, vlength):
        func_code = ""
        if self.lang == "C++":
            if func == "sort":
                self.header = "#include<algorithm.h>\n" + self.header
                func_code += "sorted(" + vname + "," + \
                    vname + "+" + str(vlength) + ");"
            if func == "sqrt":
                self.header = "#include<math.h>\n" + self.header
                func_code += "cout << sqrt(" + vname + ");"
            if func == "log":
                self.header = "#include<math.h>\n" + self.header
                func_code += "cout << log(" + vname + ");"
        if self.lang == "Python":
            if func == "sort":
                func_code += "print sorted(" + vname + \
                    "," + vname + "+" + str(vlength) + ")"
            if func == "sqrt":
                self.header = "import math" + self.header
                func_code += "print math.sqrt(" + vname + ")"
            if func == "log":
                self.header = "import math" + self.header
                func_code += "print math.log(" + vname + ")"
        if self.lang == "Perl":
            if func == "sort":
                func_code += "print sort @" + vname + ";"
            if func == "sqrt":
                func_code += "print sqrt @" + vname + ";"
            if func == "log":
                func_code += "print log @" + vname + ";"

    # Adding Arithmetic operations
    def arithmetix(self, vname, intent, num):
        if num in self.vars:
            vname, num = num, vname
        func_code = ""
        func_code += "\t" + vname + " = " + vname + " " + intent + " " + num
        self.content += func_code + ";\n"

    '''
    ---------------------------------------------------------------------------------------
                                STAY AWAY BEYOND THIS
    ---------------------------------------------------------------------------------------
    '''

    def comment(self, sent):
        if self.lang == "C++":
            self.content += "\n//" + sent + "\n"
        elif self.lang == "Python":
            self.content += "\n#" + sent + "\n"

    def init_block(self):
        func_code = "\t{"
        self.content += func_code + "\n"

    def end_block(self):
        func_code = "\t}"
        self.content += func_code + "\n"

    def add_else(self):
        func_code = "\telse"
        self.content += func_code + "\n"

    def add_condition(self, cond):
        doc = self.nlp(unicode(cond))
        var = doc[0]
        is_word = doc[1]
        comp = list(is_word.rights)[0]
        comp_var = comp.right_edge
        for i in ['>', '<', '==']:
            if comp.lemma in self.entsets[i]:
                comp_symbol = i
                break
        vname = var.text
        func_code = ""
        func_code += "\tif ( " + vname + " " + \
            comp_symbol + " " + comp_var.text + " )"
        self.content += func_code + "\n"

    vstack = []

    def blockproc(self, query):
        if query.startswith("if"):
            statement = query.split("if ")[1]
            condition, solution = statement.split(" then ")
            if not solution:
                print "Solution not Found"
            if " else " in solution:
                pos, neg = solution.split(" else ")
            condition = condition.strip()
            pos = pos.strip().split(" and ")
            neg = neg.strip().split(" and ")
            print condition, pos, neg
            if neg:
                status = "false"
            else:
                status = "true"
            self.program.append({
                "type": "condition",
                "condition": condition,
                "true": pos,
                "false": neg,
                "status": status
            })
            self.prog_count += 1
        elif query.startswith("also ") or query.startswith("and "):
            if query.startswith("also"):
                statement = query.split("also ")[1]
            else:
                statement = query.split("and ")[1]
            curr_block = self.program[self.prog_count]
            if curr_block["type"] == "condition":
                if curr_block["status"] == "false":
                    self.program[self.prog_count]["false"].append(statement)
                else:
                    self.program[self.prog_count]["true"].append(statement)
            else:
                print "Also/And is out of condition. Adding it to program without Also/And"
                self.blockproc(statement)
        else:
            self.program.append({
                "type": "normal",
                "statement": query
            })
            self.prog_count += 1

    def assemble(self):
        for block in self.program:
            print block
            if block["type"] == "normal":
                self.proc(block["statement"])
            elif block["type"] == "condition":
                self.add_condition(block["condition"])
                self.init_block()
                for statement in block["true"]:
                    print statement
                    self.proc(statement)
                self.end_block()
                self.add_else()
                self.init_block()
                for statement in block["false"]:
                    self.proc(statement)
                self.end_block()

    def proc(self, query):
        print self.vars
        doc = self.nlp(u'You must ' + unicode(query))
        varname = 'temp'
        vtype = 'int'
        count = 1
        root = mod = None
        sent_root = [w for w in doc if w.head is w][0]
        object_var = list(sent_root.rights)[0]
        doc[object_var.left_edge.i: object_var.i + 1].merge()
        intent = None
        for i in ['input', 'output', '+', '*', '/', '-']:
            if sent_root.lemma in self.entsets[i]:
                intent = i

        print 'Intent found :', intent

        if intent == 'input':
            w = sent_root
            var = list(w.rights)[0]
            print w, w.lemma, '---', w.dep_, var
            num, vtype = self.nlp(unicode(var.text))
            print num, vtype
            try:
                count = int(num.text)
            except ValueError:
                if num.text == 'a':
                    count = 1
                else:
                    count = self.wtn.parse(num.text)
            print count
            if vtype.lemma in self.entsets['numbers']:
                vtype = 'int'
            else:
                vtype = 'string'
            for w in doc:
                if w.lemma in self.entsets['variabledest']:
                    varname = list(w.rights)[0].text
            self.vars[str(varname)] = {'type': vtype, 'length': count}
            print 'Vars is set'
            print self.vars[varname]
            self.declare_var(vtype, varname, count)
            self.input_var(vtype, varname, count)

        elif intent == "output":
            w = sent_root
            # x - first right of x ("the sum" in "print the sum of X")
            x = list(w.rights)[0]
            # Name of variable being referenced ("X" in "print the sum of X")
            varname = x.right_edge
            # Get root of X. "Number" in "the smallest number". "Sum" in "the
            # sum"
            root = [w for w in self.nlp(x.text) if w.head is w][0]
            # print root,list(root.lefts)
            # mod - "Smallest/largest". None for sum/product
            mod = None
            for i in root.lefts:
                if i.dep == 398:
                    mod = i
            print mod, root, '---', varname
            print 'varname =', varname
            var_record = self.vars.get(str(varname.text), None)
            if var_record:
                print 'varname is =', self.vars[str(varname.text)]
                vtype = var_record['type']
                count = var_record['length']
                if mod == None and root.text == varname.text:
                    self.print_var(vtype, varname.text, count)
                if vtype == 'int' and count > 1:
                    if root.lemma in self.entsets['numbers']:
                        if mod.lemma == self.nlp(u'smallest')[0].lemma:
                            self.smallest(vtype, str(varname.text), count)
                        if mod.lemma == self.nlp(u'largest')[0].lemma:
                            self.largest(vtype, str(varname.text), count)
                    elif root.lemma in self.entsets['product']:
                        self.get_product(vtype, str(varname.text), count)
                    elif root.lemma in self.entsets['sum']:
                        self.get_sum(vtype, str(varname.text), count)
                else:
                    if count < 2:
                        self.comment(varname.text + " is not an array")
                    else:
                        self.comment(varname.text + " is not of type int")
            else:
                self.comment(varname + " does not exist")

        elif intent in ['+', '*', '/', '-']:
            w = sent_root
            var = list(w.rights)[0]
            var_record = self.vars.get(str(var.text), None)
            if var_record:
                vtype = var_record['type']
                count = var_record['length']
                if vtype == "int" and count == 1:
                    magnitude = var.right_edge
                    if magnitude.i == var.i:
                        magnitude = '1'
                    else:
                        magnitude = magnitude.text
                    self.arithmetix(var.text, intent, magnitude)
                else:
                    if count > 1:
                        self.comment(var.text + " is an array. Cannot be operated on")
                    else:
                        self.comment(var.text + " is not of type int")
            else:
                self.comment(var.text + " does not exist")
        print self.content

'''
from NLP import CodeSpeak
from pprint import pprint
c= CodeSpeak("C++")
c.blockproc("Input 10 numbers into X")
c.blockproc("Print the sum of X")
c.blockproc("if X is greater than 10 then print X else print the product of X")
c.blockproc("also increment X")
pprint(c.program)
c.assemble()
print c.get_code()
'''
