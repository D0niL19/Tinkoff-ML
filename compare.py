import ast
import codecs

def levenstein(a, b):
    F = [[(i+j) if i*j == 0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
         for j in range(1, len(b)+1):
             if a[i-1]==b[j-1]:
                 F[i][j] = F[i-1][j-1]
             else:
                 F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(a)][len(b)]

input_file = open(input(), 'r')
output_file = open(input(), 'w')


for line in input_file:
    a = line.split()
    #print(a)
    node1 = ast.parse(codecs.open( a[0], "r", "utf_8_sig" ).read())
    node2 = ast.parse(codecs.open( a[1], "r", "utf_8_sig" ).read())
    #print(len(ast.dump(node1)), len(ast.dump(node2)))
    pop = levenstein(ast.dump(node1), ast.dump(node2))
    #print(pop, 1 - round(pop/len(ast.dump(node1)),2))
    output_file.write(str(1 - round(pop/len(ast.dump(node1)),2)) + '\n')
    
input_file.close()
output_file.close()
