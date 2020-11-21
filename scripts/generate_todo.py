import os

tab = '\t'
api_path = './fast_api/app'


def generate_todo():
    for name in os.listdir(api_path):
        if name != '__pycache__':
            if os.path.isdir(f'{api_path}/{ name }'):
                for sub_name in os.listdir((f'{api_path}/{ name }')):
                    if sub_name.find('.py') != -1 and sub_name.find('.pyc') == -1:  # noqa: E501
                        with open(f'{api_path}/{ name }/{ sub_name }', 'r') as f:  # noqa: E501
                            lines = f.readlines()
                            for x in range(len(lines)):
                                name_line = ''
                                desc_line = ''
                                if lines[x] != '\n':
                                    if lines[x].find('# TODO') != -1:
                                        starting_pos = x
                                        while x != len(lines) and lines[x].find('#') != -1:  # noqa: E501
                                            limit = 0
                                            if x == len(lines) - 1:
                                                limit = len(lines[x])
                                            else:
                                                limit = len(lines[x])-1
                                            if x != starting_pos:
                                                desc_line = desc_line + lines[x][1:limit]  # noqa: E501
                                            else:
                                                name_line = name_line + lines[x][1:limit]  # noqa: E501
                                            x = x + 1
                                        write_to_readme(f"{name_line.strip().replace('#', '')[5:]} ('{api_path}/{name}/{sub_name}', L{x})")  # noqa: E501
            else:
                if name.find('.py') != -1 and name.find('.pyc') == -1:
                    with open(f'{api_path}/{ name }', 'r') as f:
                        lines = f.readlines()
                        for x in range(len(lines)):
                            name_line = ''
                            desc_line = ''
                            if lines[x] != '\n':
                                if lines[x].find('# TODO') != -1:
                                    starting_pos = x
                                    while x != len(lines) and lines[x].find('#') != -1:  # noqa: E501
                                        limit = 0
                                        if x == len(lines) - 1:
                                            limit = len(lines[x])
                                        else:
                                            limit = len(lines[x])-1
                                        if x != starting_pos:
                                            desc_line = desc_line + lines[x][1:limit]  # noqa: E501
                                        else:
                                            name_line = name_line + lines[x][1:limit]  # noqa: E501
                                        x = x + 1
                                    write_to_readme(f"{name_line.strip().replace('#', '')[5:]} ('{api_path}/{name}', L{x})")  # noqa: E501


def write_to_readme(line):
    text = ''
    with open('README.md', 'r') as f:
        text = f.read()
    if text.find(line[:line.rindex(',')]) != -1 and text.find(line) == -1:
        line_start_index = len(line[:line.rindex(',')])
        line_end_index = len(line)
        text_start_index = text.index(line[:line.rindex(',')]) + line_start_index  # noqa: E501
        text_end_index = text.index(line[:line.rindex(',')]) + line_end_index
        final_text = text[:text_start_index] + line[line_start_index:line_end_index] + text[text_end_index:]  # noqa: E501
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
