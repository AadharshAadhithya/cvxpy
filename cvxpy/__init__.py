"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = "0.2.15"
from cvxpy.atoms import *
from cvxpy.expressions.variables import Variable, Semidef, BoolVar, IntVar
from cvxpy.expressions.constants import Parameter, CallbackParam, Constant
from cvxpy.problems.problem import Problem
from cvxpy.problems.objective import Maximize, Minimize
import cvxpy.interface.numpy_wrapper
from cvxpy.error import SolverError
from cvxpy.settings import (CVXOPT, ECOS, SCS,
OPTIMAL, UNBOUNDED, INFEASIBLE, SOLVER_ERROR,
OPTIMAL_INACCURATE, UNBOUNDED_INACCURATE, INFEASIBLE_INACCURATE)

# Legacy names.
from cvxpy.expressions.variables.semidefinite import Semidef as semidefinite
