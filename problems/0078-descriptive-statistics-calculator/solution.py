import math
from collections import Counter

def descriptive_statistics(data: list) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset
    using pure Python and direct mathematical formulas.
    
    Args:
        data: List of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        25th_percentile, 50th_percentile, 75th_percentile, and interquartile_range.
    """
    if not data:
        raise ValueError("Input data list must not be empty.")

    n = len(data)
    sorted_data = sorted(data)

    # 1. mean: Average of all values
    mean = sum(sorted_data) / n

    # Helper function for percentiles using Linear Interpolation formula: idx = (n - 1) * p
    def calculate_percentile(p: float) -> float:
        idx = (n - 1) * p
        lower_idx = int(idx)
        fraction = idx - lower_idx
        
        if lower_idx + 1 < n:
            return sorted_data[lower_idx] + fraction * (sorted_data[lower_idx + 1] - sorted_data[lower_idx])
        return float(sorted_data[lower_idx])

    # 2. median: Middle value when sorted
    q50 = calculate_percentile(0.50)
    median = q50

    # 3. mode: Most frequently occurring value
    counts = Counter(sorted_data)
    mode = max(counts, key=counts.get)

    # 4. variance: Population variance (divide by N)
    squared_deviations_sum = sum((x - mean) ** 2 for x in sorted_data)
    variance = squared_deviations_sum / n

    # 5. standard_deviation: Square root of variance
    standard_deviation = math.sqrt(variance)

    # 6. 25th_percentile, 50th_percentile, 75th_percentile: Quartile values
    q25 = calculate_percentile(0.25)
    q75 = calculate_percentile(0.75)

    # 7. interquartile_range: Difference between 75th and 25th percentiles (IQR)
    interquartile_range = q75 - q25

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q25,
        "50th_percentile": q50,
        "75th_percentile": q75,
        "interquartile_range": interquartile_range
    }