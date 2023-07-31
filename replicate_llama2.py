import replicate

system_optimized = """Write a Python function based on the user input.

You must obey ALL the following rules:
- Only respond with the Python function.
- Never put in-line comments or docstrings in your code."""

def gen_code(question):
    output = replicate.run(
        "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": system_optimized + "\n user's question is " + question}
    )

    # The replicate/llama-2-70b-chat model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    out = ""
    for i in output:
        out += i
    return out


code = gen_code("is_palindrome")
print(code)
print("\n\n")


code = gen_code("multiprocess hash")
print(code)
print("\n\n")

