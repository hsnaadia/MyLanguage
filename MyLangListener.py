# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MyLangParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MyLangParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MyLangParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MyLangParser#printStatement.
    def enterPrintStatement(self, ctx:MyLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#printStatement.
    def exitPrintStatement(self, ctx:MyLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileLimitStatement.
    def enterWhileLimitStatement(self, ctx:MyLangParser.WhileLimitStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileLimitStatement.
    def exitWhileLimitStatement(self, ctx:MyLangParser.WhileLimitStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileStatement.
    def enterWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileStatement.
    def exitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:MyLangParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:MyLangParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#switchStatement.
    def enterSwitchStatement(self, ctx:MyLangParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#switchStatement.
    def exitSwitchStatement(self, ctx:MyLangParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#forEachStatement.
    def enterForEachStatement(self, ctx:MyLangParser.ForEachStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#forEachStatement.
    def exitForEachStatement(self, ctx:MyLangParser.ForEachStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#forRangeStatement.
    def enterForRangeStatement(self, ctx:MyLangParser.ForRangeStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#forRangeStatement.
    def exitForRangeStatement(self, ctx:MyLangParser.ForRangeStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#forStepStatement.
    def enterForStepStatement(self, ctx:MyLangParser.ForStepStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#forStepStatement.
    def exitForStepStatement(self, ctx:MyLangParser.ForStepStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#forLoopStatement.
    def enterForLoopStatement(self, ctx:MyLangParser.ForLoopStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#forLoopStatement.
    def exitForLoopStatement(self, ctx:MyLangParser.ForLoopStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#unlessStatement.
    def enterUnlessStatement(self, ctx:MyLangParser.UnlessStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#unlessStatement.
    def exitUnlessStatement(self, ctx:MyLangParser.UnlessStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:MyLangParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:MyLangParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#comment.
    def enterComment(self, ctx:MyLangParser.CommentContext):
        pass

    # Exit a parse tree produced by MyLangParser#comment.
    def exitComment(self, ctx:MyLangParser.CommentContext):
        pass


    # Enter a parse tree produced by MyLangParser#multilineComment.
    def enterMultilineComment(self, ctx:MyLangParser.MultilineCommentContext):
        pass

    # Exit a parse tree produced by MyLangParser#multilineComment.
    def exitMultilineComment(self, ctx:MyLangParser.MultilineCommentContext):
        pass


    # Enter a parse tree produced by MyLangParser#iterable.
    def enterIterable(self, ctx:MyLangParser.IterableContext):
        pass

    # Exit a parse tree produced by MyLangParser#iterable.
    def exitIterable(self, ctx:MyLangParser.IterableContext):
        pass


    # Enter a parse tree produced by MyLangParser#array.
    def enterArray(self, ctx:MyLangParser.ArrayContext):
        pass

    # Exit a parse tree produced by MyLangParser#array.
    def exitArray(self, ctx:MyLangParser.ArrayContext):
        pass


    # Enter a parse tree produced by MyLangParser#object.
    def enterObject(self, ctx:MyLangParser.ObjectContext):
        pass

    # Exit a parse tree produced by MyLangParser#object.
    def exitObject(self, ctx:MyLangParser.ObjectContext):
        pass


    # Enter a parse tree produced by MyLangParser#pair.
    def enterPair(self, ctx:MyLangParser.PairContext):
        pass

    # Exit a parse tree produced by MyLangParser#pair.
    def exitPair(self, ctx:MyLangParser.PairContext):
        pass


    # Enter a parse tree produced by MyLangParser#condition.
    def enterCondition(self, ctx:MyLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by MyLangParser#condition.
    def exitCondition(self, ctx:MyLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by MyLangParser#expression.
    def enterExpression(self, ctx:MyLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLangParser#expression.
    def exitExpression(self, ctx:MyLangParser.ExpressionContext):
        pass



del MyLangParser