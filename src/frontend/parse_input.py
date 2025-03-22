from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from src.frontend.antlr_part import IronLangLexer, IronLangParser


def parse_input(input_code: str):
    input_stream = InputStream(input_code)

    lexer = IronLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = IronLangParser(stream)
    tree = parser.program()  # Начинаем разбор с правила 'program'

    return tree, parser