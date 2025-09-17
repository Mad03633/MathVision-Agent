from sympy import sympify, Eq, solveset, S, simplify
from sympy.parsing.latex import parse_latex
from sympy.core.sympify import SympifyError
from sympy import symbols


class MathSolver:
    def parse_expression(self, expr: str, is_latex: bool = False):
        try: 
            return parse_latex(expr) if is_latex else sympify(expr)
        except Exception as e:
            raise ValueError(f"Failed to parse expression: {e}")

    def simplify(self, left: str, right: str = "0", var: str | None = None, is_latex: bool = False):
            try:
                l = self.parse_expression(left, is_latex=is_latex)
                r = self.parse_expression(right, is_latex=is_latex)
                equation = Eq(l, r)
                if var:
                    sym = symbols(var)
                    sol = solveset(equation, sym, domain=S.Complexes)
                else:
                    sol = solveset(equation, domain=S.Complexes)
                return str(sol)
            except SympifyError as e:
                raise ValueError(f"Invalid expression: {e}")
            except Exception as e:
                raise ValueError(f"Failed to solve: {e}")