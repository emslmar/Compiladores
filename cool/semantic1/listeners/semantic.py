from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser


class SemanticListener(coolListener):
    def __init__(self):
        self.main = False

    def exitAttribute(self, ctx:coolParser.AttributeContext):
        if ctx.ID().getText() == 'self':
            raise BadAttributeName();

    def exitClass(self, ctx:coolParser.ClassContext):
        if len(ctx.TYPE()) == 2:
            if ctx.TYPE(1).getText() == 'Bool':
                raise InvalidInheritance();

