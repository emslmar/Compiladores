from antlr4 import *
from antlr.coolLexer import coolLexer
from antlr.coolParser import coolParser
from os import getcwd

from cool.semantic3.listeners.basicSemanticCheck import basicSemanticListener
from cool.semantic3.listeners.featuresBuilder import featuresBuilder
from cool.semantic3.listeners.structureBuilder import structureBuilder
from listeners.semantic import SemanticListener

PATH=getcwd()

def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()

    walker.walk(basicSemanticListener(), tree)

    walker.walk(structureBuilder(), tree)  # build the allClasses dict, sets inheritance

    walker.walk(featuresBuilder(), tree)  # add feature methods and attributes

    walker.walk(SemanticListener(), tree)


def dummy():
    raise SystemExit(1)


if __name__ == '__main__':
    compile('../resources/semantic/input/trickyatdispatch2.cool')
