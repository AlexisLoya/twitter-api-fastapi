from typing import TypeVar, Generic, Dict, Optional, List
T = TypeVar('T')

def function_to_dict(f: Generic[T], dict: Dict) -> None:
    """
    Function in a dictionary.

    This function iterates to a dictionary and applies the function of the parameter.

    Parameters:
    - **f: Generic[T]**: The function to apply. For example a lamba function.
    - **dict: Dict**: The dictionary in which to apply the function.

    Returns
    - **None**
    """
    for key, val in dict.items():
        dict[key] = f(val)