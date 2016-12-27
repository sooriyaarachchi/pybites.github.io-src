Title: Learning from Python mistakes
Date: 2016-12-28 9:00
Category: Learning
Tags: best practices, pep8, virtualenv, cleancode
Slug: py-mistakes
Authors: Bob
Summary: In this post I summarize some great lessons Mike Pirnat shared in his free ebook 'How to make mistakes in Python'

There are some great [free Python O'Reilly ebooks](http://www.oreilly.com/programming/free/). In this post some useful tips from Mike Pirnat's [How to make mistakes in Python](http://www.oreilly.com/programming/free/how-to-make-mistakes-in-python.csp?intcmp=il-prog-free-product-lgen_python_mistakes):

* Use [virtualenv / pyvenv](http://pybit.es/the-beauty-of-virtualenv.html) to isolate your environment.

* I am still doing this: using the default REPL which leads to a lot of arrow-up repeating, use IPython or Jupyter Notebooks.

* Always return a value from your functions / methods.

* Use PyLint (I am also relatively late in this, future post, promise ...)

* Read, use, abide by [PEP 8](https://www.python.org/dev/peps/pep-0008/), the Python style guide.

* (not Python per se) name your variables wisely. There is a whole chapter in [clean code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) dedicated to this.

* Don't abuse lambdas, I almost only use them for [sorting](https://docs.python.org/3/howto/sorting.html). Ditto for list comprehension, too much nesting makes it hard to read them. Same goes for decorators, too much nesting makes for complex code.

* Avoid long if/elif/ blocks, wrap options into classes or dicts, use Enums, look at the [Replace Conditional with Polymorphism pattern](http://refactoring.com/catalog/replaceConditionalWithPolymorphism.html).

* Leave extensive getters and setters for Java, use properties (future post).

* Write small methods and (decoupled) modules, I wrote about this generically [here](http://bobbelderbos.com/2016/03/building-maintainable-software/).

* Avoid the global scope.

* Be specific in your imports, from time import * is asking for trouble. Use time.time() instead and you won't have name clashes.

* "Explicit is better than implicit" (import this): don't use pass in except, handle the error (log it). And be specific what exception to catch (e.g. 'except IOError' is better than just 'except' which catches everything).

* Don't re-invent the wheel: [PyPI](https://pypi.python.org) is full of great modules you can pip install.

* Never use mutable default values for methods, it leads to weird behavior because each time you call the method you expect a new object (say list), yet you modify an existing one, use None instead. This and other common gotchas are described [here](http://docs.python-guide.org/en/latest/writing/gotchas/).

* Overeager Code: keep your constuctors (dunder inits) methods lean, watch out for modules doing a lot of operations when being imported. 

* [Test your code!](http://docs.python-guide.org/en/latest/writing/tests/) There are great frameworks apart from unittest, checkout [pytest](http://docs.pytest.org/en/latest/).

* Logging is cheap, [use it!](https://docs.python.org/3.5/library/logging.html) Config is tricky (future post ...)

Let's thank Mike Pirnat for sharing all these great insights in this [freely distributed ebook](http://www.oreilly.com/programming/free/how-to-make-mistakes-in-python.csp?intcmp=il-prog-free-product-lgen_python_mistakes) of just 80 pages.

---

Keep Calm and Code in Python!

-- Bob and Julian 
