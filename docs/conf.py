import os
import sys
sys.path.insert(0, os.path.abspath('..'))
project = 'JetEngineCycleSimulator'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store'] 