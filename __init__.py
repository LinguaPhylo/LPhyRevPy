import sys, getopt
from antlr4 import *
from lphy.core.parser.DataModelLexer import DataModelLexer
from lphy.core.parser.DataModelParser import DataModelParser
from lphy.core.parser.DataModelVisitor import DataModelVisitor


def parse_args(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is : ', inputfile)
   print ('Output file is : ', outputfile)
   argsdict = {"in": inputfile, "out": "outputfile"}
   return argsdict


def main():
   argsdict = parse_args(sys.argv[1:])

   f = open(argsdict["in"], "r")
   # print lphy script
   print(f.read())

   # data =  InputStream(input(">>> "))
   # # lexer
   # lexer = MyGrammerLexer(data)
   # stream = CommonTokenStream(lexer)
   # # parser
   # parser = MyGrammerParser(stream)
   # tree = parser.expr()
   # # evaluator
   # visitor = MyVisitor()
   # output = visitor.visit(tree)
   # print(output)

if __name__ == "__main__":
    print ('Argument List:', str(sys.argv))

    main()

