#!/usr/bin/env python3

import os, json
from terminaltables import AsciiTable

def extract(path):
    data = json.load(open(path, 'r'))
    name = data['name']
    version = data['version']
    file = data['fileName']
    return [name, version, file]
    
def main():
    columns = [['Name', 'Version', 'File']]
    path = '/'.join(__file__.split('/')[:-1])
    if (path == ''): 
        path = '.'
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            dep = os.path.join(root, name)
            if dep.endswith('.json'):
                print("Processing " + dep + "...")
                columns.append(extract(dep))
    table = AsciiTable(columns).table
    md = '\n'.join(table.replace('+', '|').split('\n')[1:-1])
    print("\n" + table + "\n")
    title = "UPDATED VENDORDEPS"
    # with open(path + '/readme.txt', 'w') as f:
    #     f.write(title + '\n' + len(title) * '-' + '\n\n' + table)
    with open(path + '/readme.md', 'w') as f:
        f.write("# " + title + '\n\n' + md + '\n')
    
if __name__ == '__main__':
    main()