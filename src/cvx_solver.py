from cvxEDA import cvxEDA
from scipy import stats

# This class implements a method to input data into the cvx solver
# It can support simple list analysis (list of datapoints)
# And windowing with a default window size of 256. This seems to make the analysis
# Run quite quickly, and will hopefully allow near real time solving
class CVX:
    def __init__(self, f_s: int=256):
        """ CVX will take a series and compute the convex optimization.
            Parameters:
            f_s     - sampling rate of data"""
        self.f_s = f_s

    def CVX_list(self, y:list, use_window=False, f_s=None, window=None):
        """ Computes the CVX analysis on a list with the setup samplerate
            Parameters:
                y:list     - a list of the series to be analyzed
                use_window - a boolean to use windowing or not
                f_s        - optional sampling rate - default is instance default 
                window     - a custom window width  - default is instance default 


            Returns: 
                An 2d array containing all CVX parameters of each chunk:
                Number of chunks is 1 if use_window is off

                r  :   Phasic component
                p  :   Sparse SMNA driver of phasic component
                t  :   Tonic Component 
                l  :   Coefficients of tonic spline function
                d  :   Offset and slope of the linear drift term
                e  :   Model Residuals
                obj:   Value of the objective function being minimized (eq15)
            """
        sample_rate = f_s if f_s else self.f_s

        # Datatype to pass in here will become a 2d array so 
        # performance of chunking improves
        data = [y]

        # Using chunking
        if use_window:
            w = window if window else self.window                   # Get window width
            y_chunks = [y[s:s+w] for s in range(0, len(y)-w+1, w)]  # Get most chunks of size w
            r = len(y) % w
            if r != 0:
                y_chunks.append(y[len(y)-len(y)%w:])                # Get last cunk if y%w !=0
            data = y_chunks                                    # this will produce a 2d Array of chunks

        cvx_data = []
        for s in data:
            r, p, t, l, d, e, obj = cvxEDA(s, 1/sample_rate)
            cvx_data.append([r,p,t,l,d,e,obj])

        return r,p,t,l,d,e,obj
    
    # Utilize the information from CVX_List to
    # Create a prediciton
    def predict(self, data):
        data = stats.zscore(data)
        phasic, _, tonic, _, _, _, _ = self.CVX_list(data)
        
        # TODO: Utilize the gradient of the tonic component
        #       To get a better view of what is occuring - is tonic dropping or rising
        # TODO: Utilize gradient of phasic, is phasic activity increasing
        #       or decreasing?
        phasic_av = sum(phasic) / len(phasic)
        tonic_av = sum(tonic) / len(tonic)

        return phasic_av, tonic_av

    
if __name__ == "__main__":
    print("Running cvx eda analysis")
    #c = cvxAnalysis(infile='data/c2.csv')
    c = CVX(256)

    # Opening a datafile to read from
    with open('data/c2.csv', 'r') as f: 
        data = f.read()

    # Testing CVX EDA with no chunking 
    dataPoints = [float(x) for x in data.strip().split('\n')]
    len_data = len(dataPoints)
    out_data = c.CVX_list(dataPoints)
    print(out_data[0][0]) # Print out the phasic component r of chunk 0

    # Testing CVX EDA with default chunk size
    out_data_chunks = c.CVX_list(dataPoints, use_window=True)
    print(out_data.__len__())
