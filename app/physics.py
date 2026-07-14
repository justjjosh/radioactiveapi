import math

def decay_constant(halflife: float) -> float:
    """
    calculate the decay rate(lambda) from the half-life (T1/2)"""
    if halflife <= 0:
        raise ValueError("Half-life must be a positive number.")
    
    return math.log(2) / halflife

def substance_left(initial_amount: float, halflife: float, time: float) -> float:
    """
    Calculate the remaining amount of a substance after a given time based on its half-life.
    
    Parameters:
    initial_amount (float): The initial amount of the substance.
    halflife (float): The half-life of the substance.
    time (float): The time elapsed.
    
    Returns:
    float: The remaining amount of the substance.
    """
    if initial_amount < 0:
        raise ValueError("Initial amount must be a non-negative number.")
    if halflife <= 0:
        raise ValueError("Half-life must be a positive number.")
    if time < 0:
        raise ValueError("Time must be a non-negative number.")
    
    lambda_decay = decay_constant(halflife)
    remaining_amount = initial_amount * math.exp(-lambda_decay * time)
    return remaining_amount
    
