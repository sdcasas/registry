Documenting your Django application with sphinx
===============================================
 

Documenting web applications is not easy, over the last 8 years or so I have been a software consultant this has been one of the most challenging bits.

Overtime I have come to appreciate the value and importance of writing documentation, I setup my projects from the start to have documentation and thankfully with Django this is super easy.

After trying out a couple of  options and pulling out my hair in frustration smiley , I’ve settled with a combination of sphinx and django-docs which I’ve found to be both efficient , time saving and most importantly this setup fits naturally into my development flow, I don’t have to learn new markups or syntax to write my documentation, I simply use python docstrings and I am good to go.

For me documentation has two main benefits, it helps me understand my code better and helps others understand my code and thought process.With those benefits in mind let’s get started.
Install Sphinx

Sphinx is a document generator written in python, it was originally created to build the new Python documentation.
Sphinx converts reStructuredText files into HTML websites and other formats including PDF, EPub and man.

We will use pip to install Sphinx

    $ pip install sphinx

o

    $ pip install -r deploy/requirements-doc.txt

Once the installation is done you will need to create the document root folder, this folder will hold  the generated documentation and also all the assets you will need to generate your documentation.Run the following command

    $ sphinx-quickstart

You will be asked a number of questions.



To build the html files you will to cd into your /docs folder and hit the make command.

    $ make html