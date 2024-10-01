import gdsfactory as gf
from gdsfactory.typings import ComponentSpec

import MAIN

def component_placement(
    die: gf.Component,
) -> gf.Component:
    """This function places the components in the DIE"""

    die = gf.get_component(die)
    mzi = die << MAIN.simple_mzi_mine(length_y=100.0)
    mzi.dmove((100, 50))
    

