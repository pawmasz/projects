import os

def run_notebook(fn=''):
    os.system(f'jupyter notebook {fn} --ip 0.0.0.0 --port 8080')