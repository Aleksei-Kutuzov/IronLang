# Generated from C:/Users/Admin/PycharmProjects/IronLang/src/frontend/antlr_part/IronLang.4g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IronLangParser import IronLangParser
else:
    from IronLangParser import IronLangParser

# This class defines a complete listener for a parse tree produced by IronLangParser.
class IronLangListener(ParseTreeListener):

    # Enter a parse tree produced by IronLangParser#program.
    def enterProgram(self, ctx:IronLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by IronLangParser#program.
    def exitProgram(self, ctx:IronLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by IronLangParser#statement.
    def enterStatement(self, ctx:IronLangParser.StatementContext):
        pass

    # Exit a parse tree produced by IronLangParser#statement.
    def exitStatement(self, ctx:IronLangParser.StatementContext):
        pass


    # Enter a parse tree produced by IronLangParser#if_statement.
    def enterIf_statement(self, ctx:IronLangParser.If_statementContext):
        pass

    # Exit a parse tree produced by IronLangParser#if_statement.
    def exitIf_statement(self, ctx:IronLangParser.If_statementContext):
        pass


    # Enter a parse tree produced by IronLangParser#block.
    def enterBlock(self, ctx:IronLangParser.BlockContext):
        pass

    # Exit a parse tree produced by IronLangParser#block.
    def exitBlock(self, ctx:IronLangParser.BlockContext):
        pass


    # Enter a parse tree produced by IronLangParser#assignment.
    def enterAssignment(self, ctx:IronLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IronLangParser#assignment.
    def exitAssignment(self, ctx:IronLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IronLangParser#function_statement.
    def enterFunction_statement(self, ctx:IronLangParser.Function_statementContext):
        pass

    # Exit a parse tree produced by IronLangParser#function_statement.
    def exitFunction_statement(self, ctx:IronLangParser.Function_statementContext):
        pass


    # Enter a parse tree produced by IronLangParser#expression.
    def enterExpression(self, ctx:IronLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#expression.
    def exitExpression(self, ctx:IronLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:IronLangParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:IronLangParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:IronLangParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:IronLangParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#equalityExpression.
    def enterEqualityExpression(self, ctx:IronLangParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#equalityExpression.
    def exitEqualityExpression(self, ctx:IronLangParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#relationalExpression.
    def enterRelationalExpression(self, ctx:IronLangParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#relationalExpression.
    def exitRelationalExpression(self, ctx:IronLangParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:IronLangParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:IronLangParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:IronLangParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by IronLangParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:IronLangParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by IronLangParser#factor.
    def enterFactor(self, ctx:IronLangParser.FactorContext):
        pass

    # Exit a parse tree produced by IronLangParser#factor.
    def exitFactor(self, ctx:IronLangParser.FactorContext):
        pass



del IronLangParser