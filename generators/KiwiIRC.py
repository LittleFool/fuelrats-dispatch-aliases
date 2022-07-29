#!/usr/bin/env python3
aliases_file_path = "Aliases.txt"
output_file_path = "KiwiIRC/aliases-auto.ini"

def main():
    with open(aliases_file_path, 'r', encoding='utf-8') as aliases_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:

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
            
            if name in ("close", "wing", "team", "beacon", "sc"):
                a, b = invocation.split(maxsplit=1)
                invocation = ' '.join((a, '/lines', b))
                # We also have to emit the proper command
                if name == "close":
                    invocation += ' | /msg $channel !close $1 $2'
                else:
                    invocation += f' | /msg $channel !{name}-{lang} $1+' if lang != 'en' else f' | /msg $channel !{name} $1+'
                
            alias_definitions.append(invocation)
                
        
        if alias_definitions[0].strip() == '': alias_definitions.pop(0)  # remove first line if empty
        alias_definitions_string = '\n'.join(alias_definitions)

        output_file.write(alias_definitions_string)

def parse_alias(alias):
    name, lang, text = alias.split(maxsplit=2)
    if name == "eta":
        pass  # no need to replace the parameters for this alias
    elif name == "close":
        text = text.replace('$1', '$3')
    elif "$2" in text:
        text = text.replace('$1', '$1')
        text = text.replace('$2', '$2+')
    else:
        text = text.replace('$1', '$1+')
    invocation = f'/{name}-{lang} /msg $channel {text}' if lang != 'en' else f'/{name} /msg $channel {text} '   
    return lang, name, text, invocation


if __name__ == "__main__":
    main()