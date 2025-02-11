import os

def create_project_structure():
    # Define the project directories and files
    directories = [
        'src',
        'kb'
    ]
    
    files = [
        'src/main.py',
        'src/agente_ia.py',
        'kb/conocimiento.json',
        'grafo.py',
        'README.md',
        'setup_ini.py'
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Create files
    for file in files:
        with open(file, 'w') as f:
            if file == 'kb/conocimiento.json':
                f.write('{}')  # Create an empty JSON file
            else:
                f.write('# This file is intentionally left blank\n')

if __name__ == "__main__":
    create_project_structure()