import math
import mod 
import requests
# importing the module with alias name
import numpy as np

# import specific function from the module
from math import sqrt, pi

# import everything from the module
from math import *

# import everythin from the module not recommended

# Case 1: 'import math' (Lazy-loading)
import math  # Only loads the module object
# No extra memory used until `math.sqrt()` is called.

# Case 2: 'from math import *' (Eager-loading)
from math import *  # Loads ALL names (pi, sin, cos, sqrt, ...)
# Memory usage increases even if you never use `pi` or `sin`.


# modules is a simple code file that can be imported and can be used easily and this is for reusability
# and to make the code more readable and easy to understand.

# Types of Modules in python


# Built-in Modules in python(standard library)

# Pre-installed modules in Python are called built-in modules. These modules are available in the Python standard library and can be used without any installation. Some of the built-in modules are:
# 1. math: This module provides mathematical functions and constants.
# 2. datetime: This module provides classes for manipulating dates and times.
# 3. os: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.
# 4. sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

# 5. random: This module implements pseudo-random number generators for various distributions.

# 6. json: This module can parse JSON from strings or files. The module can also convert Python dictionaries into JSON strings.

# 7. re: This module provides regular expression matching operations similar to those found in Perl.

# example fo built-in modules
print(math.sqrt(16))

# User-defined Modules in python

# Any python file we created can be used as the module


# this module should created in the same directory as the main file
# and the name of the module should be same as the file name
print(mod.add(2, 3))  # This will print 5

# Third party modules in python
# Third-party modules are not part of the Python standard library and need to be installed separately. These modules are created by other developers and can be found on the Python Package Index (PyPI). Some popular third-party modules are:
# 1. NumPy: This module is used for numerical computations and provides support for arrays and matrices.
# requests: This module is used for making HTTP requests and handling responses.

response = requests.get('https://api.github.com')
print(response.status_code)

print(np.array([1, 2, 3, 4, 5]))  # This will print [1 2 3 4 5]
print(np.mean([1, 2, 3, 4, 5]))  # This will print 3.0