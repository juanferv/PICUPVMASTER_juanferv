import datetime

import gdsfactory as gf

import TEST

# die definition
die_name = "TEST"
DIE = gf.Component(die_name)

# borders
die_border = DIE << gf.components.die(
    size=[2500.0, 5000.0],
    die_name=None,
    bbox_layer=None,
    draw_corners=False,
)

# Component Placement
TEST.component_placement(die=DIE)


DIE.show()

dirpath = "gds/"  # noqa: E501

current_time = datetime.datetime.now()


DIE.write_gds(
    f"{dirpath}/DIE_TEST_{current_time.day}_{current_time.month}_{current_time.year}_PICUPV.gds"
)