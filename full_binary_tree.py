t = int(raw_input()) # read a line with a single integer
import numpy as np

def num_children(root,s,e,a_matrix,children):
    children[root][s] = 1
    for u in a_matrix[s]:

        if u == e :
            continue

        num_children(root,u,s,a_matrix,children)

        children[root][s] += children[root][u]

def num_to_delete(root,s,e,a_matrix,children,to_delete):
    to_delete[root][s] = 0
    for u in a_matrix[s]:

        if u == e :
            continue

        num_to_delete(root,u,s,a_matrix,children,to_delete)

    del_chil = []
    total_chil = 0
    for u in a_matrix[s]:
        if u != e :
            del_chil.append((children[root][u],to_delete[root][u]))
            total_chil += children[root][u]
    sorted_del_chil = sorted(del_chil)
    sorted_del_chil = list(reversed(sorted_del_chil))

    if len(sorted_del_chil) == 1 :
        to_delete[root][s] = sorted_del_chil[0][0]
    elif len(sorted_del_chil) == 2:
        to_delete[root][s] = sorted_del_chil[0][1] + sorted_del_chil[1][1]
    elif len(sorted_del_chil) > 2:
        to_delete[root][s] = (total_chil - sorted_del_chil[0][0] - sorted_del_chil[1][0]) + sorted_del_chil[0][1] + sorted_del_chil[1][1]




for i in xrange(1, t + 1):
    n = int(raw_input())
    children = [[-1 for k in range(n+1)] for j in range(n+1)]
    to_delete = [[-1 for k in range(n+1)] for j in range(n+1)]
    a_matrix = {}
    original = []
    for j in range(n-1):
        a,b = [int(s) for s in raw_input().split(" ")]
        original.append((a,b))
        if a not in a_matrix:
            a_matrix[a] = []
        if b not in a_matrix:
            a_matrix[b] = []

        a_matrix[a].append(b)
        a_matrix[b].append(a)

    for root in a_matrix:
        num_children(root,root,0,a_matrix,children)
        num_to_delete(root,root,0,a_matrix,children,to_delete)

    ans = 2 * n
    for j in range(1,n+1):
        if to_delete[j][j] < ans:
            ans = to_delete[j][j]

    if i==8:
        pass
       # print original
       # print a_matrix
       # print np.matrix(children)
       # print np.matrix(to_delete)

    print "Case #{}: {}".format(i, ans)
