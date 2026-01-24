import numpy as np
def distance(instance1, instance2):
    return np.linalg.norm(np.subtract(instance1, instance2))

print("%2f"% distance([3, 5], [1, 1]))
