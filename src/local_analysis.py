from cvxEDA import cvxEDA
import argparse
import matplotlib.pyplot as plt

# Chose live or non live analysis
# Open a full fine if non live - path specified
# Open an empty or file to append if live
# If not live, choose window width and step
# If live, choose window width and step
# Perform analysis with given window and step
# Output shall be stored in new file unless inplace argument added

# The goal is that this is command line driven using the ArgParse methods

class cvxAnalysis:

    def __init__(self, infile=None, outfile=None, f_s=256):
        self.infile = open(infile, 'r') if infile else None 
        self.sample_rate = f_s 
        self.data = self.infile.read()
        self.dataPoints = [float(x) for x in self.data.strip().split('\n')]
        len_data = len(self.dataPoints)
        self.dataPoints_r = self.dataPoints[:int(len_data/6)]
        print(self.dataPoints) 
        self.plot([self.dataPoints])
    
        # TODO: Speed Testing and optimal window width:
        # r:    Phasic component
        # p:    Sparse SMNA driver of phasic componenet
        # t:    Tonic Component
        # l:    coefficients of tonic spline
        # d:    offset and slope of the linear drift term
        # e:    model residuals
        # obj:  jalue of objective function being minimized (eq15)

        r, p, t, l, d, e, obj = self.applyCVX(self.dataPoints_r)

        self.plot([self.dataPoints_r,r,p,t])

    def set_window(self, window_width):
        self.window=window_width
    
    def applyCVX(self, y):
        [r, p, t, l, d, e, obj] = cvxEDA(y, 1/self.sample_rate)
        return r, p, t, l, d, e, obj
    
    def plot(self, y: list):
        for x in y:
            plt.plot(x)
        plt.show()

        pass

    def cleanup(self):
        self.infile.close()
        self.outfile.close()


# TODO: Implement the argument parsing to allow
# Easy command line usage
class Parser:
    pass

# TODO: Implement GSR Sensor with pi
class GSR_Sensor:
    pass

if __name__ == "__main__":

    print("Running cvx eda analysis")
    
    c = cvxAnalysis(infile='data/c2.csv')

