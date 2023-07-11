import ast
import astor

# example Python parse tree
python_tree = ast.Module(
    body=[ast.Call(
        func=ast.Name(id="OptionMenu", ctx=ast.Load()),
        args=[
            ast.Str(s="Select a color"),
            ast.List(
                elts=[
                    ast.Call(
                        func=ast.Name(id="Option", ctx=ast.Load()),
                        args=[ast.Str(s="Option 1"), ast.Str(s="red")],
                        keywords=[]
                    ),
                    ast.Call(
                        func=ast.Name(id="Option", ctx=ast.Load()),
                        args=[ast.Str(s="Option 2"), ast.Str(s="green")],
                        keywords=[]
                    ),
                    ast.Call(
                        func=ast.Name(id="Option", ctx=ast.Load()),
                        args=[ast.Str(s="Option 3"), ast.Str(s="blue")],
                        keywords=[]
                    ),
                    ast.Call(
                        func=ast.Name(id="Option", ctx=ast.Load()),
                        args=[ast.Str(s="Option 4"), ast.Str(s="yellow")],
                        keywords=[]
                    )
                ],
                ctx=ast.Load()
            )
        ],
        keywords=[]
    )]
)

# generate Python code from the parse tree
python_code = astor.to_source(python_tree)

# print the Python code
print(python_code)