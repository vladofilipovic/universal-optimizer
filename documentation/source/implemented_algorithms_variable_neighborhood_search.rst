..  _Algorithm_Variable_Neighborhood_Search:

Variable Neighborhood Search
============================

Basic information 
-----------------

Variable Neighborhood Search (denoted as VNS) is proposed by Mladenović and Hansen [MlaHan1997]_ is a metaheuristic method for solving a set of combinatorial optimization and global optimization problems. It explores distant *neighborhoods* of the current incumbent solution, and moves from there to a new one if and only if an improvement was made. The local search method is applied repeatedly to get from solutions in the neighborhood to local optima. 

VNS systematically changes the neighborhood in two phases: firstly, descent to find a local optimum and finally, a perturbation phase to get out of the corresponding valley.

Applications are rapidly increasing in number and pertain to many fields: location theory, cluster analysis, scheduling, vehicle routing, network design, lot-sizing, artificial intelligence, engineering, pooling problems, biology, phylogeny, reliability, geometry, telecommunication design, etc.

There are several books important for understanding VNS, like Handbook of Metaheuristics [GenPot2010]_ , Handbook of Metaheuristics [GloKoc2003]_ and Search methodologies [BurKen2005]_.

Structure of the algorithm
--------------------------

According to authors, VNS systematically performs the procedure of neighborhood change, both in descent to local minima and in escape from the valleys which contain them.

VNS is built upon the following perceptions:

1. A local minimum with respect to one neighborhood structure is not necessarily a local minimum for another neighborhood structure.

2. A global minimum is a local minimum with respect to all possible neighborhood structures.

3. For many problems, local minima with respect to one or several neighborhoods are relatively close to each other.

The main steps in VNS are:

- **Local search**: it is performed through choosing an initial solution *x*, discovering a direction of descent from *x*, within a given neighborhood  *k*, and proceeding to the minimum of *f(x)* within that neighborhood in the same direction. If there is no direction of descent, the heuristic stops; otherwise, it is iterated. Usually the highest direction of descent, also related to as best improvement, is used. 

- **Shaking**:  typically, it involves the random extraction of a feasible solution within current neighborhood *k*. 

- **Neighborhood change**: it compares the new value *f(x')* with the incumbent value *f(x)* obtained in the neighborhood *k*. If an improvement is obtained, *k* is returned to its initial value and the new incumbent updated. Otherwise, the next neighborhood is considered.

In-depth structure of the VNS and its various variants is given in following `document <https://www.cs.uleth.ca/~benkoczi/OR/read/vns-tutorial.pdf>`_.

Implementation notes
--------------------

Implementation of that optimization method is given within the class :ref:`VnsOptimizer<py_vns_optimizer>`.


References
----------

.. [MlaHan1997] Mladenović, N.; Hansen P. (1997). "Variable neighborhood search". Computers and Operations Research. 24 (11): 1097–1100. CiteSeerX 10.1.1.800.1797. doi:10.1016/s0305-0548(97)00031-2.

.. [GenPot2010] Gendreau, M.; Potvin, J-Y. (2010). "Handbook of Metaheuristics". Springer.

.. [GloKoc2003] Glover, F.; Kochenberger, G.A. (2003). "Handbook of Metaheuristics". Kluwer Academic Publishers.

.. [BurKen2005] Burke, EK.; Kendall, G. (2005). Burke, Edmund K; Kendall, Graham (eds.). Search methodologies. Introductory tutorials in optimization and decision support techniques. Springer. doi:10.1007/978-1-4614-6940-7. ISBN 978-1-4614-6939-1.