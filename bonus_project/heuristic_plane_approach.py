"""Heuristic Plane Approach

This script solves the kMST problem for points on the plane.
It implements the algorithm in section 4.1 of the research paper: SPANNING TREES--SHORT OR SMALL
by R. RAVIt, R. SUNDARAM:, M. V. MARATHE, D. J. ROSENKRANTZ, AND S. S. RAVIII
    * main - the main function of the script
    * mst_nonrectilinear - function using Kruskal's algorithm for MST with Euclidean distance
    * mst_rectilinear - function using Prim's Algorithm  for MST with rectilinear distance
    * print_solution - finds and prints the smallest value found
"""

import sys
import math
from kruskal_MST import Graph
from prim_MST import Graphs

def main():
    input_file = sys.argv[1]
    coordinates_x_y = list()
    k = None

    with open(input_file, "r") as f:
        for i, l in enumerate(f):
            if i != 0:
                l = l.replace("(", "").replace(")", "").replace(",", "")
                co = [float(x) for x in l.split()]
                coordinates_x_y.append(co)
            else:
                k = int(l)
    s = []

    for i, si in enumerate(coordinates_x_y):
        for j, sj in enumerate(coordinates_x_y):
            if si != sj:
                # We calculate the Euclidean distance
                d = math.sqrt(sum([(a - b) ** 2 for a, b in zip(si, sj)]))
                diameter = math.sqrt(3) * d
                x_point = (si[0] + sj[0]) / 2
                y_point = (si[0] + sj[1]) / 2
                center = [x_point, y_point]
                subset = list()
                for v, sk in enumerate(coordinates_x_y):
                    if math.sqrt(((sk[0] - center[0]) ** 2 + (sk[1] - center[1]) ** 2)) <= diameter / 2:
                        # We add all the points that are inside the circle
                        subset.append(sk)
                if len(subset) < k:
                    # We move on to the next pair in this case
                    continue
                else:
                    square_side = diameter / math.sqrt(k)
                    x_point = center[0] - diameter / 2
                    cell_points = []
                    # We add to cell_points in cell_points[i] there will be all the points that are inside the i square
                    # For every square we find all the points in subset which are inside the square

                    while x_point < center[0] + diameter / 2:
                        y_point = center[1] + diameter / 2
                        l = []

                        while y_point > center[1] - diameter / 2:

                            for v in subset:
                                if x_point <= v[0] and v[0] <= x_point + square_side:
                                    if y_point >= v[1] and v[1] >= y_point - square_side:
                                        l.append(v)
                            y_point = y_point - square_side
                        cell_points.append(l)
                        x_point = x_point + square_side
                    # sorting cell_points from maximum to minimum
                    cell_points.sort(key=len, reverse=True)
                    st = []
                    # We select k points. If there are more than k points, we arbitrarily discard points from
                    # the last chosen cell until the number is equal to k.

                    for c in cell_points:
                        for p in c:
                            if len(st) < k:
                                st.append(p)

                    while len(st) > k:
                        st.pop()
                    # We need to check first which MST we are going to create (Euclidean or Rectilinear).
                    # In order to do that we are going to check if the two points in  the beginning
                    # are rectilinear or not; if the line they form is parallel to the x or y axes or not.
                    rectilinear = False
                    if si[0] == sj[0] or si[1] == sj[1]:
                        rectilinear = True
                    if rectilinear == False:
                        result = mst_nonrectilinear(st)
                    else:
                        result = mst_rectilinear(st)
                    length = 0
                    for v in result:
                        length += v[2]
                    s.append(length)
    print_solution(s)


def mst_nonrectilinear(st):
    """Gets the k-points that are the subset from which we want to create a MST
    Parameters using Kruskal's Algorithm
    ----------
    st: list
        The subset of k-points

    Returns
    -------
    list
        a list of lists which is the MST of the k-points
        the internal lists contain the edges and the weight between them
    """

    g = Graph(len(st))
    list_points = list()
    n = 0
    for m in st:
        list_points.append([n, m])
        n += 1
    for m in list_points:

        for n in list_points:
            # we add each pair once in the graph BECAUSE THE GRAPH IS UNDIRECTED AND COMPLETE
            if m != n and (g.graph.__contains__(
                    [n[0], m[0], math.sqrt(sum([(a - b) ** 2 for a, b in zip(n[1], m[1])]))]) == False):
                g.addEdge(m[0], n[0], math.sqrt(sum([(a - b) ** 2 for a, b in zip(m[1], n[1])])))
    result = g.KruskalMST()
    return result


def mst_rectilinear(st):
    """Gets the k-points that are the subset from which we want to create a MST
    using Prims's Algorithm
    Parameters
    ----------
    st: list
        The subset of k-points

    Returns
    -------
    list
        a list of lists which is the MST of the k-points
        the internal lists contain the edges and the weight between them
    """

    adj_matrix = []
    for v in st:
        l = []
        for w in st:
            if v == w:
                l.append(0)
            else:
                l.append(math.fabs(v[0] - w[0]) + math.fabs(v[1] - w[1]))
        adj_matrix.append(l)
    g = Graphs(len(st))
    g.graph = adj_matrix
    result = g.primMST()
    return result


def print_solution(s):
    """Gets the lengths of all the MST's we created, calculates the smallest value and prints it on the screen

    Parameters
    ----------
    s: list
        The lengths of all the MST's

    Returns
    -------
    """
    min_length = sys.maxsize
    for solution_value in s:
        if solution_value < min_length:
            min_length = solution_value
    print("The smallest solution value found is:", min_length)


if __name__ == "__main__":
    main()
