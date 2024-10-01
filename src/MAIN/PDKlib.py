import gdsfactory as gf
from gdsfactory.typings import ComponentSpec

import MAIN
def simple_mzi_mine( 
        length_y: float = 2.0,
        ):
    c = gf.Component()

    # components
    mmi_in = gf.components.mmi2x2()
    mmi_out = gf.components.mmi2x2()
    mmi_out2 = gf.components.mmi2x2()
    bend = gf.components.bend_euler()
    half_delay_straight = gf.components.straight(length=length_y)
    half_delay_straight2 = gf.components.straight(length=2*length_y)
    # references
    mmi_in = c.add_ref(mmi_in, name="mmi_in")
    mmi_out = c.add_ref(mmi_out, name="mmi_out")
    mmi_out2 = c.add_ref(mmi_out2, name="mmi_out")
    straight_top1 = c.add_ref(half_delay_straight, name="straight_top1")
    straight_top2 = c.add_ref(half_delay_straight, name="straight_top2")
    straight_bot11 = c.add_ref(half_delay_straight2, name="straight_top11")
    straight_bot21 = c.add_ref(half_delay_straight2, name="straight_top21")
    bend_top1 = c.add_ref(bend, name="bend_top1")
    bend_top2 = c.add_ref(bend, name="bend_top2").dmirror()
    bend_top3 = c.add_ref(bend, name="bend_top3").dmirror()
    bend_top4 = c.add_ref(bend, name="bend_top4")
    bend_btm1 = c.add_ref(bend, name="bend_btm1").dmirror()
    bend_btm2 = c.add_ref(bend, name="bend_btm2")
    bend_btm3 = c.add_ref(bend, name="bend_btm3")
    bend_btm4 = c.add_ref(bend, name="bend_btm4").dmirror()
    bend_top11 = c.add_ref(bend, name="bend_top11")
    bend_top21 = c.add_ref(bend, name="bend_top21").dmirror()
    bend_top31 = c.add_ref(bend, name="bend_top31").dmirror()
    bend_top41 = c.add_ref(bend, name="bend_top41")
    bend_btm11 = c.add_ref(bend, name="bend_btm1").dmirror()
    bend_btm21 = c.add_ref(bend, name="bend_btm21")
    bend_btm31 = c.add_ref(bend, name="bend_btm31")
    bend_btm41 = c.add_ref(bend, name="bend_btm41").dmirror()
    # connections
    bend_top1.connect("o1", mmi_in.ports["o3"])
    straight_top1.connect("o1", bend_top1.ports["o2"])
    bend_top2.connect("o1", straight_top1.ports["o2"])
    bend_top3.connect("o1", bend_top2.ports["o2"])
    straight_top2.connect("o1", bend_top3.ports["o2"])
    bend_top4.connect("o1", straight_top2.ports["o2"])

    bend_btm1.connect("o1", mmi_in.ports["o4"])
    bend_btm2.connect("o1", bend_btm1.ports["o2"])
    bend_btm3.connect("o1", bend_btm2.ports["o2"])
    bend_btm4.connect("o1", bend_btm3.ports["o2"])

    mmi_out.connect("o1", bend_btm4.ports["o2"])

    bend_top11.connect("o1", mmi_out.ports["o3"])
    bend_top21.connect("o1", bend_top11.ports["o2"])
    bend_top31.connect("o1", bend_top21.ports["o2"])
    bend_top41.connect("o1", bend_top31.ports["o2"])

    bend_btm11.connect("o1", mmi_out.ports["o4"])
    straight_bot11.connect("o1", bend_btm11.ports["o2"])
    bend_btm21.connect("o1", straight_bot11.ports["o2"])
    bend_btm31.connect("o1", bend_btm21.ports["o2"])
    straight_bot21.connect("o1", bend_btm31.ports["o2"])
    bend_btm41.connect("o1", straight_bot21.ports["o2"])

    mmi_out2.connect("o1", bend_btm41.ports["o2"])
    # ports
    c.add_port("o1", port=mmi_in.ports["o1"])
    c.add_port("o2", port=mmi_in.ports["o2"])
    c.add_port("o3", port=mmi_out2.ports["o3"])
    c.add_port("o4", port=mmi_out2.ports["o4"])
    return c