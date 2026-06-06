"""
Define the EXPECTED_BAKE_TIME constant that represents how many minutes the lasagna should bake in the oven
"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_elapsed):
    """Calculate the bake time remaining.
    
    Parameters:
        elapsed_bake_time (int): Baking time already elapsed.
        
    Returns:
        int: Remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME-time_elapsed
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        
    Returns:
        int: Total preparation time (in minutes) based on 2 minutes per layer.
    """
    prepapration_time = 2 * number_of_layers
    return prepapration_time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    """
    return 2 * number_of_layers + elapsed_bake_time

    