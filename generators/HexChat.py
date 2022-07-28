#!/usr/bin/env python3
base_file_path = "HexChat/commands-default.conf"
aliases_file_path = "Aliases.txt"
output_file_path = "HexChat/commands-auto.conf"

def main():
    with open(base_file_path, 'r',  encoding='utf-8') as base_file, \
         open(aliases_file_path, 'r', encoding='utf-8') as aliases_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:

        alias_definitions = []
        last_name = ""
        for alias in aliases_file.readlines():
            if alias.strip() == '': continue
            alias = alias.strip('\n')
            lang, name, text, invocation = parse_alias(alias)
            
            if name != last_name:
                alias_definitions.append('')  # Append empty line for file readibility
                last_name = name
            
            
            alias_definitions.append(invocation)
            alias_definitions.append('')
            if name in ("close", "wing", "team", "beacon"):
                # We also have to emit the proper command
                if not name == "close":
                    mecha_cmd_invocation = f'NAME {name}-{lang}\nCMD say !{name}-{lang} &2' if lang != 'en' else f'NAME {name}\nCMD say !{name} &2'
                else:
                    mecha_cmd_invocation = f'NAME {name}-{lang}\nCMD say !{name} %2 %3'
                alias_definitions.append(mecha_cmd_invocation)
                alias_definitions.append('')
                

        alias_definitions_string = '\n'.join(alias_definitions)

        output_file.write(base_file.read())  # copy already existing content
        output_file.write(alias_definitions_string)

def parse_alias(alias):
    name, lang, text = alias.split(maxsplit=2)
    if name == "eta":
        text = text.replace('$1', '%2')
        text = text.replace('$2', '%3')
    elif name == "close":
        text = text.replace('$1', '%4')
    elif "$2" in text:
        text = text.replace('$1', ' %2')
        text = text.replace('$2', '&3')
    else:
        text = text.replace('$1', '&2')
    invocation = f'NAME {name}-{lang}\nCMD say {text}' if lang != 'en' else f'NAME {name}\nCMD say {text} '   
    return lang, name, text, invocation


if __name__ == "__main__":
    main()