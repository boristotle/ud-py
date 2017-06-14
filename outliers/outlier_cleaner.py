#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    print('outlier cleaner code running', predictions[0] - net_worths[0])
    for a, n, p in zip(ages, predictions, net_worths):
        if (p[0] - n[0] < 52):
            cleaned_data.append((a[0], n[0], p[0] - n[0]))
    print('cleaned_data', cleaned_data)
    print('len', len(cleaned_data))
    return cleaned_data

