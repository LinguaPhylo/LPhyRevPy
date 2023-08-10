from antlr4 import ParserRuleContext


class UnsupportedOperationException(Exception):

    def __init__(self, msg:str):
        super().__init__(msg)

class ParsingException(Exception):
#TODO add line number
    def __init__(self, msg: str, ctx: ParserRuleContext):
        super().__init__(msg + "\n" + ctx.start)
        #self.line_num = ctx.getToken()
        #self.character_num = ctx.



