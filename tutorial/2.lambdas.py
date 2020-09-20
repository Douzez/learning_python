"""
Small anonymous functions can be created with the lambda keyword.
This function returns the sum of its two arguments: lambda a, b: a+b.
* Lambda functions can used wherever function objects are required.
* They are syntactically restricted to a single expression.
* Semantically, they are just syntactic sugar for a normal function definition.
* They can reference variables from the containing scope.
"""

# Lambda Function that return a function
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))     # 42
print(f(1))     # 43
print(f(10))    # 52
