from pycparser import c_parser, c_ast, parse_file

class FuncDefVisitor(c_ast.NodeVisitor):

    def __init__(self, func_names, excludes=list()):
        self.func_names = func_names
        self.excludes = excludes

    def visit_FuncDef(self, node):
        if (node.decl.name not in self.excludes):
            self.func_names.add(node.decl.name)

class FuncCallVisitor(c_ast.NodeVisitor):

    def __init__(self, func_names, excludes=list()):
        self.func_names = func_names
        self.excludes = excludes

    def visit_FuncCall(self, node):
        if (node.name.name not in self.excludes):
            self.func_names.add(node.name.name)

class Parser(object):

    def __init__(self, file_name, def_excludes=list(), call_excludes=list()):
        ast = parse_file(file_name,
        use_cpp=True,
        cpp_args=r'-Iutils/fake_libc_include')

        self.func_names = set()

        fdv = FuncDefVisitor(self.func_names, def_excludes)
        fdv.visit(ast)

        fcv = FuncCallVisitor(self.func_names, call_excludes)
        fcv.visit(ast)