# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:58:20 2022

@author: Admin
"""


from distutils.core import setup
setup(
  name = 'matrice_math',         # How you named your package folder (MyLib)
  packages = ['matrice_math'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Matrice_math is package that can be used for matrix and determinant computing with Python',   # Give a short description about your library
  author = 'Ishaan Sawant',                   # Type in your name
  author_email = 'imsawant05@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['matrix', 'determinants', 'matrices', 'array'],   # Keywords that define your package best
  install_requires=[],           # I get to this in a second
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python word :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
