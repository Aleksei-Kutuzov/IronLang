# Generated from C:/Users/Admin/PycharmProjects/IronLang/src/frontend/antlr_part/IronLang.4g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IronLangParser import IronLangParser
else:
    from IronLangParser import IronLangParser

# This class defines a complete generic visitor for a parse tree produced by IronLangParser.

class IronLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IronLangParser#program.
    def visitProgram(self, ctx:IronLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#statement.
    def visitStatement(self, ctx:IronLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#if_statement.
    def visitIf_statement(self, ctx:IronLangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#block.
    def visitBlock(self, ctx:IronLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#assignment.
    def visitAssignment(self, ctx:IronLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#function_statement.
    def visitFunction_statement(self, ctx:IronLangParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#expression.
    def visitExpression(self, ctx:IronLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:IronLangParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:IronLangParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#equalityExpression.
    def visitEqualityExpression(self, ctx:IronLangParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#relationalExpression.
    def visitRelationalExpression(self, ctx:IronLangParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:IronLangParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:IronLangParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IronLangParser#factor.
    def visitFactor(self, ctx:IronLangParser.FactorContext):
        return self.visitChildren(ctx)



del IronLangParser