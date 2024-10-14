..  _Problem_Minimum_Multi_Cut:

Minimum Multi Cut Problem
=========================

Minimum Multi Cut problem is the NP-hard problem of finding the minimum multi cut in a graph. 

## Problem Definition

- **Instance:** A graph G(V, E), a set S ⊆ V × V of source-terminal pairs, and a weight function w: E → N.

- **Solution:** Find a multi-cut E' ⊆ E such that removing E' disconnects each source s from its corresponding terminal t for every pair (s, t) ∈ S.

- **Measure:** Minimize the weight of the cut, defined as the sum of weights in E'

* Minimum Multi Cut Problem. Problem is represented with class :ref:`MinMultiCutProblemProblem<py_minimum_multi_cut_problem>`.

    - `BitArray` representation for solution of Max Ones Problem. Implementation of the solution with such representation is given with class :ref:`MinMultiCutProblemProblemBitArraySolution <py_minimum_multi_cut_problem_bit_array_solution>`.  


