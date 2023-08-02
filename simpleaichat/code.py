from pydantic import BaseModel, Field
from simpleaichat import AIChat
from uuid import uuid4
import orjson

params = {"temperature": 0.0}  
model = "gpt-3.5-turbo"

system_optimized = """Write a Python function based on the user input.

You must obey ALL the following rules:
- Only respond with the Python function.
- Never put in-line comments or docstrings in your code."""


ai_func = AIChat(console=False)

class write_python_function(BaseModel):
    """Writes a Python function based on the user input."""
    code: str = Field(description="Python code")
    efficient_code: str = Field(description="More efficient Python code than previously written")

def gen_code(question):
    id = uuid4()
    ai_func.new_session(id=id, system=system_optimized, params=params, model=model)
    response_structured = ai_func(question, id=id, output_schema=write_python_function)
    
    ai_func.delete_session(id=id)
    return response_structured

code = gen_code("is_palindrome")
# print(orjson.dumps(code, option=orjson.OPT_INDENT_2).decode())
print(code["efficient_code"])
print("\n\n")


code = gen_code("multiprocess hash")
print(code["efficient_code"])
print("\n\n")

code = gen_code("reverse string")
print(code["efficient_code"])
print("\n\n")
