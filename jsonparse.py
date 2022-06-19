from constants import *

def separate_json(message):
    separated = []
    while(len(message)):
        if message[0] in JSON_WHITESPACE: # skip whitespace
            message = message[1:]
            continue
        elif message[0] in JSON_SYNTAX:
            separated.append(message[0])
            message = message[1:]
            continue
        elif message[0] == JSON_QUOTE:
            ret,message = separate_string(message)
            separated.append(ret)
        elif message[0].isnumeric():
            ret,message = separate_number(message)
            separated.append(ret)
    return separated

def separate_string(message):
    string = ''
    message = message[1:] # remove opening quote
    while(len(message)):
        if message[0] == JSON_QUOTE:
            message = message[1:]
            string = string
            return string,message
        else:
            string = string + message[0]
            message = message[1:]

def separate_number(message):
    string = ''
    while(len(message)):
        if not message[0].isnumeric():
            string = float(string)
            return string,message
        else:
            string = string + message[0]
            message = message[1:]


def parse_json(separated):
    parsed = {}
    separated = separated[1:]
    while(len(separated)):
        if separated[0] == JSON_RIGHTBRACE:
            return parsed, separated[1:]
        elif (((type(separated[0]) is str) and (separated[0] not in JSON_SYNTAX)) and (separated[1] is JSON_COLON)):
            # handle key, check here if next char is open brace or bracket
            if separated[2] is JSON_LEFTBRACKET:
                key = separated[0]
                separated = separated[2:]
                arr,separated = parse_array(separated[1:])
                parsed.update({key:arr})
            elif separated[2] is JSON_LEFTBRACE:
                key = separated[0]
                separated = separated[2:]
                internal_parsed, separated = parse_json(separated)
                parsed.update({key:internal_parsed})
            else:
                parsed.update({separated[0]:separated[2]})
                separated = separated[3:]
        elif (separated[0] == JSON_COMMA):
            separated = separated[1:]

def parse_array(separated):
    arr = []
    while(len(separated)):
        if separated[0] == JSON_RIGHTBRACKET:
            separated = separated[1:]
            return arr, separated
        elif separated[0] == JSON_COMMA:
            separated = separated[1:]
        elif separated[0] is JSON_LEFTBRACE:
            internal_parsed, separated = parse_json(separated)
            arr.append(internal_parsed)
        else:
            arr.append(separated[0])
            separated = separated[1:]
        
