from Regressor import Regressor
import numpy as np
import matplotlib.pyplot as plt
class PolynomialLinearRegressor(Regressor):

    def __init__(self, dataset, y_index, header=False):
        super(PolynomialLinearRegressor, self).__init__(dataset, y_index)
        self.pol_reg = None


    def train(self):
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.linear_model import LinearRegression
        self.pol_reg = PolynomialFeatures(degree = 4)
        X_poly = self.pol_reg.fit_transform(self.X)

        self.regressor = LinearRegression()
        self.regressor.fit(X_poly, self.y)

    def predict(self, *args, **kwargs):
        self.current_test = args
        self.current_result = self.regressor.predict(self.pol_reg.fit_transform(args))
        return self.current_result

    def plot(self):
        if len(self.current_test) == 0 or len(self.current_result) == 0:
            print("No value has been asked to predict")
            return
        print(self.current_test)
        if len(self.current_test[0]) > 1:
            print("YO, Can't plot multivariable dataset!")
            return
        plt.scatter(self.X_train, self.y_train, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.title("Title pls")
        plt.xlabel("x label pls")
        plt.ylabel("y label pls")
        plt.show()


        #print("X = {}\n Y = {}".format(len(self.X), len(self.y)))

        #X_grid = np.arange(min(self.X), max(self.X), 0.01)
        #X_grid = X_grid.reshape(len(X_grid), 1)
        #print("XGrid = {}\n Y = {}".format(len(X_grid), len(self.y)))
        #print( self.regressor.predict(X_grid))
        #plt.scatter(self.X, self.y, color = "red")
        #plt.plot(self.X, self.regressor.predict(self.X), color = "blue")
        #plt.title("Decision Tree Prediction")
        #plt.show()
