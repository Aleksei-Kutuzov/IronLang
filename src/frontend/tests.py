from src.frontend.parse_input import parse_input
import unittest

class TestParser(unittest.TestCase):

    def test_parse_assign(self):
        input_code = """
        x = 42;
        y = 3.14;
        flag = true;
        ch = 'a';
        str = "hello";
        """
        parse_tree, parser = parse_input(input_code)
        self.assertEqual(parse_tree.toStringTree(recog=parser),
                         """(program (statement (assignment x = (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor 42))))))))) ;) (statement (assignment y = (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor 3.14))))))))) ;) (statement (assignment flag = (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor true))))))))) ;) (statement (assignment ch = (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor 'a'))))))))) ;) (statement (assignment str = (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor "hello"))))))))) ;))""",
                         "Assignments doesn't match")
    def test_parse_if(self):
        input_code = """
        if (x > 10 && y < 20){}
        """
        parse_tree, parser = parse_input(input_code)
        self.assertEqual(parse_tree.toStringTree(recog=parser),
                         """(program (statement (if_statement if ( (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor x))) > (additiveExpression (multiplicativeExpression (factor 10))))) && (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor y))) < (additiveExpression (multiplicativeExpression (factor 20)))))))) ) (block { }))))""",
                         "Ifs doesn't match")
    def test_parse_function_statement(self):
        input_code = """
        print("");
        """
        parse_tree, parser = parse_input(input_code)
        print(parse_tree.toStringTree(recog=parser))
        self.assertEqual(parse_tree.toStringTree(recog=parser),
                         """(program (statement (function_statement print ( (expression (logicalOrExpression (logicalAndExpression (equalityExpression (relationalExpression (additiveExpression (multiplicativeExpression (factor "")))))))) )) ;))""",
                         "Function statements doesn't match")

if __name__ == '__main__':
    unittest.main()

input_code = """
x = 42;
y = 3.14;
flag = true;
ch = 'a';
str = "hello";
if (x > 10 && y < 20){}
print("");
"""

# Разбираем входной код
parse_tree, parser = parse_input(input_code)

# Выводим дерево разбора в текстовом виде
print(parse_tree.toStringTree(recog=parser))

