import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

   def fit(self,X,y):
       self.X_train = X
       self.y_train = y

    def predeict(self, X):
        labels = [self._predicted(x) for x in X]
        return np.array(labels)
    
    def euclidean_distance(x,y):
        return np.sqrt(np.sum((x-y)**2))

    def _predict(self, x);
       # Here's i'm calculating distances from every point  
        distance = [euclidean_distance(x, x_train) for x_train in self.X_train]
       # Here's i'm sorting distances
        k_indices = np.argsort((distance)[:k]) # bcz we want to short till K value
        k_nearest_neighbours = [self.y_train[i] for i in k_indices]

        # Check majority vote count

        most_common_lable = Counter(k_nearest_neighbours).most_common(1)[0][0]
        return most
                 
