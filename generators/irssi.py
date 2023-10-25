#!/usr/bin/env python3
aliases_file_path = "Aliases.txt"
output_file_path = "irssi/add-auto.ini"
remove_file_path = "irssi/remove-auto.ini"

def main():
    with open(aliases_file_path, 'r', encoding='utf-8') as aliases_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file,  \
         open(remove_file_path, 'w', encoding='utf-8') as remove_file:

        alias_definitions = []
        remove_definitions = []
        last_name = ""
        for alias in aliases_file.readlines():
            if alias.strip() == '': continue
            alias = alias.strip('\n')
            lang, name, text, invocation = parse_alias(alias)
            
            if name != last_name:
                alias_definitions.append('')  # Append empty line for file readibility
                last_name = name
            
            if name in ("close", "wing", "team", "beacon"):
                # We also have to emit the proper command
                if name == "close":
                    invocation += '; say !close $0 $1'
                else:
                    invocation += f'; say !{name}-{lang} $0-' if lang != 'en' else f'; say !{name} $0-'
                
            alias_definitions.append(invocation)
            remove_definitions.append(f'/alias -{name}-{lang}' if lang != 'en' else f'/alias -{name}')
                

        
        if alias_definitions[0].strip() == '': alias_definitions.pop(0)  # remove first line if empty
        alias_definitions_string = '\n'.join(alias_definitions)

        output_file.write(alias_definitions_string)
        remove_file.write('\n'.join(remove_definitions))

def parse_alias(alias):
    name, lang, text = alias.split(maxsplit=2)
    if name == "eta":
        text = text.replace('$1', '$0')
        text = text.replace('$2', '$1')
    elif name == "close":
        text = text.replace('$1', '$2')
    elif "$2" in text:
        text = text.replace('$1', '$0')
        text = text.replace('$2', '$1-')
    else:
        text = text.replace('$1', '$0-')
    invocation = f'/alias {name}-{lang} say {text}' if lang != 'en' else f'/alias {name} say {text} '   
    return lang, name, text, invocation


if __name__ == "__main__":
    main()