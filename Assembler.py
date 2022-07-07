import sys
import os
import site

instructions_dict={"add":"10000","sub":"10001","mov":"10010","ld":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010"}
instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt","var"]
register_dict={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}
register_dict_FLAGS={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"} #includes FLAGS
#for different binary value of mov as C type
instructions_dict_C={"add":"10000","sub":"10001","mov":"10011","ld":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010"}
# 3 label_name : add R1 R2 R3
# 30 jmp label_name

#label
#var
#errors
"""
var X
mov R1 $10
mov R2 $100
mul R3 R1 R2
st R3 X
hlt
"""
#var a b
#add R1 R2 R3
#add R1 R2 X X


error_dict={} #dict with all errors
out_list=[] #list with all outputs
global_error_flag=0 #for detecting any error at any part of the program

"""
def check_valid_instruction():
    return


def check_instruction_len():
    return
"""
#function for converting a string value to binary string value
def binary(n):
    out=""
    temp = int(n[1:])
    while len(out)<8: #check
        out+=str(temp%2)
        temp=temp//2
    return out[::-1]

#function for converting an integer value to binary string value
def binary_int(n):
    out=""
    temp = n
    while len(out)<8: #check
        out+=str(temp%2)
        temp=temp//2
    return out[::-1]
lines = [] #for taking input
temp=[]
# while True:
    # line = input()
    # if line:
    #     lines.append(line)
    # else:
    #     break
temp = sys.stdin.read().splitlines()
#print(lines)
for i in range(len(temp)):
    if(temp[i]=='' or temp[i].isspace()==True):
        lines.append("just_an_empty_line_69420")
    else:
        lines.append(temp[i])
#print(lines)
		


text = '\n'.join(lines)
#print(text)
#print(type(text))

input_list=text.split("\n")

halt_index=0
found_halt=0
for j in range(len(input_list)):
    if "hlt" in input_list[j]:
        halt_index = j
        found_halt=1 #if halt is found, set found_halt=1
        break

flag_length=0

if input_list==[""]:
    flag_length=1

#print(input_list)

var_list=[] #list of variables
label_list=[] #list of labels
var_dict={} #dictionary of variables with their corresponding memory address
label_dict={} #dictionary of labels with their corresponding memory address
count_instructions=0 #counts the number of instructions
line_number=0 #counts the number of lines

opcodeA_list=["add","sub","mul","xor","or","and"]
opcodeB_list=["mov","ls","rs"]
opcodeC_list=["mov","div","not","cmp"]
opcodeD_list=["ld","st"]
opcodeE_list=["jmp","jlt","jgt","je"]
opcodeF_list=["hlt"]
#print((input_list))
if flag_length==0:
    for i in input_list:

        line_number+=1 #line number is incremented regardless of type of instruction
        command=i.split() #part of each instruction is split into separate components
        if command==["just_an_empty_line_69420"]:
            pass
        else:
            #checking if the command is a label or not
            if command[0][-1]==":" and command[0][:-1] not in label_list:
                temp_flag=0
                for j in command[0][:-1]:
                    if j not in "_1234567890abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM":
                        error_dict[line_number]="Invalid character in label name; line " + str(line_number)
                        temp_flag=1
                if temp_flag==0:
                    label_list.append(command[0][:-1])
                    label_dict[command[0][:-1]]=binary_int(count_instructions)
                    flag_label=1 #if yes then setting flag=1
            elif command[0][-1]==":" and command[0][:-1] in label_list:
                error_dict[line_number]="Label name already exists; line "+str(line_number)
            else:
                flag_label=0 #else flag=0
           
            if command[0] not in instructions and flag_label==0: #command is neither an instruction nor a label
                pass
            if(command[0])=="var": #if command is declaring a variable
                if(len(command)==2 and command[1] not in var_list):
                    temp_flag=0
                    for j in command[1]:
                        if j not in "_1234567890abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM":
                            error_dict[line_number]="Invalid character in variable name; line " + str(line_number)
                            temp_flag=1
                    if temp_flag==0:
                        var_list.append(command[1]) #add the variable to the variable list
                elif (len(command)>2):
                    error_dict[line_number]="Too many variables declared; line "+str(line_number)
                elif(len(command)==2 and command[1] in var_list):
                    error_dict[line_number]="Variable name already exists; line "+str(line_number)
                else:
                    error_dict[line_number]="Variable missing; line "+str(line_number)

           
            if (command[0]=="var"):
                continue

            count_instructions+=1 #counting the number of instructions, excluding var

var_memory_line=count_instructions

for i in var_list:
    var_dict[i]=binary_int(var_memory_line)
    var_memory_line+=1


def opcode_A(list_input,line_number):
    if((list_input[1] or list_input[2] or list_input[3]) not in register_dict):
        error_dict[line_number]="Register not defined;"+str(line_number)
        global_error_flag=1
        return
   
    if((list_input[3]=="flags") or (list_input[3]=="FLAGS")):
        error_dict[line_number]="Illegal use of flags; line "+str(line_number)
        global_error_flag=1
        return
       
    return instructions_dict[list_input[0]] + "00"+ register_dict[list_input[1]] + register_dict[list_input[2]] + register_dict[list_input[3]]

def opcode_B(list_input,line_number):
    if(list_input[1] not in register_dict):
        error_dict[line_number]="Register not defined; line "+str(line_number)
        global_error_flag=1
        return
    if ("." in list_input[2][1:]):
        error_dict[line_number]="Float values not allowed; line "+str(line_number)
        global_error_flag=1
        return
    if(int(list_input[2][1:])<0 or int(list_input[2][1:])>255):
        error_dict[line_number]="Immediate value out of range; line "+str(line_number)
        global_error_flag=1
        return
    if((list_input[2]=="flags") or (list_input[2]=="FLAGS")):
        error_dict[line_number]="Illegal use of flags; line "+str(line_number)
        global_error_flag=1
        return

    return instructions_dict[list_input[0]] + register_dict[list_input[1]] + binary(list_input[2])

def opcode_C(list_input,line_number):
    if((list_input[1] or list_input[2]) not in register_dict):
        error_dict[line_number]="Register not defined; line "+str(line_number)
        global_error_flag=1
        return
    return instructions_dict_C[list_input[0]] + "00000" + register_dict_FLAGS[list_input[1]] + register_dict[list_input[2]]

def opcode_D(list_input,line_number):
    if(list_input[1] not in register_dict):
        error_dict[line_number]="Register not defined; line "+str(line_number)
        global_error_flag=1
        return
   
    if(list_input[2] not in var_dict):
        error_dict[line_number]="Variable not defined; line "+str(line_number)
        global_error_flag=1
        return
   
    if((list_input[2]=="flags") or (list_input[2]=="FLAGS")):
        error_dict[line_number]="Illegal use of flags; line "+str(line_number)
        global_error_flag=1
        return
   
    return instructions_dict[list_input[0]] + register_dict[list_input[1]] + var_dict[list_input[2]]

def opcode_E(list_input,line_number):
    if(list_input[1] not in label_dict):
        error_dict[line_number]="Label not defined; line "+str(line_number)
        global_error_flag=1
        return
   
    if((list_input[1]=="flags") or (list_input[1]=="FLAGS")):
        error_dict[line_number]="Illegal use of flags; line "+str(line_number)
        global_error_flag=1
        return    
    return instructions_dict[list_input[0]] + "000" + label_dict[list_input[1]]

def opcode_F(list_input,line_number):
    if((list_input[0]=="flags") or (list_input[0]=="FLAGS")):
        error_dict[line_number]="Illegal use of flags; line "+str(line_number)
        global_error_flag=1
        return
   
    return instructions_dict[list_input[0]] + "00000000000"




def error_instruction(line_no):
    error_dict[line_number]="Command not found; line "+str(line_no)
    return

"""
def error_hlt():
    erro_list.append("Halt not found")
    return

def find(inst):
    if(inst in opcodeA_list):
        return opcode_A

"""

line_number=0 #for counting the line number
count_instructios=0 #for counting the line number
not_var=0 #for checking if instruction is not a variable declaration

if flag_length==0:
    for i in input_list:
       
        line_number+=1 #line number is incremented regardless of type of instruction


       
        command=i.split() #part of each instruction is split into separate components
        #checking if the command is a label or not

        if command==["just_an_empty_line_69420"]:
            pass
        else:
            if (command[0]!="var"):
                not_var=1
            if(command[0]=="hlt"):
                found_halt=1
            #    if line_number!=len(input_list)-:
            #        error_dict[line_number]="Halt not used as last instruction; line "+str(line_number)
  
            if command[0][-1]==":":
                label_list.append(command[0])
                flag_label=1 #if yes then setting flag=1
            else:
                flag_label=0 #else flag=0
           
            if command[0] not in instructions and flag_label==0: #command is neither an instruction nor a label
                error_instruction(line_number) #print error


            if (command[0]) in opcodeA_list:
                if len(command)==4:
                    out_list.append(opcode_A(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type A Instruction; line " +str(line_number)
                   
            elif (command[0] in opcodeB_list) and ('$' in command[2]):
                if len(command)==3:
                    out_list.append(opcode_B(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type B Instruction; line " +str(line_number)
                   
            elif(command[0]) in opcodeC_list:
                if len(command)==3:
                    out_list.append(opcode_C(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type C Instruction; line " +str(line_number)
                   
            elif (command[0]) in opcodeD_list:
                if len(command)==3:
                    out_list.append(opcode_D(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type D Instruction; line " +str(line_number)

            elif(command[0]) in opcodeE_list:
                if len(command)==2:
                    out_list.append(opcode_E(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type E Instruction; line " +str(line_number)

            elif (command[0]) in opcodeF_list:
                if len(command)==1:
                    out_list.append(opcode_F(command,line_number))
                else:
                    global_error_flag=1
                    error_dict[line_number]="Invalid input length for Type F Instruction; line " +str(line_number)

            elif (command[0]=="var"):
                if not_var==1:
                    error_dict[line_number]="Variable not declared at beginning; line " +str(line_number)
               
                continue

            #checking for the label
            elif(command[0][:-1] in label_dict):
               
                command=command[1:] #changing the command such that 'label_name:' is excluded
                if(len(command)==0):
                    error_dict[line_number]="Label incomplete; line " +str(line_number)
                elif command[0] not in instructions_dict:
                    error_dict[line_number]="Invalid command in label; line " +str(line_number)

                elif (command[0]) in opcodeA_list:
                    if len(command)==4:
                        out_list.append(opcode_A(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type A Instruction; line " +str(line_number)
                
                elif (command[0] in opcodeB_list) and ('$' in command[2]):
                    if len(command)==3:
                        out_list.append(opcode_B(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type B Instruction; line " +str(line_number)
                       
                elif(command[0]) in opcodeC_list:
                    if len(command)==3:
                        out_list.append(opcode_C(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type C Instruction; line " +str(line_number)
                       
                elif (command[0]) in opcodeD_list:
                    if len(command)==3:
                        out_list.append(opcode_D(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type D Instruction; line " +str(line_number)

                elif(command[0]) in opcodeE_list:
                    if len(command)==2:
                        out_list.append(opcode_E(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type E Instruction; line " +str(line_number)

                elif (command[0]) in opcodeF_list:
                    if len(command)==1:
                        out_list.append(opcode_F(command,line_number))
                    else:
                        global_error_flag=1
                        error_dict[line_number]="Invalid input length for Type F Instruction; line " +str(line_number)
                else:
                    pass
                   
            else:
                pass
                #error_instruction(line_number) #thus we have taken into account if input is a valid instruction or not

            count_instructions+=1 #counting the number of instructions, excluding var
i=halt_index+1
while_flag=0
while(i<len(input_list) and while_flag==0):
    if input_list[i]!="just_an_empty_line_69420":
        print(input_list[i])
        error_dict[line_number+1]="Halt not used as last instruction; line "+str(line_number)
        while_flag=1
    i+=1
if found_halt==0:
    error_dict[line_number+1]="Halt instruction missing"
#print(error_list)
#print(out_list)

if line_number==0:
    print("No input provided")
elif line_number>256:
    print("Number of lines exceeds 256")
elif(len(error_dict)==0):
    for i in out_list:
        print(i)
else:
    for i in sorted(error_dict.keys()):
        print(error_dict[i])
