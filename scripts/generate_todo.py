import os, sys

tab = '\t'

def generate_todo():
    for name in os.listdir('./project'):
        if name != '__pycache__':
            if os.path.isdir(f'./project/{ name }'):
                for sub_name in os.listdir((f'./project/{ name }')):
                    if sub_name.find('.py') != -1 and sub_name.find('.pyc') == -1:
                        with open(f'./project/{ name }/{ sub_name }', 'r') as f:
                            lines = f.readlines()
                            for x in range(len(lines)):
                                name_line = ''
                                desc_line = ''
                                if lines[x] != '\n':
                                    if lines[x].find('#TODO') != -1:
                                        starting_pos = x
                                        while x != len(lines) and lines[x].find('#') != -1:
                                            limit = 0
                                            if x == len(lines) - 1:
                                                limit = len(lines[x])
                                            else:
                                                limit = len(lines[x])-1
                                            if x != starting_pos:
                                                desc_line = desc_line + lines[x][1:limit]
                                            else:
                                                name_line = name_line + lines[x][1:limit]
                                            x = x + 1
                                        write_to_readme(f"{name_line.strip().replace('#', '')[5:]} ('./project/{name}/{sub_name}', L{x})")
            else:
                if name.find('.py') != -1 and name.find('.pyc') == -1:
                    with open(f'./project/{ name }', 'r') as f:
                        lines = f.readlines()
                        for x in range(len(lines)):
                            name_line = ''
                            desc_line = ''
                            if lines[x] != '\n':
                                if lines[x].find('#TODO') != -1:
                                    starting_pos = x
                                    while x != len(lines) and lines[x].find('#') != -1:
                                        limit = 0
                                        if x == len(lines) - 1:
                                            limit = len(lines[x])
                                        else:
                                            limit = len(lines[x])-1
                                        if x != starting_pos:
                                            desc_line = desc_line + lines[x][1:limit]
                                        else:
                                            name_line = name_line + lines[x][1:limit]
                                        x = x + 1
                                    write_to_readme(f"{name_line.strip().replace('#', '')[5:]} ('./project/{name}', L{x})")
                        
def write_to_readme(line):
    text = ''
    with open('README.md', 'r') as f:
        text = f.read()
    if text.find(line[:line.rindex(',')]) != -1 and text.find(line) == -1:
        line_start_index = len(line[:line.rindex(',')])
        line_end_index = len(line)
        text_start_index = text.index(line[:line.rindex(',')]) + line_start_index
        text_end_index = text.index(line[:line.rindex(',')]) + line_end_index
        final_text = text[:text_start_index] + line[line_start_index:line_end_index] + text[text_end_index:]
        with open('README.md', 'w') as f:
            f.write(final_text)
    elif text.find(line) == -1:
        index = text.index('Todo:') + 6
        final_text = f'{text[:index]}* {line}\n{text[index:]}'
        with open('README.md', 'w') as f:
            f.write(final_text)

print('Starting python script\n...')
generate_todo()
print('Finished python script!')
