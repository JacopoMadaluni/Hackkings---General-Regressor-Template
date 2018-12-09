from Regressor import Regressor
from PolynomialLinearRegressor import PolynomialLinearRegressor
from SVRRegressor import SVRRegressor
from SimpleLinearRegressor import SimpleLinearRegressor
from DecisionTreeRegressor import DecisionTreeRegressor
from RandomForestRegressor import RandomForestRegressor
import sys

class Controller:

    def __init__(self):
        self.file = ""
        self.y_index = -1
        self.to_ignore = []

    def get_all_regressors(self, dataset, y_index):
        sl = SimpleLinearRegressor(dataset, y_index)
        pl = PolynomialLinearRegressor(dataset, y_index)
        dt = DecisionTreeRegressor(dataset, y_index)
        rf = RandomForestRegressor(dataset, y_index)
        return [sl, pl, dt, rf]


    def add_to_ignore(self, index, reader):
        if len(self.to_ignore) + 2 >= len(reader.get_headers_names()):
            print("you need at least 2 variables")
        elif index == self.y_index:
            print("you can't ignore y values")
        else:
            if not self.to_ignore:
                self.to_ignore.append(index)
            else:
                if index not in self.to_ignore:
                    self.to_ignore.append(index)
                    self.to_ignore.sort(reverse=True)

        print(self.to_ignore)

    def get_choices(self, dataset):
        pass

    def remove_toignore_from(self, regressor):
        for i in self.to_ignore:
            regressor.remove_variable(i)

    def get_best_regressor(self):
        if self.file == "" or self.y_index == -1:
            return None

        regressors = self.get_all_regressors(self.file, self.y_index)
        min_error = 10000000000
        current_best = None
        for regressor in regressors:
            self.remove_toignore_from(regressor)
            error = regressor.get_average_error()
            if (error < min_error):
                min_error = error
                current_best = regressor
        return current_best

    def set_file(self, file):
        self.file = file
    def set_y_index(self, y_index):
        self.y_index = y_index
