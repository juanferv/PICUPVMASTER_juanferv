import datetime

import gdsfactory as gf

import MAIN




# die definition
die_name = "MAIN"
DIE = gf.Component(die_name)

# borders
die_border = DIE << gf.components.die(
    size=[10000.0, 5000.0],
    die_name=None,
    bbox_layer=None,
    draw_corners=False,
)

# Component Placement
MAIN.component_placement(die=DIE)


DIE.show()

dirpath = "gds/"  # noqa: E501

current_time = datetime.datetime.now()


DIE.write_gds(
    f"{dirpath}/DIE_MAIN_{current_time.day}_{current_time.month}_{current_time.year}_PICUPV.gds"
)