#!/usr/bin/env python3
base_file_path = "AdiIRC/base.ini"
aliases_file_path = "Aliases.txt"
output_file_path = "AdiIRC/aliases-auto.ini"

def main():
    with open(base_file_path, 'r',  encoding='utf-8') as base_file, \
         open(aliases_file_path, 'r', encoding='utf-8') as aliases_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:

        alias_definitions = []
        alias_invocations = []
        last_name = ""
        for alias in aliases_file.readlines():
            if alias.strip() == '': continue
            lang, name, text, parameters, invocation = parse_alias(alias)
            if name == "close": continue   # We handle /close special for AdiIRC
            if name != last_name:
                alias_definitions.append('')  # Append empty line for file readibility
                alias_invocations.append('')
            
            text = text.strip('\n')

            alias_definitions.append(f"  /hadd -m13 {name} {lang} {text}")
            alias_invocations.append(invocation)
            if name != last_name:
                alias_invocations.append(f"alias {name}-a /say-alias {name} a {parameters}")
                last_name = name

        alias_definitions_string = '\n'.join(alias_definitions)
        invocation_definition_string = '\n'.join(alias_invocations)

        base_string = base_file.read()
        base_string = base_string.replace('[[[INSERT ALIAS DEFINITIONS HERE]]]', alias_definitions_string)
        base_string = base_string.replace('[[[INSERT ALIAS INVOCATIONS HERE]]]', invocation_definition_string)
        
        output_file.write(base_string)

def parse_alias(alias):
    name, lang, text = alias.split(maxsplit=2)
    invocation = f'alias {name}-{lang} /say_alias {name} {lang} ' if lang != 'en' else f'alias {name} /say_alias {name} {lang} '
    #parameters = ''
    if name == "eta":
        text = text.replace('$1', '&clientName&')
        text = text.replace('$2', '&eta&')
        parameters = '$$1 $$2'
    elif "$2" in text:
        text = text.replace('$1', '&clientName&')
        text = text.replace('$2', '&rats&')
        parameters = '$$1 $$2-'
    else:
        text = text.replace('$1', '&clientNames&')
        parameters = '$$1-'
       
    invocation += parameters
    return lang, name, text, parameters, invocation


if __name__ == "__main__":
    main()