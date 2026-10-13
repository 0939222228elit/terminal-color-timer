def get_color_code(color):
    """
    Get the ANSI color code for the specified color.

    Args:
        color (str): The color name ('red', 'green', 'yellow', or 'reset').

    Returns:
        str: The ANSI color code.
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'reset': '\033[0m'
    }
    return colors.get(color, colors['reset'])