# LLM demo

## Setup
add:
```sh
export OPENAI_API_KEY="<your key>"

export REPLICATE_API_TOKEN="<your key>"
```
to your `~/.bashrc` or `~/.zshrc`, and run `source ~/.bashrc` or `source ~/.zshrc` in the terminal

https://replicate.com/blog/run-llama-2-with-an-api

## Result
**gpt-3.5-turbo** model:

```sh
python3 code.py

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True



import hashlib
import multiprocessing


def hash_string(string):
    return hashlib.sha256(string.encode()).hexdigest()


def multiprocess_hash(strings):
    with multiprocessing.Pool() as pool:
        hashes = pool.map(hash_string, strings)
    return hashes



def reverse_string(s):
    return ''.join(reversed(s))
```

**llama 2** model
```sh
 Sure! Here's a Python function for checking whether a given string is a palindrome or not:

def is_palindrome(str):
   """
   Returns True if the given string is a palindrome, False otherwise.
   
   A palindrome is a string that reads the same backward as forward.
   """
   return str == str[::-1]

I hope this helps! Let me know if you have any questions or need further clarification.



Traceback (most recent call last):
  File "/Users/flyq/workspace/github/flyq/py/replicate_llama2.py", line 28, in <module>
    code = gen_code("multiprocess hash")
  File "/Users/flyq/workspace/github/flyq/py/replicate_llama2.py", line 18, in gen_code
    for i in output:
  File "/opt/homebrew/lib/python3.10/site-packages/replicate/prediction.py", line 42, in output_iterator
    raise ModelError(self.error)
replicate.exceptions.ModelError: CUDA error: an illegal memory access was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```