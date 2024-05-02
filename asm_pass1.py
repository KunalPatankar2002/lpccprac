LC=0
instructions = ["START", "ADD", "SUB", "MOVER", "MOVEM", "MULT", "DIV", "COMP", "BC", "READ", "PRINT", "STOP", "END", "LTORG"]
symbolTable = []
literalTable = []
poolTable = [[0]]
currentPool = set()
with open('input_asm.txt', 'r') as file:
    assembly_code = file.readlines()
for line in assembly_code:
    split = line.split(sep=" ")
    if(split[0] == "START"):
        LC = int(split[1])
        LC-=1
    if split[0] not in instructions:
        symbolTable.append([split[0],LC])
    if any(element.startswith('=') for element in split):
        for element in split:
                if element.startswith('=') and element not in currentPool:
                    literalTable.append([element])
                    currentPool.add(element)
    elif split[0] == 'END':
        for item in literalTable:
            if len(item) !=2:
                item.append(LC)
                LC+=1
    elif split[0] == 'LTORG':
        currentPool.clear()
        poolTable.append([len(literalTable)])
        for item in literalTable:
            if len(item) !=2:
                item.append(LC)
                LC+=1
        LC-=1
    # print(split[0], LC)
    LC+=1
print(assembly_code)
print(symbolTable)
print(literalTable)
print(poolTable)