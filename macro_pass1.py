MDT = []
MNT = {}
lines = []
ALA =[]
with open('input_macro.txt', 'r') as file:
    macro_code = file.readlines()

for line in macro_code:
    tokens = line.split()
    lines.append(tokens)

i=0
while i < len(lines):
    if(lines[i][0] == 'MACRO'):
        MNT[lines[i][1]] = len(MDT)
        ala_dict = {}
        for j in range(2, len(lines[i]), 2):
            ala_dict[lines[i][j]] = '#' + str(j // 2)
        ALA.append(ala_dict)
        while lines[i][0] != 'MEND':
            MDT.append([ALA[-1].get(token, token) for token in lines[i]])
            i+=1
        MDT.append(['MEND'])
    i+=1

print(MNT)
print('\n'.join(map(str,MDT)))
print(ALA)
