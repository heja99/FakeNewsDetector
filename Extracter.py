import nbformat

def extract_code_cells(notebook_path, output_file):
    # Load the Jupyter notebook
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

    # Extract code cells
    code_cells = [cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']

    # Save code cells to a Python file
    with open(output_file, 'w', encoding='utf-8') as py_file:
        py_file.write('\n\n# Code cells extracted from Jupyter notebook\n\n')
        for code_cell in code_cells:
            py_file.write(f'\n# In[ ]:\n{code_cell}\n')

# Specify the path to the Jupyter notebook and the desired output Python file
notebook_path = './Project_Notebook.ipynb'
output_file = 'output_script.py'

# Call the function to extract code cells
extract_code_cells(notebook_path, output_file)
