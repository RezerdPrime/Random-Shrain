print('Welcome to ArrowString S!\n\n{\n< write: ( Hello World! ) >\n}\n\nUse *help* for more information\n')
code = []; memory = []
var_names = []; var_values = []; var_types = []
consoleline = ''; line_counter = 0
math_supported_symbols = '0123456789.'

while consoleline != '/exit':
    if '}' not in code: print('-' * 30 + '\n/<Console output: Code mode >/\n')
    while '}' not in code:
        line_counter += 1
        line = input(str(line_counter) + '. ')
        code.append(line)

    if code[0] != '{':
        print("\n/<Console output - event.ERROR: '{' not found [Line: 1] >/\n")

    if 'help' in code:
        print("\n*help* | console_help | operations_help\n\nEvery program uses '{' & '}' as 'begin' & 'end'\nExecutable lines uses '<' & '>' as in example of code (also as 'begin & 'end')\nYou should to use Space ' ' between variables, functions and any symbols\n")
        print("Functions:\n")
        print("'var:' - assignment function.\n< var: *name* = *value* >\n")
        print("'write:' - output function.\n< write: *var* >\n< write: ( *random text* ) >\n")
        print("'op:' - function for beginning operations (only one operation per line). Has 2 types of arguments.\n< op: math: *var* *math operation* *other var / number* >\n< op: text: *var* *text operations* *other var / text* >\n")
        code[1] = ''

    if 'console_help' in code:
        print('\nhelp | *console_help* | operations_help\n\nFunctions:\n')
        print("'/save' - save-to-memory function. Remember that the memory is reset each time you re-enter.\n")
        print("'/clear' - clearing function.\n") # How unexpected lmao
        print("'/exit' - out from the program.\n")
        print("'/write *var* / ( *text* )' - console output function.\n")

    if 'operations_help' in code:
        print('\nhelp | console_help | *operations_help*\n\nOperations:\n')
        print('Mathematic operations:\n')
        print("'+, -, *, /, ^' - base math operations\n")
        print("'//' - integer division\n")
        print("'%' - residue from division\n")
        print('\nText operations:\n')
        print("'add *var* / ( *text* )' - string stacking. It allows to stack 'text' variable with 'num', but not the other way around.\n")
        print("'rcut *num*' - slicing from the right side.\n")
        print("'lcut *num*' - slicing from the left side.\n")
#/\---------------------------------------------------------------------------------------------------/\# Core of the programming language
    for i in range(1, len(code) - 1):
        if ('<' in code[i].split()) and ('>' in code[i].split()):
            if (code[i].split()[0] == '<') or (code[i].split()[-1] == '>'):

                if code[i].split()[1] == 'var:':

                    if (code[i].split()[4] != '(') and (code[i].split()[2] not in var_names): # Assignment (for numbers)
                        sym_in_list = True
                        for j in range(len(code[i].split()[4])):

                            if code[i].split()[4][j] not in math_supported_symbols:
                                sym_in_list = False

                        if sym_in_list == False:
                            print("\n/<Console output - event.ERROR: Assignment text to a numeric variable [Line: " + str(i + 1) + "] >/\n")

                        else:
                            var_names.append(code[i].split()[2])
                            var_values.append(float(code[i].split()[4]))
                            var_types.append('num')
                
                    if (code[i].split()[4] == '(') and (code[i].split()[2] not in var_names): # Also assignment (for text)
                        var_names.append(code[i].split()[2])
                        stringvar = ''
                    
                        for j in range(5, len(code[i].split()) - 2):
                            stringvar += str(code[i].split()[j])
                        stringvar = stringvar.replace('`_', ' ')
                        var_values.append(stringvar)
                        var_types.append('text')

                    if (code[i].split()[2] in var_names) and (code[i].split()[4] != '(') and (var_values[var_names.index(code[i].split()[2])] == 'num'): # Re-assignment (for numbers)
                        value = var_names.index(code[i].split()[2])
                        var_values[value] = float(code[i].split()[4])

                    if (code[i].split()[2] in var_names) and (code[i].split()[4] == '(') and (var_values[var_names.index(code[i].split()[2])] == 'text'): # Also re-assignment (for text)
                        value = var_names.index(code[i].split()[2])
                        stringvar = ''
                    
                        for j in range(5, len(code[i].split()) - 2):
                            stringvar += str(code[i].split()[j])
                        stringvar = stringvar.replace('`_', ' ')
                        var_values[value] = stringvar
#/\---------------------------------------------------------------------------------------------------/\# 'var' function
                if code[i].split()[1] == 'write:':
            
                    if code[i].split()[2] == '(':
                        stringvar = ''
                        for j in range(3, len(code[i].split()) - 2):
                            stringvar += str(code[i].split()[j])
                        stringvar = stringvar.replace('`_', ' ')
                        stringvar = '\n/<Console output: "' + stringvar + '" >/\n'
                        print(stringvar)

                    if code[i].split()[2] != '(':

                        if code[i].split()[2] not in var_names:
                            print('\n/<Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')
                            
                        else:
                            value = var_names.index(code[i].split()[2])
                            stringvar = '\n/<Console output: "' + str(var_values[value]) + '" >/\n'
                            print(stringvar)
#/\---------------------------------------------------------------------------------------------------/\# 'write' function
                if code[i].split()[1] == 'op:':

                    if code[i].split()[3] in var_names:
                        value = var_names.index(code[i].split()[3])
                    
                        if (code[i].split()[2] == 'math:') and (var_types[value] == 'num'):
                            condition = True
                            
                            for j in range(len(code[i].split()[5])):

                                if code[i].split()[5][j] not in math_supported_symbols:
                                    condition = False
                                    
                            if condition == False:
                                
                                if code[i].split()[5] in var_names:
                                    other_number = var_values[var_names.index(code[i].split()[5])]
                                        
                                else: print('\n/<Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')

                            else: other_number = float(code[i].split()[5])

                            if type(var_values[value]) == type(other_number):
                                    
                                if code[i].split()[4] == '+':
                                    var_values[value] += other_number

                                if code[i].split()[4] == '-':
                                    var_values[value] -= other_number

                                if code[i].split()[4] == '*':
                                    var_values[value] *= other_number

                                if code[i].split()[4] == '^':
                                        var_values[value] **= other_number

                                if code[i].split()[4] == '/':

                                    if code[i].split()[5] != '0':
                                        var_values[value] /= other_number
                                    else: print('\n/<Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                                if code[i].split()[4] == '//':

                                    if code[i].split()[5] != '0':
                                        var_values[value] = float(var_values[value] // other_number)
                                    else: print('\n/<Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                                if code[i].split()[4] == '%':
                                    
                                    if code[i].split()[5] != '0':
                                        var_values[value] = float(var_values[value] % other_number)
                                    else: print('\n/<Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                            else: print('\n/<Console output - event.ERROR: Using a text variable in math operation [Line: ' + str(i + 1) + '] >/\n')
                            

                        elif (var_types[var_names.index(code[i].split()[3])] == 'text') and (code[i].split()[2] == 'math:'):
                            print('\n/<Console output - event.ERROR: Using a text variable in math operation [Line: ' + str(i + 1) + '] >/\n')
                                
#/\---------------------------------------------------------------------------------------------------/\# 'op math' function
                                
                        if (code[i].split()[2] == 'text:') and (var_types[value] == 'text'):

                            if code[i].split()[4] == 'rcut':
                                var_values[value] = var_values[value][:int(code[i].split()[5])]

                            if code[i].split()[4] == 'lcut':
                                var_values[value] = var_values[value][int(code[i].split()[5]):]

                            if code[i].split()[4] == 'add':

                                if code[i].split()[5] == '(':
                                    stringvar = ''

                                    for j in range(6, len(code[i].split()) - 2):
                                        stringvar += str(code[i].split()[j])

                                    stringvar = stringvar.replace('`_', ' ')
                                    var_values[value] += stringvar

                                elif code[i].split()[5] in var_names:
                                    var_values[value] += str(var_values[var_names.index(code[i].split()[5])])

                                else: print('\n/<Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')

                        elif (code[i].split()[2] == 'text:') and (var_types[value] == 'num'):
                            print('\n/<Console output - event.ERROR: Using a num variable in text operation [Line: ' + str(i + 1) + '] >/\n')
                                

                    else: print('\n/<Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')
                    
#/\---------------------------------------------------------------------------------------------------/\# 'op text' function
    line_counter = 0
    if '}' in code: print('-' * 33 + '\n/<Console output: Console mode >/\n')
    consoleline = input()
    
    if consoleline == '/save':
        memory.append(code)
        print('\n/<Console output: Saved successfully >/\n')

    code = []; code.append('{'); code.append('}')

    if consoleline.split()[0] == '/write':
        stringvar = ''

        if consoleline.split()[1] != '(':

            if code[i].split()[2] not in var_names:
                print('\n/<Console output - event.ERROR: Variable is not defined >/\n')

            else:
                value = var_names.index(consoleline.split()[1])
                stringvar = '\n/<Console output: "' + str(var_values[value]) + '" >/\n'
                print(stringvar)
            
        if consoleline.split()[1] == '(':
            for j in range(2, len(consoleline.split()) - 1):
                stringvar += str(consoleline.split()[j]) + ' '
            stringvar = '\n/<Console output: "' + stringvar[:-1] + '" >/\n'
            print(stringvar)

    if consoleline == '/clear':
        code = []; var_names = []; var_values = []; var_types = []
        print('\n/<Console output: Cleared successfully >/\n')
