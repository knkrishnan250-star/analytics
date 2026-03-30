import numpy as np

def add_laplace_noise(value, sensitivity=1.0, epsilon=1.0):
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return value + noise

def add_gaussian_noise(value, sensitivity=1.0, epsilon=1.0):
    sigma = sensitivity / epsilon
    noise = np.random.normal(0, sigma)
    return value + noise

def private_count(series, epsilon=1.0):
    true_count = len(series)
    return add_laplace_noise(true_count, sensitivity=1, epsilon=epsilon)


def private_sum(series, epsilon=1.0):
    sensitivity = series.max() - series.min()
    true_sum = series.sum()
    return add_laplace_noise(true_sum, sensitivity, epsilon)

def private_mean(series, epsilon=1.0, mechanism="laplace"):
    sensitivity = (series.max() - series.min()) / len(series)
    true_mean = series.mean()

    if mechanism == "gaussian":
        return add_gaussian_noise(true_mean, sensitivity, epsilon)
    return add_laplace_noise(true_mean, sensitivity, epsilon)




def private_histogram(series, bins=5, epsilon=1.0):
    counts, bin_edges = np.histogram(series, bins=bins)
    noisy_counts = [
        add_laplace_noise(count, sensitivity=1, epsilon=epsilon)
        for count in counts
    ]
    return noisy_counts, bin_edges.tolist()