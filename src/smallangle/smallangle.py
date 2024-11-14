import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option("-n", "--number", default = 10)
def sin(number):
    """Gives you the sine of NUMBER points between 0 and 2pi

    Args:
        number (int): The amount of points between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option("-n", "number", default = 10)
def tan(number):
    """Gives you the tangent of NUMBER points between 0 and 2pi

    Args:
        number (int): The amount of points between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()
 