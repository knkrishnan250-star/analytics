import numpy as np

def simulate_federated_learning(data, num_clients=3):
    splits = np.array_split(data, num_clients)
    
    local_means = [split.mean() for split in splits if len(split) > 0]
    
    global_mean = sum(local_means) / len(local_means)
    
    return {
        "local_means": local_means,
        "global_mean": global_mean
    }