class Neural_Network(object):
    def __init__(self):
        #Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
        
        #Weights (Parameters)
        self.W1 = np.random.randn(self.inputLayerSize,
                                 self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,
                                 self.outputLayerSize)
        
    def forward(self, X):
        #Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat
        
    def sigmoid(z):
    #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))    