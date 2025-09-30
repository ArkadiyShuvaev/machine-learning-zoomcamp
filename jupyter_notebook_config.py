c = get_config()  # Get the Jupyter Notebook configuration object

# Set the indentation width for code cells
c.NotebookApp.nbconvert_template_paths = ['.']
c.NotebookApp.default_cell_config = {
    "CodeCell": {
        "cm_config": {
            "indentUnit": 4,  # Set indentation to 4 spaces
            "tabSize": 4,
            "indentWithTabs": False
        }
    }
}
