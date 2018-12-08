from Regressor import Regressor
from PolynomialLinearRegressor import PolynomialLinearRegressor
from SVRRegressor import SVRRegressor
from SimpleLinearRegressor import SimpleLinearRegressor


def test_simple_linear():
    simpleR = SimpleLinearRegressor("Salary_Data.csv", 1)
    #simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    simpleR.plot()

    simpleR = SimpleLinearRegressor("Position_Salaries.csv", 2)
    simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    simpleR.plot()

    simpleR = SimpleLinearRegressor("50_Startups.csv", 4)
    #simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1, 300, 4000, 3])
    simpleR.plot()

def test_polinomial_linear():
    regressor = PolynomialLinearRegressor("Salary_Data.csv", 1)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()

    regressor = PolynomialLinearRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()

    regressor = PolynomialLinearRegressor("50_Startups.csv", 4)
    regressor.train()
    regressor.predict([1,3, 400, 3])
    regressor.plot()

def test_svr():
    regressor = SVRRegressor("Salary_Data.csv", 1)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()

    regressor = SVRRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()

    regressor = SVRRegressor("50_Startups.csv", 4)
    regressor.train()
    regressor.predict([1,3, 400, 3])
    regressor.plot()

if __name__ == "__main__":
    test_simple_linear()
    test_polinomial_linear()
    test_svr()
    """val = 13
    regressor = Regressor("Position_Salaries.csv", 2)

    regressor.remove_variable(0)

    val = 13

    regressor.train()
    #print(regressor.predict([val]))

    simpleR = SimpleLinearRegressor("Salary_Data.csv", 1)
    #simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    simpleR.plot()

    regressor2 = PolynomialLinearRegressor("Position_Salaries.csv", 2)
    regressor2.print_X()
    regressor2.remove_variable(0)
    regressor2.train()
    print(regressor.predict([val]))
    print(regressor2.predict([val]))

    #regressor.plot()
    #regressor2.plot()
    svr = SVRRegressor("Position_Salaries.csv", 2)"""
    #svr.print_X()
    #svr.remove_variable(0)
    #svr.print_X()
    #svr.train()
    #print(svr.predict([val]))