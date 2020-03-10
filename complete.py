from graphviz import Digraph
import copy


class Matrix:
    matrix = [[[]]]

    def __init__(self, matrix):
        self.matrix = matrix

    def show(self):
        return self.matrix

    def verificare_cuvant(self, n, cuvant, nod_start, noduri_final, d, p, copie):
        ok = 0
        k = 0
        ult = 0
        g = Digraph('DFA', filename='fsm.gv')
        g.attr(rankdir='LR', size='10')
        if nod_start[0] in noduri_final:
            g.attr('node', shape='doublecircle', fillcolor="green", style="filled")
            g.node(nod_start[0])
        else:
            g.attr('node', shape='circle', fillcolor="green", style="filled")
            g.node(nod_start[0])

        g.attr('node', shape='doublecircle', fillcolor="red", style="filled")

        for o in noduri_final:
            g.node(o)

        g.attr('node', shape='circle', fillcolor="white", style="filled")

        if cuvant != "":

            for i in range(n):
                if cuvant[0] in self.matrix[d[nod_start[0]]][i]:
                    ok = 1
                    k = i
                    g.edge(nod_start[0], p[i], label=cuvant[0], color="blue", style="filled")
                    for l in range(len(self.matrix[d[nod_start[0]]][i])):
                        if self.matrix[d[nod_start[0]]][i][l] == cuvant[i]:
                            copie[d[nod_start[0]]][i][l] = '-'
            if ok == 1:
                for i in range(1, len(cuvant)):
                    verify = 0
                    for j in range(n):
                        if cuvant[i] in self.matrix[k][j]:
                            # print(j)
                            for l in range(len(self.matrix[k][j])):
                                if self.matrix[k][j][l] == cuvant[i]:
                                    if copie[k][j][l] != '-':
                                        g.edge(p[k], p[j], label=cuvant[i], color="blue", style="filled")
                                        copie[k][j][l] = '-'
                                    break
                            k = j
                            verify = 1
                            break
                    if verify == 0 and i < len(cuvant):
                        ok = 0
                        break

            for i in d:
                if d[i] == k:
                    ult = i
                    break

            if ult in noduri_final and ok == 1:
                ok = 1
            else:
                ok = 0

        elif nod_start[0] in noduri_final:
            ok = 1
        else:
            ok = 0

        for i in range(n):
            for j in range(n):
                for q in copie[i][j]:
                    if q != '-':
                        g.edge(p[i], p[j], label=q)
        g.view()
        return ok


f = open("graf3.txt")                                    # fisierul cu informatiile despre DFA
n = int(f.readline())                                   # Numarul de noduri
automat = [[[] for i in range(n)] for j in range(n)]    # Matricea de adiacenta
vr = f.readline().split()
nr = 0
d = dict()
p = dict()
for x in vr:
    d[x] = nr
    p[nr] = x
    nr += 1

nod_start = f.readline()                                # Nodul de inceput

m = int(f.readline())                                   # Numarul nodurilor finale
noduri_final = f.readline().split()                     # Lista nodurilor finale


for x in f:
    automat[d[x[0]]][d[x[2]]].append(x[4])

copie = copy.deepcopy(automat)
matrice = Matrix(automat)

cuvant = input("Cuvant: ")

print(matrice.verificare_cuvant(n, cuvant, nod_start, noduri_final, d, p, copie))
print(matrice.show())
print(copie)
f.close()
