import sys
sys.setrecursionlimit(10000)

print('Welcome to ArrowString S!\n\n{\n< write: ( Hello`_World! ) >\n}\n\nUse *help* for more information\n')
code = []; memory = []
var_names = []; var_values = []; var_types = []
consoleline = ''; line_counter = op_sym = var1 = var2 = important_shit = 0
math_supported_symbols = '0123456789.'
math_condit_sym = ['|>', '|<', '|=', '|>=', '|<=', '!>', '!<', '!=', '!>=', '!<=']; condit_op = math_condit_sym + ['in', 'not_in', 'is', 'not_is']

while consoleline != '/exit':
    if '}' not in code: print('-' * 31 + '\n/< Console output: Code mode >/\n')
    while '}' not in code:
        line_counter += 1
        line = input(str(line_counter) + '. ')

        if ('< ' in line) and ( ' >' in line):
            line = line[line.index('< '):]; line = line[:line.index(' >') + 2]
        
        code.append(line)

    if code[0] != '{':
        print("\n/< Console output - event.ERROR: '{' not found [Line: 1] >/\n")

    if 'help' in code:
        print("\n*help* | console_help | operations_help\n\nEvery program uses '{' & '}' as 'begin' & 'end'\nExecutable lines uses '<' & '>', '[' & ']' as in example of code (also as 'begin & 'end')\nYou should to use Space ' ' between variables, functions and any symbols.\n")
        print("Functions:\n")
        print("'var:' - assignment function.\n< var: *name* = *value* >\n< var: *name* = /input_num or /input_text > (input from the keyboard)\n")
        print("'write:' - output function. It deletes all Spaces. To printing ' ' use '`_' as in example.\n< write: *var* >\n< write: ( *random text* ) >\n")
        print("'op:' - function for beginning operations (only one operation per line). Has 2 types of arguments.\n< op: math: *var* *math operation* *other var / number* >\n< op: text: *var* *text operations* *other var / text* >\n")
        print("'if:' - logical function (also only one per line).\n< if: *var* / ( *text* ) *logical operation* *other var* / ( *text* ) >\n< [ *identifier* >\n< *some code* >\n< ] *identifier* >\n")
        print("'while' - cycle function. This is similar to the 'if' function. Cycle works while condition is true.\n")
        code[1] = ''

    if 'console_help' in code:
        print('\nhelp | *console_help* | operations_help\n\nFunctions:\n')
        print("'/save' - save-to-memory function. Remember that the memory is reset each time you re-enter.\n")
        print("'/clear' - clearing function.\n") # How unexpected lmao
        
        print("'/exit' - out from the program.\n")
        print("'/write *var* / ( *text* )' - console output function. It deletes all Spaces. To printing ' ' use '`_' as in example.\n")
        print("'/call var_data / memory' - calls some compiled information.\n")
        print("'/run *file_path*' - activates a file with previously written code.\n")

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
        print("'dub *num*' - duplication of the original value.\n")
        print("'rep *1st symbol* *2nd symbol*' - replacing symbols.\n")
        
        print('\nLogical operations:\n')
        print("'|>' - more than            '!>' - not more ('|<=')\n")
        print("'|<' - less than            '!<' - not less ('|>=')\n")
        print("'|=' - equals               '!=' - not equals ('|>' or '|<')\n")
        print("'|>=' - more or equals      '!>=' - not more and not equals ('|<')\n")
        print("'|<=' - less or equals      '!<=' - not less and not equals ('|>')\n")
        print("'|is' - '|=' for text vars   '!is' - '!=' for text vars\n")
        print("'|in' - existing in text     '!in' - not existing in text\n")

#/\---------------------------------------------------------------------------------------------------/\# Core of the programming language
    def line_check_begin(begin, end):
        global code, i, var1, var2, op_sym
        
        for i in range(begin, end):
        
              if ('<' in code[i].split()) and ('>' in code[i].split()):
                   if (code[i].split()[0] == '<') or (code[i].split()[-1] == '>'):

                        if code[i].split()[1] == 'var:': line_check(1)

                        if (code[i].split()[1] == 'write:') or (code[i].split()[1] == 'print:'): line_check(2)

                        if code[i].split()[1] == 'op:': line_check(3)

                        if (code[i].split()[1] == 'if:') or (code[i].split()[1] == 'while:'): line_check(4)
                        
#/\---------------------------------------------------------------------------------------------------/\# Line checking
    def line_check(function):
     global code, i, var1, var2, op_sym
     
     if function == 1: #'var:'

        if (code[i].split()[4] == '/input_num') or (code[i].split()[4] == '/input_text'): # Input num or text var from keyboard
            input_var = input("\n/< Console input: ")
            print('>/\n')

            if code[i].split()[2] not in var_names:

                if code[i].split()[4] == '/input_num': # Assignment (for numbers) (input)

                    sym_in_list = True
                    for j in range(len(input_var)):
                        if input_var[j] not in math_supported_symbols:
                            sym_in_list = False

                    if sym_in_list == False: print("\n/< Console output - event.ERROR: Assignment text to a numeric variable [Line: console] >/\n")
                    else:
                        var_names.append(code[i].split()[2])
                        var_values.append(float(input_var))
                        var_types.append('num')

                if code[i].split()[4] == '/input_text': # Also assignment (for text) (input)

                    var_names.append(code[i].split()[2])
                    input_var = input_var.replace(' ', ''); input_var = input_var.replace('`_', ' ')
                    var_values.append(input_var)
                    var_types.append('text')
                            
            else:
                if (code[i].split()[4] == '/input_num') and (var_types[var_names.index(code[i].split()[2])] == 'num'): # Re-assignment (for numbers) (input)
                                
                    value = var_names.index(code[i].split()[2])
                    var_values[value] = float(input_var)

                if (code[i].split()[4] == '/input_text') and (var_types[var_names.index(code[i].split()[2])] == 'text'): # Also re-assignment (for text) (input)
                                
                    value = var_names.index(code[i].split()[2])
                    input_var = input_var.replace(' ', ''); input_var = input_var.replace('`_', ' ')
                    var_values[value] = input_var
           
        if (code[i].split()[4] != '(') and (code[i].split()[4] != '/input_num') and (code[i].split()[4] != '/input_text') and (code[i].split()[2] not in var_names): # Assignment (for numbers)
            sym_in_list = True
            for j in range(len(code[i].split()[4])):

                if code[i].split()[4][j] not in math_supported_symbols:
                    sym_in_list = False

            if sym_in_list == False: print("\n/< Console output - event.ERROR: Assignment text to a numeric variable [Line: " + str(i + 1) + "] >/\n")

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
                        
        if (code[i].split()[2] in var_names) and (code[i].split()[4] != '(') and (code[i].split()[4] != '/input_num') and (code[i].split()[4] != '/input_text') and (var_types[var_names.index(code[i].split()[2])] == 'num'): # Re-assignment (for numbers)
            value = var_names.index(code[i].split()[2])
            var_values[value] = float(code[i].split()[4])

        if (code[i].split()[2] in var_names) and (code[i].split()[4] == '(') and (var_types[var_names.index(code[i].split()[2])] == 'text'): # Also re-assignment (for text)
            value = var_names.index(code[i].split()[2])
            stringvar = ''
                    
            for j in range(5, len(code[i].split()) - 2):
                stringvar += str(code[i].split()[j])
            stringvar = stringvar.replace('`_', ' ')
            var_values[value] = stringvar
#/\---------------------------------------------------------------------------------------------------/\# 'var' function
     if function == 2: #'write:'
         
        if code[i].split()[2] == '(':
            stringvar = ''
            for j in range(3, len(code[i].split()) - 2):
                stringvar += str(code[i].split()[j])
            stringvar = stringvar.replace('`_', ' ')
            stringvar = '\n/< Console output: "' + stringvar + '" >/\n'
            print(stringvar)

        if code[i].split()[2] != '(':

            if code[i].split()[2] not in var_names:
                print('\n/< Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')
                            
            else:
                value = var_names.index(code[i].split()[2])
                stringvar = '\n/< Console output: "' + str(var_values[value]) + '" >/\n'
                print(stringvar)
#/\---------------------------------------------------------------------------------------------------/\# 'write' function
     if function == 3: #'op:'

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
                                        
                    else: print('\n/< Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')

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
                        else: print('\n/< Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                    if code[i].split()[4] == '//':

                        if code[i].split()[5] != '0':
                            var_values[value] = float(var_values[value] // other_number)
                        else: print('\n/< Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                    if code[i].split()[4] == '%':
                                    
                        if code[i].split()[5] != '0':
                            var_values[value] = float(var_values[value] % other_number)
                        else: print('\n/< Console output - event.ERROR: Dividing by zero [Line: ' + str(i + 1) + '] >/\n')

                else: print('\n/< Console output - event.ERROR: Using a text variable in math operation [Line: ' + str(i + 1) + '] >/\n')                    

            elif (var_types[var_names.index(code[i].split()[3])] == 'text') and (code[i].split()[2] == 'math:'):
                print('\n/< Console output - event.ERROR: Using a text variable in math operation [Line: ' + str(i + 1) + '] >/\n')
                                
#/\---------------------------------------------------------------------------------------------------/\# 'op math' function
                                
            if (code[i].split()[2] == 'text:') and (var_types[value] == 'text'):

                if code[i].split()[4] == 'rcut':
                    var_values[value] = var_values[value][:int(code[i].split()[5])]

                if code[i].split()[4] == 'lcut':
                    var_values[value] = var_values[value][int(code[i].split()[5]):]

                if code[i].split()[4] == 'dub':
                    var_values[value] *= int(code[i].split()[5])

                if code[i].split()[4] == 'rep':
                    var_values[value] = var_values[value].replace(code[i].split()[5], code[i].split()[6])

                if code[i].split()[4] == 'add':

                    if code[i].split()[5] == '(':
                        stringvar = ''

                        for j in range(6, len(code[i].split()) - 2):
                            stringvar += str(code[i].split()[j])

                        stringvar = stringvar.replace('`_', ' ')
                        var_values[value] += stringvar

                    elif code[i].split()[5] in var_names:
                        var_values[value] += str(var_values[var_names.index(code[i].split()[5])])

                    else: print('\n/< Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')

            elif (code[i].split()[2] == 'text:') and (var_types[value] == 'num'):
                print('\n/< Console output - event.ERROR: Using a num variable in text operation [Line: ' + str(i + 1) + '] >/\n')
                                
        else: print('\n/< Console output - event.ERROR: Variable is not defined [Line: ' + str(i + 1) + '] >/\n')
                    
#/\---------------------------------------------------------------------------------------------------/\# 'op text' function
     if function == 4: #'if:' + 'while:'

        if (len(code[i + 1].split()) == 4) and (code[i + 1].split()[1] == '['):
            if_op_id = code[i + 1].split()[2]
            condition_line_index = i # as constant
            condit_line = code[condition_line_index].split()
            
        else: print("\n/< Console output - event.ERROR: Invalid syntax [Line: " + str(i + 2) + "] >/\n")

        def condition_check(function):
            global code, i, var1, var2, op_sym, important_shit

            for j in range(len(condit_line)):
                if condit_line[j] in condit_op:
                    op_sym = j
            
            if (('< ] ' + if_op_id + ' >') in code) and (function == 4):
                if_begin = code.index('< [ ' + if_op_id + ' >') + 1
                if_end = code.index('< ] ' + if_op_id + ' >', if_begin)
                condition2 = True
                var1_is_defined = True; var2_is_defined = True                       
    #--------------------------------------------------------------------- first var
                condition = True
                if len(condit_line[:op_sym]) == 3:
                        
                    if condit_line[2] in var_names:
                        value = var_names.index(condit_line[2])
                        var1 = var_values[value]

                    else:
                        for j in range(len(condit_line[2])):

                            if condit_line[2][j] not in math_supported_symbols:
                                condition = False

                        if condition == True:
                            var1 = float(condit_line[2])

                        else: print('\n/< Console output - event.ERROR: Variable1 is not defined [Line: ' + str(i + 1) + '] >/\n'); var1_is_defined = False

                elif (len(condit_line[:op_sym]) >= 5) and (condit_line[2] == '('):
                    stringvar = ''
                    value = condit_line.index(')', 1)

                    for j in range(3, value):
                        stringvar += str(condit_line[j])

                    stringvar = stringvar.replace('`_', ' ')
                    var1 = stringvar
    #--------------------------------------------------------------------- second var      
                condition = True
                if len(condit_line[op_sym:]) == 3:
                        
                    if condit_line[op_sym:][1] in var_names:
                        value = var_names.index(condit_line[op_sym:][1])
                        var2 = var_values[value]

                    else:
                        for j in range(len(condit_line[op_sym:][1])):

                            if condit_line[op_sym:][1][j] not in math_supported_symbols:
                                condition = False

                        if condition == True:
                            var2 = float(condit_line[op_sym:][1])

                        else: print('\n/< Console output - event.ERROR: Variable2 is not defined [Line: ' + str(i + 1) + '] >/\n'); var2_is_defined = False

                elif (len(condit_line[op_sym:]) >= 5) and (condit_line[op_sym:].count('(') == 1):
                    stringvar = ''

                    for j in range(condit_line.index('(', op_sym) + 1, len(condit_line) - 2):
                        stringvar += str(condit_line[j])

                    stringvar = stringvar.replace('`_', ' ')
                    var2 = stringvar
    #--------------------------------------------------------------------- logical operations
                if (var1_is_defined == True) and (var2_is_defined == True):

                    if type(var1) != type(var2): print("\n/< Console output - event.ERROR: Logical operation between num and text vars [Line: " + str(i + 1) + "] >/\n")

                    else:
                        if (condit_line[3] in math_condit_sym) and (type(var1) == type(var2) == float):

                            if (condit_line[op_sym] == '|>') or (condit_line[op_sym] == '!<='):
                                if var1 > var2:
                                    condition2 = True
                                else: condition2 = False

                            if (condit_line[op_sym] == '|<') or (condit_line[op_sym] == '!>='):
                                if var1 < var2:
                                    condition2 = True
                                else: condition2 = False

                            if condit_line[op_sym] == '|=':
                                if var1 == var2:
                                    condition2 = True
                                else: condition2 = False
    
                            if condit_line[op_sym] == '!=':
                                if var1 != var2:
                                    condition2 = True
                                else: condition2 = False
    
                            if (condit_line[op_sym] == '|>=') or ((condit_line[op_sym] == '!<')):
                                if var1 >= var2:
                                    condition2 = True
                                else: condition2 = False

                            if (condit_line[op_sym] == '|<=') or (condit_line[op_sym] == '!>'):
                                if var1 <= var2:
                                    condition2 = True
                                else: condition2 = False

                        elif type(var1) == type(var2) == str:

                            if condit_line[op_sym] == '|in':
                                if var1 in var2:
                                    condition2 = True
                                else: condition2 = False

                            if condit_line[op_sym] == '!in':
                                if var1 not in var2:
                                    condition2 = True
                                else: condition2 = False

                            if condit_line[op_sym] == '|is':
                                if var1 == var2:
                                    condition2 = True
                                else: condition2 = False
                                
                            if condit_line[op_sym] == '!is':
                                if var1 != var2:
                                    condition2 = True
                                else: condition2 = False

                        if condition2 == False:

                             important_shit = 1
                             for j in range(if_begin, if_end):
                                  code[j] = code[j][1:]
 
                        elif condit_line[1] == 'while:':

                             while important_shit == 0:
                                  line_check_begin(if_begin, if_end)
                                  condition_check(4)

            else: print("\n/< Console output - event.ERROR: Invalid syntax [Line: " + str(i + 2) + "] >/\n")
        condition_check(4)                
#/\---------------------------------------------------------------------------------------------------/\# 'if' function
    line_check_begin(1, len(code) - 1)
    line_counter = 0
    if '}' in code: print('-' * 34 + '\n/< Console output: Console mode >/\n')
    consoleline = input('>> ')
    
    if consoleline == '/save':
        memory.append(code)
        print('\n/< Console output: Saved successfully >/\n')

    code = ['{','}']

    if len(consoleline.split()) > 1:

        if consoleline.split()[0] == '/run':

             import os.path
             if os.path.exists(consoleline.split()[1]) == True:
                 
                 print('\n')
                 code = open(consoleline.split()[1]).readlines(); code[0] = '{'
                 for y in range(len(code)):
                     print(code[y].replace('\n', ''))
                     if ('< ' in code[y]) and ( ' >' in code[y]): code[y] = code[y][code[y].index('< '):]; code[y] = code[y][:code[y].index(' >') + 2];

             else: print('\n/< Console output - event.ERROR: Path does not exist >/\n')
                 
        if (consoleline.split()[0] == '/write') or (consoleline.split()[0] == '/print'):
            stringvar = ''

            if consoleline.split()[1] != '(':

                if consoleline.split()[1] not in var_names:
                    print('\n/< Console output - event.ERROR: Variable is not defined >/\n')

                else:
                    value = var_names.index(consoleline.split()[1])
                    stringvar = '\n/< Console output: "' + str(var_values[value]) + '" >/\n'
                    print(stringvar)
            
            if consoleline.split()[1] == '(':
                for j in range(2, len(consoleline.split()) - 1):
                    stringvar += str(consoleline.split()[j]) + ' '
                stringvar = stringvar.replace(' ', ''); stringvar = stringvar.replace('`_', ' ')
                stringvar = '\n/< Console output: "' + stringvar + '" >/\n'
                print(stringvar)

        if consoleline.split()[0] == '/call':

            if consoleline.split()[1] == 'var_data':

                if var_names != var_values != var_types != []:
                
                    print('\n')
                    for i in range(len(var_names)):
                        print('Var name:', var_names[i], '| Var value:', var_values[i], '| Var type:', var_types[i], sep = ' ')
                    print('\n')

                else: print('\n/< Console output: Memory is empty >/\n')

            if consoleline.split()[1] == 'memory':
                print('\n'); print(memory); print('\n')
                
    if consoleline == '/clear':
        code = []; var_names = []; var_values = []; var_types = []
        print('\n/< Console output: Cleared successfully >/\n')
#/\---------------------------------------------------------------------------------------------------/\# Console commands
