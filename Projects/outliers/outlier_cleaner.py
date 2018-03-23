
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    data_with_error = [(age[0], net_worth[0], (net_worth[0]-prediction[0])**2) for (prediction, age, net_worth) in zip(predictions, ages, net_worths)]
    data_with_error_sorted = sorted(data_with_error, key=lambda tup: tup[2])
    limit = int(len(data_with_error_sorted)*0.9)
    cleaned_data = data_with_error_sorted[:limit]
    return cleaned_data

