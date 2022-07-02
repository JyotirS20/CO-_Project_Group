#Under construction

instructions_dict={"add":"10000","sub":"10001","mov":"10010","ld":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010"}
instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt","var"]
register_dict={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

# 3 label_name : add R1 R2 R3
# 30 jmp label_name

#label
#var
#errors

#var a b
#add R1 R2 R 3
#add R1 R2 X X

"""
var X
mov R1 $10
mov R2 $100
mul R3 R1 R2
st R3 X
hlt
"""

def binary(n):
    out=""
    temp = int(n[1:])
    while len(out)<8: #check
        out+=str(temp%2)
        temp=temp//2
    return out[::-1]

def binary_int(n):
    out=""
    temp = n
    while len(out)<8: #check
        out+=str(temp%2)
        temp=temp//2
    return out[::-1]

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
#print(text)
#print(type(text))
input_list=text.split("\n")
print(input_list)

out_list=[]
var_list=[]
label_list=[]
var_dict={}
label_dict={}
count_instructions=0
line_number=0

opcodeA_list=["add","sub","mul","xor","or","and"]
opcodeB_list=["mov","ls","rs"]
opcodeC_list=["mov","div","not","cmp"]
opcodeD_list=["ld","st"]
opcodeE_list=["jmp","jlt","jgt","je"]
opcodeF_list=["hlt"]

for i in input_list:

    line_number+=1 #line number is incremented regardless of type of instruction
   
    command=i.split() #part of each instruction is split into separate components
    #checking if the command is a label or not
    if command[0][-1]==":":
        label_list.append(command[0])
        label_dict[command[0][:-1]]=binary_int(count_instructions)
        flag_label=1 #if yes then setting flag=1
    else:
        flag_label=0 #else flag=0
   
    if command[0] not in instructions and flag_label==0: #command is neither an instruction nor a label
        error_instruction() #print error
    if(command[0])=="var": #if command is declaring a variable
        var_list.append(command[1]) #add the variable to the variable list
   
    if (command[0]=="var"):
        continue
    """
    if(command[0]) in opcodeA_list:
        print(opcode_A(command))
    elif (command[0]) in opcodeB_list:
        print(opcode_B(command))
    elif(command[0]) in opcodeC_list:
        print(opcode_C(command))
    elif (command[0]) in opcodeD_list:
        print(opcode_D(command))
    elif(command[0]) in opcodeE_list:
        print(opcode_E(command))
    elif (command[0]) in opcodeF_list:
        print(opcode_F(command))
    elif (command[0]=="var"):
        continue
    else:
        error_instruction() #thus we have taken into account if input is a valid instruction or not
    """
    count_instructions+=1 #counting the number of instructions, excluding var

var_memory_line=count_instructions
for i in var_list:
    var_dict[i]=binary_int(var_memory_line)
    var_memory_line+=1


def opcode_A(list_input):
    return instructions_dict[list_input[0]] + "00"+ register_dict[list_input[1]] + register_dict[list_input[2]] + register_dict[list_input[3]]

def opcode_B(list_input):
    return instructions_dict[list_input[0]] + register_dict[list_input[1]] + binary(list_input[2])

def opcode_C(list_input):
    return instructions_dict[list_input[0]] + "00000" + register_dict[list_input[1]] + register_dict[list_input[2]]

def opcode_D(list_input):
    return instructions_dict[list_input[0]] + register_dict[list_input[1]] + var_dict[list_input[2]]

def opcode_E(list_input):
    return instructions_dict[list_input[0]] + "000" + label_dict[list_input[1]]

def opcode_F(list_input):
    return instructions_dict[list_input[0]] + "00000000000"




def error_instruction():
    print("Command not found")
    return

def error_hlt():
    print("Halt not found")
    return

def find(inst):
    if(inst in opcodeA_list):
        return opcode_A

for i in input_list:
   
    line_number+=1 #line number is incremented regardless of type of instruction
   
    command=i.split() #part of each instruction is split into separate components
    #checking if the command is a label or not
    if command[0][-1]==":":
        label_list.append(command[0])
        flag_label=1 #if yes then setting flag=1
    else:
        flag_label=0 #else flag=0
   
    if command[0] not in instructions and flag_label==0: #command is neither an instruction nor a label
        error_instruction() #print error
    if(command[0])=="var": #if command is declaring a variable
        var_list.append(command[1]) #add the variable to the variable list

    if (command[0]) in opcodeA_list:
        if len(command)==4:
            out_list.append(opcode_A(command))
        else:
            error_list.append("Invalid input length for Type A Instruction; line " +str(line_number))
            
    elif (command[0]) in opcodeB_list and len(command)==3:
        if len(command)==3:
            out_list.append(opcode_B(command))
        else:
            error_list.append("Invalid input length for Type B Instruction")
            
    elif(command[0]) in opcodeC_list and len(command)==3:
        if len(command)==3:
            out_list.append(opcode_C(command))
        else:
            error_list.append("Invalid input length for Type C Instruction")
            
    elif (command[0]) in opcodeD_list and len(command)==3:
        if len(command)==3:
            out_list.append(opcode_D(command))
        else:
            error_list.append("Invalid input length for Type D Instruction")

    elif(command[0]) in opcodeE_list and len(command)==2:
        if len(command)==2:
            out_list.append(opcode_E(command))
        else:
            error_list.append("Invalid input length for Type E Instruction")

    elif (command[0]) in opcodeF_list len(command)==1:
        if len(command)==1:
            out_list.append(opcode_F(command))
            error_list.append("Invalid input length for Type F Instruction")

    elif (command[0]=="var"):
        continue
    
    elif(command[0][:-1] in label_dict):
        command=command[1:]
        if(command[0]) in opcodeA_list:
            out_list.append(opcode_A(command))
        elif (command[0]) in opcodeB_list:
            out_list.append(opcode_B(command))
        elif(command[0]) in opcodeC_list:
            out_list.append(opcode_C(command))
        elif (command[0]) in opcodeD_list:
            out_list.append(opcode_D(command))
        elif(command[0]) in opcodeE_list:
            out_list.append(opcode_E(command))
        elif (command[0]) in opcodeF_list:
            out_list.append(opcode_F(command))
       
    else:
        error_instruction() #thus we have taken into account if input is a valid instruction or not

    count_instructions+=1 #counting the number of instructions, excluding var


#var aba
