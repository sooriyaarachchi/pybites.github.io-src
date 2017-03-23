Title: 5 Vim Shortcuts for Happier Python Coding
Date: 2017-01-24 9:00
Category: Tools
Tags: vim, tools, shortcuts, tricks, flake, howdoi
Slug: vim-shortcuts
Authors: Bob
Summary: In this article I show you 5 vimrc key mappings to speed up your Vim editing / Python development. 
cover: images/featured/pb-article.png
status: draft

In this article I show you 5 .vimrc shortcuts to speed up your Python development. If you don't use or like Vim maybe you want to skip this post. On the other hand it's never too late, after a steep learning curve, [editing text at the speed of light](https://pragprog.com/book/dnvim/practical-vim) makes you a power programmer :)

## 1. Save and run Python

	nmap ,p :w<CR>:!python3 %<CR>

For Python 2 I got another shortcut:

    nmap ,2 :w<CR>:!python2.7 %<CR>

## 2. Flake 8 check

As featured in our [pep8 article](http://pybit.es/pep8.html) I find this extremely useful to flake8 my code before committing (flake8 = "the modular source code checker: pep8, pyflakes and co"):

    autocmd FileType python map <buffer> ,f :call Flake8()<CR>

Required plugin: [vim-flake8](https://github.com/nvie/vim-flake8).

## 3. Query Stackoverflow from Vim

I made a script [long time ago](http://bobbelderbos.com/2013/01/search-copy-stackoverflow-data-in-vim-with-conque/) which requires [Conque](https://github.com/vim-scripts/Conque-Shell). 

To open a Python in vertical split: 

    nmap cp :ConqueTermVSplit python3<CR>

Of course you can specify any script. The advantage is that any output generated in the second window can be edited, copied, etc with Vim commands.

UPDATE though: since I discovered the awesome [howdoi](https://github.com/gleitz/howdoi) I just installed [this plugin](https://github.com/laurentgoudet/vim-howdoi). Now I can just type the thing I will SO-search and it automatically pastes howdoi's output the doc I am editing with Vim, very cool.

## 4. Toggle Vim / Shell

I use Ctrl + Z / fg a lot. For example to go back and forth between coding and version control. You can also type :sh / Ctrl + d, see [How to temporarily exit vim and go back](http://stackoverflow.com/questions/1879219/how-to-temporarily-exit-vim-and-go-back). 

For testing I usually open script.py and test_script.py alongside each other with (here is where PEP8's 80 char line limit comes in handy):
	
	$ vi -O script.py test_script.py

Another way to interact with the command line is via Vim's Command Mode. While writing this article I found [the useful q: shortcut](http://stackoverflow.com/questions/6920943/navigating-in-vims-command-mode).

Other options for shell integration are [screen](http://www.vim.org/scripts/script.php?script_id=2711) and [tmux](https://tmux.github.io). For a follow-up post ...

## 5. Navigate files

I use [NERD tree](https://github.com/scrooloose/nerdtree) which opens a nice file tree you can navigate with regular Vim strokes, I mapped it to Ctrl + x

    map <C-x> :NERDTreeToggle<CR>

TODO: give [Command-T](https://github.com/wincent/command-t) another try. I was blown away the first time I saw Gary Bernhardt use it in [Destroy All Software](https://www.destroyallsoftware.com/screencasts).

## More Vim + Python

This only scratched the surface. Some great articles on Vim + Python: 

* [VIM and Python - a Match Made in Heaven](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) (specially note the nice indentation settings which might save you a headache).

* [Full Stack Python - Vim](https://www.fullstackpython.com/vim.html)

* [Vim & Python: Making yourself at home](https://justin.abrah.ms/vim/vim_and_python.html)

* [Use Vim as a Python IDE](http://liuchengxu.org/posts/use-vim-as-a-python-ide/)

* [Turning vim into an IDE through vim plugins](https://www.safaribooksonline.com/blog/2014/11/23/way-vim-ide/)

## What about .bashrc

Oh yeah, I do have a lot of shell aliases, 2 Python related ones I like:

* As soon as I start a new project I run 'pvenv' to create and start a new [virtual env](http://pybit.es/the-beauty-of-virtualenv.html):

		alias pvenv='python -m venv venv && source venv/bin/activate'

* I had this one too but found out that you can run 'nosetests':

		alias utest='python -m unittest discover'

## More Vim

[Practical Vim: Edit Text at the Speed of Thought](https://www.amazon.com/Practical-Vim-Edit-Speed-Thought/dp/1680501275/ref=sr_1_1?ie=UTF8&qid=1490269692&sr=8-1&keywords=practical+vim) from the author of [vimcasts](http://vimcasts.org), is THE book that got my Vim skills to the next level.

---

Keep Calm and Code in Python!

-- Bob
