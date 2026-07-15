import math
import numpy as np

def decay_constant(halflife: float) -> float:
    """
    calculate the decay rate(lambda) from the half-life (T1/2)"""
    if halflife <= 0:
        raise ValueError("Half-life must be a positive number.")
    
    return math.log(2) / halflife

def quantity_remaining(initial_amount: float, halflife: float, time: float) -> float:
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

def time_until_quantity(initial_amount: float, halflife: float, final_amount: float) -> float:
    if halflife <= 0:
        raise ValueError("Half-life must be a positive number.")
    if initial_amount <= 0:
        raise ValueError("Initial amount must be a positive number.")
    if final_amount <= 0 or final_amount >= initial_amount:
        raise ValueError("Final amount must be a positive number less than the initial amount.")
    
    lambda_decay = decay_constant(halflife)
    time = math.log(initial_amount / final_amount) / lambda_decay
    return time

def sine_wave_points(amplitude: float, frequency: float, duration_seconds: float, n_points: int = 100) -> float:
    """
    Generate n-points(time, value) pair along a sine wave path with given amplitude
    """
    if amplitude < 0:
        raise ValueError("Amplitude must be a non-negative number.")
    if frequency <= 0:
        raise ValueError("Frequency must be a positive number.")
    if duration_seconds <= 0:
        raise ValueError("Duration must be a positive number.")
    
    time = np.linspace(0, duration_seconds, n_points)
    value = amplitude * np.sin(2 * np.pi * frequency * time)
    return time, value

if __name__ == "__main__":
    print(decay_constant(5730)) 
    # Should print ~ 0.000121
    
    print(quantity_remaining(100, 5730, 5730)) 
    # Should print ~ 50.0 (one half-life = half remains)
    
    print(quantity_remaining(100, 5730, 11460)) 
    # Should print ~ 25.0 (two half-lives = quarter remains)

    print(time_until_quantity(100, 5730, 25))
    # Should print ~ 11460 (time for quantity to reduce from 100 to 25)
