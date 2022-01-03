import math

class expression:
    def __init__(self,a,b,c):
        self.term1 = a
        self.term2 = b
        self.term3 = c
        self.variable = "x"
    def describe(self,Var):
        self.variable = Var
        expr = f"{self.term1} * {self.variable} ** 2 + {self.term2} * {self.variable} + {self.term3}"
        return expr
    def eval(self,num):
        answer = self.term1 * num ** 2 + self.term2 * num + self.term3
        return answer


class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.expression = expression(a, b, c)
    def formula(self):
        sol1 = -self.b - math.sqrt(abs(self.b ** 2 - 4 * self.a * self.c))
        sol2 = -self.b + math.sqrt(abs(self.b ** 2 - 4 * self.a * self.c))
        x = sol1 / 2 * self.a
        x2 = sol2 / 2 * self.a
        solutions = [x, x2]
        return solutions
    def factor(self):
        global i, fact
        fact = 0
        i = 0
        if self.a == 1:
            for i in range(-abs(self.c), abs(self.c)):
                if i == 0:
                    i = 1
                if self.c % i == 0:
                    fact = self.c / i
                    bb = fact + i
                    cb = fact * i
                    if bb == self.b and cb == self.c:
                        break
        fact = -fact
        i = -i
        if self.a > 1:
            mult = self.a * self.c
            for i in range(-abs(mult), abs(mult)):
                if i == 0:
                    i = 1
                if mult % i == 0:
                    fact = mult / i
                    bb = fact + i
                    cb = fact * i
                    if bb == self.b and cb == mult:
                        break
            def hcfnaive(a, b):
                if (b == 0):
                    return a
                else:
                    return hcfnaive(b, a % b)
            fac1 = abs(hcfnaive(self.a, fact))
            fac2 = abs(hcfnaive(self.a, i))
            answer = f"({self.a / fac1}x {fact / fac1})({self.a / fac2}x {i / fac2})"
            fact = -(fact / fac1) / (self.a / fac1)
            i = -(i / fac2) / (self.a / fac2)
        return [fact, i]

equation = quadratic(1, -9, 20)

print(equation.formula())
print(equation.factor())

print(equation.expression.describe("d"))
print(equation.expression.eval(10))

equation2 = quadratic(5, -9, 4)

print(equation2.factor())

equation3 = quadratic(10,-11,3)

print(equation3.factor())

solving = quadratic(-16,89,197)

print(solving.factor())

quad = quadratic(1,1,-20)

print(quad.factor())