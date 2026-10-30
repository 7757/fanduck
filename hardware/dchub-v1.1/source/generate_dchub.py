#!/usr/bin/env python3
"""Generate the deterministic KiCad source files for the Microduck DCHUB.

This is a passive four-port Dynamixel TTL/power distribution board.  It is a
clean-room redraw based on the owner's topology request and the public JST
connector geometry; it does not copy the shared EasyEDA project's artwork.
"""

from __future__ import annotations

import csv
import json
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = "dchub_4port_strip_v1_1"
NS = uuid.UUID("73ed6eb8-b76b-43e0-aeb9-402f08ea7e76")


def uid(name: str) -> str:
    return str(uuid.uuid5(NS, name))


def effects(size: float = 0.8, thickness: float = 0.12, *, mirror: bool = False) -> str:
    justify = "\n      (justify mirror)" if mirror else ""
    return f"""(effects
      (font
        (size {size:g} {size:g})
        (thickness {thickness:g})
      ){justify}
    )"""


def property_block(ref: str, value: str, description: str, name: str) -> str:
    return f"""  (property \"Reference\" \"{ref}\"
    (at 0 0 0)
    (layer \"F.Fab\")
    (hide yes)
    (uuid \"{uid(name + '-ref')}\")
    {effects(0.7, 0.1)}
  )
  (property \"Value\" \"{value}\"
    (at 0 0 0)
    (layer \"F.Fab\")
    (hide yes)
    (uuid \"{uid(name + '-value')}\")
    {effects(0.7, 0.1)}
  )
  (property "Description" "{description}"
    (at 0 0 0)
    (layer "F.Fab")
    (hide yes)
    (uuid "{uid(name + '-description')}")
    {effects(0.7, 0.1)}
  )"""


def jst_footprint(ref: str, role: str, x: float, y: float, angle: int = 0) -> str:
    name = ref.lower()
    return f"""(footprint \"DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical\"
  (layer \"F.Cu\")
  (uuid \"{uid(name)}\")
  (at {x:g} {y:g} {angle})
  (descr \"JST EH B3B-EH-A, 3 positions, 2.50 mm pitch, vertical THT\")
  (tags \"JST EH B3B-EH-A X3P Dynamixel\")
{property_block(ref, 'B3B-EH-A(LF)(SN)', 'Parallel X3P port: pin 1 GND, pin 2 VBATT, pin 3 DATA', name)}
  (property \"Role\" \"{role}\"
    (at 0 0 0)
    (layer \"F.Fab\")
    (hide yes)
    (uuid \"{uid(name + '-role')}\")
    {effects(0.7, 0.1)}
  )
  (property \"Manufacturer\" \"JST\"
    (at 0 0 0)
    (layer \"F.Fab\")
    (hide yes)
    (uuid \"{uid(name + '-manufacturer')}\")
    {effects(0.7, 0.1)}
  )
  (property \"MPN\" \"B3B-EH-A(LF)(SN)\"
    (at 0 0 0)
    (layer \"F.Fab\")
    (hide yes)
    (uuid \"{uid(name + '-mpn')}\")
    {effects(0.7, 0.1)}
  )
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_line (start -2.91 0.11) (end -2.91 2.61)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s1')}\"))
  (fp_line (start -2.91 2.61) (end -0.41 2.61)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s2')}\"))
  (fp_line (start -2.61 0) (end -2.11 0)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s3')}\"))
  (fp_line (start -2.61 0.81) (end -1.61 0.81)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s4')}\"))
  (fp_line (start -2.11 -1.21) (end 7.11 -1.21)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s5')}\"))
  (fp_line (start -2.11 0) (end -2.11 -1.21)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s6')}\"))
  (fp_line (start -1.61 0.81) (end -1.61 2.31)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s7')}\"))
  (fp_line (start 6.61 0.81) (end 6.61 2.31)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s8')}\"))
  (fp_line (start 7.11 -1.21) (end 7.11 0)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s9')}\"))
  (fp_line (start 7.11 0) (end 7.61 0)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s10')}\"))
  (fp_line (start 7.61 0.81) (end 6.61 0.81)
    (stroke (width 0.12) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-s11')}\"))
  (fp_rect (start -2.61 -1.71) (end 7.61 2.31)
    (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\") (uuid \"{uid(name + '-srect')}\"))
  (fp_rect (start -3 -2.1) (end 8 2.7)
    (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\") (uuid \"{uid(name + '-courtyard')}\"))
  (fp_rect (start -2.5 -1.6) (end 7.5 2.2)
    (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\") (uuid \"{uid(name + '-fab')}\"))
  (pad \"1\" thru_hole roundrect
    (at 0 0)
    (size 1.8 2.0)
    (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (roundrect_rratio 0.14)
    (net \"GND\")
    (pinfunction \"GND\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad1')}\")
  )
  (pad \"2\" thru_hole oval
    (at 2.5 0)
    (size 1.8 2.0)
    (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (net \"VBATT\")
    (pinfunction \"VBATT\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad2')}\")
  )
  (pad \"3\" thru_hole oval
    (at 5 0)
    (size 1.8 2.0)
    (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (net \"DATA\")
    (pinfunction \"DATA\")
    (pintype \"passive\")
    (uuid \"{uid(name + '-pad3')}\")
  )
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Connector_JST.3dshapes/JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical.step\"
    (offset (xyz 0 0 0))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )
)"""


def jst_rot90_footprint(ref: str, role: str, x: float, y: float) -> str:
    """A pre-rotated JST footprint, kept at board angle zero for library parity."""
    name = ref.lower()
    return f"""(footprint \"DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90\"
  (layer \"F.Cu\")
  (uuid \"{uid(name)}\")
  (at {x:g} {y:g})
  (descr \"JST EH B3B-EH-A, vertical board layout, 2.50 mm pitch\")
  (tags \"JST EH B3B-EH-A X3P Dynamixel rotated\")
{property_block(ref, 'B3B-EH-A(LF)(SN)', 'Parallel X3P port: pin 1 GND, pin 2 VBATT, pin 3 DATA', name)}
  (property \"Role\" \"{role}\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-role')}\") {effects(0.7, 0.1)})
  (property \"Manufacturer\" \"JST\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-manufacturer')}\") {effects(0.7, 0.1)})
  (property \"MPN\" \"B3B-EH-A(LF)(SN)\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-mpn')}\") {effects(0.7, 0.1)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_rect (start -2.31 -2.61) (end 1.71 7.61)
    (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\") (uuid \"{uid(name + '-srect')}\"))
  (fp_line (start -2.31 -2.61) (end -0.81 -2.61)
    (stroke (width 0.3) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-pin1mark')}\"))
  (fp_rect (start -2.7 -3) (end 2.1 8)
    (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\") (uuid \"{uid(name + '-courtyard')}\"))
  (fp_rect (start -2.2 -2.5) (end 1.6 7.5)
    (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\") (uuid \"{uid(name + '-fab')}\"))
  (pad \"1\" thru_hole roundrect (at 0 0) (size 1.8 2.0) (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\") (remove_unused_layers no) (roundrect_rratio 0.14)
    (net \"GND\") (pinfunction \"GND\") (pintype \"passive\") (zone_connect 2)
    (uuid \"{uid(name + '-pad1')}\"))
  (pad \"2\" thru_hole oval (at 0 2.5) (size 2.0 1.8) (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\") (remove_unused_layers no)
    (net \"VBATT\") (pinfunction \"VBATT\") (pintype \"passive\") (zone_connect 2)
    (uuid \"{uid(name + '-pad2')}\"))
  (pad \"3\" thru_hole oval (at 0 5) (size 2.0 1.8) (drill 0.95)
    (layers \"*.Cu\" \"*.Mask\") (remove_unused_layers no)
    (net \"DATA\") (pinfunction \"DATA\") (pintype \"passive\")
    (uuid \"{uid(name + '-pad3')}\"))
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Connector_JST.3dshapes/JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical.step\"
    (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 90)))
)"""


def terminal_footprint() -> str:
    name = "j5"
    return f"""(footprint \"DCHUB:KF301-5.0-2P\"
  (layer \"F.Cu\")
  (uuid \"{uid(name)}\")
  (at 138 106.5)
  (descr \"Generic KF301-compatible 2-position 5.00 mm pitch screw terminal\")
  (tags \"KF301 5.0mm screw terminal THT\")
{property_block('J5', 'KF301-5.0-2P', 'Unregulated battery input', name)}
  (property \"Role\" \"BATTERY INPUT\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-role')}\") {effects(0.7, 0.1)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_rect (start -3.8 -5) (end 3.8 5)
    (stroke (width 0.15) (type solid)) (fill no) (layer \"F.SilkS\") (uuid \"{uid(name + '-outline')}\"))
  (fp_line (start 2.5 -5) (end 2.5 5)
    (stroke (width 0.15) (type solid)) (layer \"F.SilkS\") (uuid \"{uid(name + '-wire-side')}\"))
  (fp_rect (start -4.1 -5.3) (end 4.1 5.3)
    (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\") (uuid \"{uid(name + '-courtyard')}\"))
  (fp_rect (start -3.8 -5) (end 3.8 5)
    (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\") (uuid \"{uid(name + '-fab')}\"))
  (pad \"1\" thru_hole roundrect
    (at 0 2.5)
    (size 2.5 2.5)
    (drill 1.4)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (roundrect_rratio 0.15)
    (net \"GND\")
    (pinfunction \"GND\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad1')}\")
  )
  (pad \"2\" thru_hole circle
    (at 0 -2.5)
    (size 2.5 2.5)
    (drill 1.4)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (net \"VBATT\")
    (pinfunction \"VBATT\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad2')}\")
  )
  (embedded_fonts no)
)"""


def capacitor_footprint() -> str:
    name = "c1"
    return f"""(footprint \"DCHUB:CP_Radial_D8.0mm_P3.50mm_Vertical\"
  (layer \"F.Cu\")
  (uuid \"{uid(name)}\")
  (at 126.5 104.75)
  (descr \"Polarized radial electrolytic, 8 mm diameter, 3.50 mm lead pitch\")
  (tags \"470uF 16V low impedance radial electrolytic\")
{property_block('C1', '470uF 16V', 'Polarized bulk capacitor', name)}
  (property \"Manufacturer\" \"Panasonic\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-manufacturer')}\") {effects(0.7, 0.1)})
  (property \"MPN\" \"EEU-FR1C471\" (at 0 0 0) (layer \"F.Fab\") (hide yes)
    (uuid \"{uid(name + '-mpn')}\") {effects(0.7, 0.1)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_circle (center 0 1.75) (end 4.08 1.75)
    (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\") (uuid \"{uid(name + '-silk-circle')}\"))
  (fp_circle (center 0 1.75) (end 4.25 1.75)
    (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\") (uuid \"{uid(name + '-courtyard')}\"))
  (fp_circle (center 0 1.75) (end 4 1.75)
    (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\") (uuid \"{uid(name + '-fab')}\"))
  (pad \"1\" thru_hole rect
    (at 0 0)
    (size 2.2 2.2)
    (drill 0.9)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (net \"VBATT\")
    (pinfunction \"+\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad1')}\")
  )
  (pad \"2\" thru_hole circle
    (at 0 3.5)
    (size 2.2 2.2)
    (drill 0.9)
    (layers \"*.Cu\" \"*.Mask\")
    (remove_unused_layers no)
    (net \"GND\")
    (pinfunction \"-\")
    (pintype \"passive\")
    (zone_connect 2)
    (uuid \"{uid(name + '-pad2')}\")
  )
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Capacitor_THT.3dshapes/CP_Radial_D8.0mm_P3.50mm.step\"
    (offset (xyz 0 0 0))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 90))
  )
)"""


def gr_text(text: str, x: float, y: float, name: str, *, layer: str = "F.SilkS", size: float = 0.75,
            thickness: float = 0.12, angle: int = 0, mirror: bool = False) -> str:
    return f"""(gr_text \"{text}\"
  (at {x:g} {y:g} {angle})
  (layer \"{layer}\")
  (uuid \"{uid('text-' + name)}\")
  {effects(size, thickness, mirror=mirror)}
)"""


def segment(x1: float, y1: float, x2: float, y2: float, width: float, layer: str, net: str, name: str) -> str:
    return f"""(segment
  (start {x1:g} {y1:g})
  (end {x2:g} {y2:g})
  (width {width:g})
  (layer \"{layer}\")
  (net \"{net}\")
  (uuid \"{uid('seg-' + name)}\")
)"""


def edge_line(x1: float, y1: float, x2: float, y2: float, name: str) -> str:
    return f"""(gr_line
  (start {x1:g} {y1:g})
  (end {x2:g} {y2:g})
  (stroke (width 0.05) (type solid))
  (layer \"Edge.Cuts\")
  (uuid \"{uid('edge-' + name)}\")
)"""


def edge_arc(start: tuple[float, float], mid: tuple[float, float], end: tuple[float, float], name: str) -> str:
    return f"""(gr_arc
  (start {start[0]:g} {start[1]:g})
  (mid {mid[0]:g} {mid[1]:g})
  (end {end[0]:g} {end[1]:g})
  (stroke (width 0.05) (type solid))
  (layer \"Edge.Cuts\")
  (uuid \"{uid('edge-' + name)}\")
)"""


def zone(net: str, layer: str, name: str) -> str:
    return f"""(zone
  (net \"{net}\")
  (layer \"{layer}\")
  (uuid \"{uid('zone-' + name)}\")
  (name \"{name}\")
  (hatch edge 0.5)
  (connect_pads (clearance 0.3))
  (min_thickness 0.25)
  (fill yes
    (thermal_gap 0.3)
    (thermal_bridge_width 0.8)
    (island_removal_mode 0)
  )
  (polygon
    (pts
      (xy 100.3 100.3) (xy 142.7 100.3) (xy 142.7 112.7) (xy 100.3 112.7)
    )
  )
)"""


def make_board() -> str:
    footprints = [
        # The physical body centres of every part sit on the board's
        # horizontal centreline, y=106.5 mm.  The rotated JST body's centre is
        # 2.5 mm below its footprint origin; the capacitor body's centre is
        # 1.75 mm below its positive-pin origin.
        jst_rot90_footprint("J1", "BUS / HAT", 103.2, 104.0),
        jst_rot90_footprint("J2", "LEFT LEG", 108.5, 104.0),
        jst_rot90_footprint("J3", "RIGHT LEG", 113.8, 104.0),
        jst_rot90_footprint("J4", "HEAD / NECK", 119.1, 104.0),
        capacitor_footprint(),
        terminal_footprint(),
    ]

    edges = [
        edge_line(101.5, 100, 141.5, 100, "top"),
        edge_arc((141.5, 100), (142.56066, 100.43934), (143, 101.5), "top-right"),
        edge_line(143, 101.5, 143, 111.5, "right"),
        edge_arc((143, 111.5), (142.56066, 112.56066), (141.5, 113), "bottom-right"),
        edge_line(141.5, 113, 101.5, 113, "bottom"),
        edge_arc((101.5, 113), (100.43934, 112.56066), (100, 111.5), "bottom-left"),
        edge_line(100, 111.5, 100, 101.5, "left"),
        edge_arc((100, 101.5), (100.43934, 100.43934), (101.5, 100), "top-left"),
    ]

    texts = [
        gr_text("+", 132.7, 104.0, "terminal-plus", size=0.8, thickness=0.15),
        gr_text("-", 132.7, 109.0, "terminal-minus", size=0.8, thickness=0.15),
        gr_text("+", 126.5, 101.4, "capacitor-plus", size=0.8, thickness=0.15),
        gr_text("YIFAN DESGIN", 121.5, 112.0, "title", layer="B.SilkS", size=0.8, mirror=True),
        gr_text("1=G 2=V 3=D", 108.5, 101.0, "pin-map", layer="B.SilkS", size=0.8, mirror=True),
        gr_text("NO FUSE / NO REG", 134.0, 101.0, "warning", layer="B.SilkS", size=0.8, mirror=True),
    ]

    data_tracks = [
        segment(103.2, 109.0, 108.5, 109.0, 0.5, "B.Cu", "DATA", "d-j1-j2"),
        segment(108.5, 109.0, 113.8, 109.0, 0.5, "B.Cu", "DATA", "d-j2-j3"),
        segment(113.8, 109.0, 119.1, 109.0, 0.5, "B.Cu", "DATA", "d-j3-j4"),
    ]

    # Explicit power buses supplement the full-layer copper pours.  They keep
    # the critical connections visible and continuous even before zone refill.
    vbatt_tracks = [
        segment(103.2, 106.5, 108.5, 106.5, 1.5, "F.Cu", "VBATT", "v-j1-j2"),
        segment(108.5, 106.5, 113.8, 106.5, 1.5, "F.Cu", "VBATT", "v-j2-j3"),
        segment(113.8, 106.5, 119.1, 106.5, 1.5, "F.Cu", "VBATT", "v-j3-j4"),
        segment(119.1, 106.5, 121.8, 106.5, 1.5, "F.Cu", "VBATT", "v-out-a"),
        segment(121.8, 106.5, 124.0, 104.75, 1.5, "F.Cu", "VBATT", "v-out-b"),
        segment(124.0, 104.75, 126.5, 104.75, 1.5, "F.Cu", "VBATT", "v-cap"),
        segment(126.5, 104.75, 131.8, 104.75, 1.5, "F.Cu", "VBATT", "v-input-a"),
        segment(131.8, 104.75, 138.0, 104.0, 1.5, "F.Cu", "VBATT", "v-input-b"),
    ]

    ground_tracks = [
        segment(103.2, 104.0, 108.5, 104.0, 1.5, "B.Cu", "GND", "g-j1-j2"),
        segment(108.5, 104.0, 113.8, 104.0, 1.5, "B.Cu", "GND", "g-j2-j3"),
        segment(113.8, 104.0, 119.1, 104.0, 1.5, "B.Cu", "GND", "g-j3-j4"),
        segment(119.1, 104.0, 121.5, 104.0, 1.5, "B.Cu", "GND", "g-out-a"),
        segment(121.5, 104.0, 123.0, 108.25, 1.5, "B.Cu", "GND", "g-out-b"),
        segment(123.0, 108.25, 126.5, 108.25, 1.5, "B.Cu", "GND", "g-cap"),
        segment(126.5, 108.25, 134.0, 108.25, 1.5, "B.Cu", "GND", "g-input-a"),
        segment(134.0, 108.25, 138.0, 109.0, 1.5, "B.Cu", "GND", "g-input-b"),
    ]

    footprint_text = "\n  ".join(footprints)
    edge_text = "\n  ".join(edges)
    silk_text = "\n  ".join(texts)
    data_track_text = "\n  ".join(data_tracks)
    vbatt_track_text = "\n  ".join(vbatt_tracks)
    ground_track_text = "\n  ".join(ground_tracks)

    return f"""(kicad_pcb
  (version 20260206)
  (generator \"pcbnew\")
  (generator_version \"10.0\")
  (general
    (thickness 1.6)
    (legacy_teardrops no)
  )
  (paper \"A4\")
  (title_block
    (title \"Microduck DCHUB passive 4-port long-strip distribution board\")
    (date \"2026-09-29\")
    (rev \"v1.1 LONG-STRIP FABRICATION RELEASE\")
    (company \"Fanduck personal research project\")
    (comment 1 \"THIRD-PARTY DERIVATIVE; NOT POLLEN ORIGINAL\")
    (comment 2 \"43.0 x 13.0 mm / 2L / 2 oz / 1.6 mm FR-4\")
    (comment 3 \"PASSIVE HUB ONLY: NO FUSE, REGULATION OR REVERSE-POLARITY PROTECTION\")
  )
  (layers
    (0 \"F.Cu\" signal)
    (2 \"B.Cu\" signal)
    (9 \"F.Adhes\" user \"F.Adhesive\")
    (11 \"B.Adhes\" user \"B.Adhesive\")
    (13 \"F.Paste\" user)
    (15 \"B.Paste\" user)
    (5 \"F.SilkS\" user \"F.Silkscreen\")
    (7 \"B.SilkS\" user \"B.Silkscreen\")
    (1 \"F.Mask\" user)
    (3 \"B.Mask\" user)
    (17 \"Dwgs.User\" user \"User.Drawings\")
    (19 \"Cmts.User\" user \"User.Comments\")
    (21 \"Eco1.User\" user)
    (23 \"Eco2.User\" user)
    (25 \"Edge.Cuts\" user)
    (27 \"Margin\" user)
    (31 \"F.CrtYd\" user \"F.Courtyard\")
    (29 \"B.CrtYd\" user \"B.Courtyard\")
    (35 \"F.Fab\" user)
    (33 \"B.Fab\" user)
  )
  (setup
    (stackup
      (layer \"F.SilkS\" (type \"Top Silk Screen\"))
      (layer \"F.Paste\" (type \"Top Solder Paste\"))
      (layer \"F.Mask\" (type \"Top Solder Mask\") (thickness 0.01))
      (layer \"F.Cu\" (type \"copper\") (thickness 0.07))
      (layer \"dielectric 1\" (type \"core\") (thickness 1.44) (material \"FR4\") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer \"B.Cu\" (type \"copper\") (thickness 0.07))
      (layer \"B.Mask\" (type \"Bottom Solder Mask\") (thickness 0.01))
      (layer \"B.Paste\" (type \"Bottom Solder Paste\"))
      (layer \"B.SilkS\" (type \"Bottom Silk Screen\"))
      (copper_finish \"HAL lead-free\")
      (dielectric_constraints no)
    )
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no)
    (tenting (front yes) (back yes))
    (covering (front no) (back no))
    (plugging (front no) (back no))
    (capping no)
    (filling no)
    (pcbplotparams
      (layerselection 0x00000000_00000000_55555555_5755f5ff)
      (plot_on_all_layers_selection 0x00000000_00000000_00000000_00000000)
      (disableapertmacros no)
      (usegerberextensions yes)
      (usegerberattributes yes)
      (usegerberadvancedattributes yes)
      (creategerberjobfile yes)
      (dashed_line_dash_ratio 12)
      (dashed_line_gap_ratio 3)
      (svgprecision 4)
      (plotframeref no)
      (mode 1)
      (useauxorigin no)
      (pdf_front_fp_property_popups yes)
      (pdf_back_fp_property_popups yes)
      (pdf_metadata yes)
      (pdf_single_document no)
      (dxfpolygonmode yes)
      (dxfimperialunits no)
      (dxfusepcbnewfont yes)
      (psnegative no)
      (psa4output no)
      (plot_black_and_white yes)
      (sketchpadsonfab no)
      (plotpadnumbers no)
      (hidednponfab no)
      (sketchdnponfab yes)
      (crossoutdnponfab yes)
      (subtractmaskfromsilk yes)
      (outputformat 1)
      (mirror no)
      (drillshape 1)
      (scaleselection 1)
      (outputdirectory \"\")
    )
  )
  {footprint_text}
  {edge_text}
  {silk_text}
  {data_track_text}
  {vbatt_track_text}
  {ground_track_text}
  {zone('VBATT', 'F.Cu', 'VBATT_TOP_PLANE')}
  {zone('GND', 'B.Cu', 'GND_BOTTOM_PLANE')}
  (embedded_fonts no)
)
"""


def make_legacy_schematic() -> str:
    # Legacy format is deliberately used as a concise, deterministic source;
    # kicad-cli upgrades it to the current .kicad_sch format during the build.
    connectors = []
    roles = [
        ("J1", "BUS_HAT", 2600, 2000),
        ("J2", "LEFT_LEG", 4600, 2000),
        ("J3", "RIGHT_LEG", 2600, 3400),
        ("J4", "HEAD_NECK", 4600, 3400),
    ]
    for idx, (ref, role, x, y) in enumerate(roles, 1):
        stamp = f"6F{idx:06X}"
        footprint_name = "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90"
        connectors.append(f"""$Comp
L Connector_Generic:Conn_01x03 {ref}
U 1 1 {stamp}
P {x} {y}
F 0 \"{ref}\" H {x+80} {y+420} 50  0000 C CNN
F 1 \"{role}\" H {x+80} {y+320} 50  0000 C CNN
F 2 \"{footprint_name}\" H {x} {y} 50  0001 C CNN
F 3 \"https://www.jst-mfg.com/product/index.php?series=58\" H {x} {y} 50  0001 C CNN
\t1    {x} {y}
\t1    0    0    -1
$EndComp
Text Label {x-450} {y-100} 2    50   ~ 0
GND
Text Label {x-450} {y} 2    50   ~ 0
VBATT
Text Label {x-450} {y+100} 2    50   ~ 0
DATA
Wire Wire Line
\t{x-450} {y-100} {x-150} {y-100}
Wire Wire Line
\t{x-450} {y} {x-150} {y}
Wire Wire Line
\t{x-450} {y+100} {x-150} {y+100}
""")

    return f"""EESchema Schematic File Version 4
LIBS:power
LIBS:device
LIBS:Connector_Generic
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title \"Microduck DCHUB passive 4-port long-strip distribution board\"
Date \"2026-09-29\"
Rev \"v1.1\"
Comp \"Fanduck personal research project\"
Comment1 \"Third-party derivative; not Pollen original\"
Comment2 \"Four X3P ports are electrically equivalent and parallel\"
Comment3 \"No fuse, regulator, reverse-polarity or over-voltage protection\"
Comment4 \"Pin 1 GND / Pin 2 VBATT / Pin 3 DATA\"
$EndDescr
Text Notes 1700 1200 0    100  ~ 0
PASSIVE 1-to-3 DYNAMIXEL TTL / POWER HUB
Text Notes 1700 1400 0    60   ~ 0
J1 is the nominal controller input; J2-J4 are nominal branches. All four ports are electrically identical.
{''.join(connectors)}
$Comp
L Connector_Generic:Conn_01x02 J5
U 1 1 6F000010
P 7200 2500
F 0 \"J5\" H 7280 2492 50  0000 L CNN
F 1 \"BATTERY_INPUT_KF301_5.0_2P\" H 7280 2401 50  0000 L CNN
F 2 \"DCHUB:KF301-5.0-2P\" H 7200 2500 50  0001 C CNN
F 3 \"~\" H 7200 2500 50  0001 C CNN
\t1    7200 2500
\t1    0    0    -1
$EndComp
Text Label 6750 2400 2    50   ~ 0
GND
Text Label 6750 2500 2    50   ~ 0
VBATT
Wire Wire Line
\t6750 2400 7050 2400
Wire Wire Line
\t6750 2500 7050 2500
$Comp
L Device:C_Polarized C1
U 1 1 6F000011
P 7200 3550
F 0 \"C1\" H 7318 3596 50  0000 L CNN
F 1 \"470uF_16V_EEU-FR1C471\" H 7318 3505 50  0000 L CNN
F 2 \"DCHUB:CP_Radial_D8.0mm_P3.50mm_Vertical\" H 7238 3400 50  0001 C CNN
F 3 \"https://industrial.panasonic.com/ww/products/pt/aluminum-cap-lead/models/EEUFR1C471\" H 7200 3550 50  0001 C CNN
\t1    7200 3550
\t1    0    0    -1
$EndComp
Text Label 6800 3300 2    50   ~ 0
VBATT
Text Label 6800 3800 2    50   ~ 0
GND
Wire Wire Line
\t6800 3300 7200 3300
Wire Wire Line
\t7200 3300 7200 3400
Wire Wire Line
\t7200 3700 7200 3800
Wire Wire Line
\t7200 3800 6800 3800
Text Notes 6500 4400 0    60   ~ 0
J5 pin 1 = GND, pin 2 = VBATT. C1 polarity is mandatory.
Text Notes 6500 4550 0    60   ~ 0
This board does not regulate a 2S battery down to the XL330-M288-T published 3.7-6.0 V range.
$EndSCHEMATC
"""


def sch_font(size: float = 1.27, *, bold: bool = False, justify: str | None = None, hide: bool = False) -> str:
    bold_text = " (bold yes)" if bold else ""
    justify_text = f" (justify {justify})" if justify else ""
    hide_text = " (hide yes)" if hide else ""
    return f"(effects (font (size {size:g} {size:g}){bold_text}){justify_text}{hide_text})"


def sch_property(name: str, value: str, x: float, y: float, *, hidden: bool = False) -> str:
    return f"""(property \"{name}\" \"{value}\"
  (at {x:g} {y:g} 0)
  (show_name no)
  (do_not_autoplace no)
  {sch_font(hide=hidden)}
)"""


def lib_symbol_x3p() -> str:
    return f"""(symbol \"DCHUB:X3P\"
  (pin_names (offset 1.016))
  (exclude_from_sim no)
  (in_bom yes)
  (on_board yes)
  (in_pos_files no)
  (duplicate_pin_numbers_are_jumpers no)
  {sch_property('Reference', 'J', 0, 5.08)}
  {sch_property('Value', 'X3P', 0, -5.08)}
  {sch_property('Footprint', '', 0, 0, hidden=True)}
  {sch_property('Datasheet', 'https://www.jst-mfg.com/product/index.php?series=58', 0, 0, hidden=True)}
  {sch_property('Description', 'Three-pin shared Dynamixel TTL and power port', 0, 0, hidden=True)}
  (symbol \"X3P_0_1\"
    (rectangle (start -1.27 3.81) (end 1.27 -3.81)
      (stroke (width 0.254) (type default)) (fill (type background)))
  )
  (symbol \"X3P_1_1\"
    (pin passive line (at -5.08 2.54 0) (length 3.81)
      (name \"GND\" {sch_font()}) (number \"1\" {sch_font()}))
    (pin passive line (at -5.08 0 0) (length 3.81)
      (name \"VBATT\" {sch_font()}) (number \"2\" {sch_font()}))
    (pin passive line (at -5.08 -2.54 0) (length 3.81)
      (name \"DATA\" {sch_font()}) (number \"3\" {sch_font()}))
  )
  (embedded_fonts no)
)"""


def lib_symbol_terminal() -> str:
    return f"""(symbol \"DCHUB:BATT_IN\"
  (pin_names (offset 1.016))
  (exclude_from_sim no)
  (in_bom yes)
  (on_board yes)
  (in_pos_files no)
  (duplicate_pin_numbers_are_jumpers no)
  {sch_property('Reference', 'J', 0, 3.81)}
  {sch_property('Value', 'BATT_IN', 0, -3.81)}
  {sch_property('Footprint', 'DCHUB:KF301-5.0-2P', 0, 0, hidden=True)}
  {sch_property('Datasheet', '~', 0, 0, hidden=True)}
  {sch_property('Description', 'Unregulated battery input; pin 1 GND, pin 2 VBATT', 0, 0, hidden=True)}
  (symbol \"BATT_IN_0_1\"
    (rectangle (start -1.27 2.54) (end 1.27 -2.54)
      (stroke (width 0.254) (type default)) (fill (type background)))
  )
  (symbol \"BATT_IN_1_1\"
    (pin passive line (at -5.08 1.27 0) (length 3.81)
      (name \"GND\" {sch_font()}) (number \"1\" {sch_font()}))
    (pin passive line (at -5.08 -1.27 0) (length 3.81)
      (name \"VBATT\" {sch_font()}) (number \"2\" {sch_font()}))
  )
  (embedded_fonts no)
)"""


def lib_symbol_cap() -> str:
    return f"""(symbol \"DCHUB:C_POL\"
  (pin_names (offset 1.016))
  (exclude_from_sim no)
  (in_bom yes)
  (on_board yes)
  (in_pos_files no)
  (duplicate_pin_numbers_are_jumpers no)
  {sch_property('Reference', 'C', 0, 3.81)}
  {sch_property('Value', 'C_POL', 0, -3.81)}
  {sch_property('Footprint', 'DCHUB:CP_Radial_D8.0mm_P3.50mm_Vertical', 0, 0, hidden=True)}
  {sch_property('Datasheet', 'https://industrial.panasonic.com/ww/products/pt/aluminum-cap-lead/models/EEUFR1C471', 0, 0, hidden=True)}
  {sch_property('Description', 'Polarized bulk capacitor, 470 uF 16 V', 0, 0, hidden=True)}
  (symbol \"C_POL_0_1\"
    (polyline (pts (xy -0.762 2.032) (xy -0.762 -2.032))
      (stroke (width 0.508) (type default)) (fill (type none)))
    (polyline (pts (xy 0.762 2.032) (xy 0.762 -2.032))
      (stroke (width 0.254) (type default)) (fill (type none)))
    (text \"+\" (at -2.286 2.286 0)
      {sch_font(1.27, bold=True, justify='left bottom')})
  )
  (symbol \"C_POL_1_1\"
    (pin passive line (at -5.08 0 0) (length 4.318)
      (name \"+\" {sch_font()}) (number \"1\" {sch_font()}))
    (pin passive line (at 5.08 0 180) (length 4.318)
      (name \"-\" {sch_font()}) (number \"2\" {sch_font()}))
  )
  (embedded_fonts no)
)"""


def global_label(name: str, x: float, y: float, orientation: int, key: str) -> str:
    justify = "right" if orientation == 180 else "left"
    return f"""(global_label \"{name}\"
  (shape bidirectional)
  (at {x:g} {y:g} {orientation})
  (fields_autoplaced yes)
  {sch_font(justify=justify)}
  (uuid \"{uid('sch-label-' + key)}\")
)"""


def schematic_symbol(lib_id: str, ref: str, value: str, footprint: str, x: float, y: float,
                     pins: list[str], description: str) -> str:
    symbol_uuid = uid("sch-symbol-" + ref.lower())
    pin_blocks = "\n  ".join(
        f'(pin \"{pin}\" (uuid \"{uid("sch-pin-" + ref.lower() + "-" + pin)}\"))'
        for pin in pins
    )
    return f"""(symbol
  (lib_id \"{lib_id}\")
  (at {x:g} {y:g} 0)
  (unit 1)
  (exclude_from_sim no)
  (in_bom yes)
  (on_board yes)
  (in_pos_files no)
  (dnp no)
  (uuid \"{symbol_uuid}\")
  (property \"Reference\" \"{ref}\" (at {x+3:g} {y-5:g} 0) {sch_font()})
  (property \"Value\" \"{value}\" (at {x+3:g} {y+5:g} 0) {sch_font()})
  (property \"Footprint\" \"{footprint}\" (at {x:g} {y:g} 0) {sch_font(hide=True)})
  (property \"Datasheet\" \"~\" (at {x:g} {y:g} 0) {sch_font(hide=True)})
  (property \"Description\" \"{description}\" (at {x:g} {y:g} 0) {sch_font(hide=True)})
  {pin_blocks}
  (instances
    (project \"{PROJECT}\"
      (path \"/{uid('schematic-root')}/{symbol_uuid}\" (reference \"{ref}\") (unit 1))
    )
  )
)"""


def make_modern_schematic() -> str:
    x3p_specs = [
        ("J1", "BUS / HAT", "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90", 50.8, 50.8),
        ("J2", "LEFT LEG", "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90", 91.44, 50.8),
        ("J3", "RIGHT LEG", "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90", 50.8, 76.2),
        ("J4", "HEAD / NECK", "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90", 91.44, 76.2),
    ]
    labels: list[str] = []
    symbols: list[str] = []
    for ref, role, footprint, x, y in x3p_specs:
        symbols.append(schematic_symbol("DCHUB:X3P", ref, "B3B-EH-A(LF)(SN)", footprint, x, y, ["1", "2", "3"],
                                        "Parallel X3P port: pin 1 GND, pin 2 VBATT, pin 3 DATA"))
        labels.extend([
            # KiCad's symbol-local +Y axis maps upward on the schematic sheet,
            # so pin 1 (+2.54 local) is located at y-2.54 in sheet coordinates.
            global_label("GND", x - 5.08, y - 2.54, 180, ref + "-gnd"),
            global_label("VBATT", x - 5.08, y, 180, ref + "-vbatt"),
            global_label("DATA", x - 5.08, y + 2.54, 180, ref + "-data"),
        ])

    symbols.append(schematic_symbol("DCHUB:BATT_IN", "J5", "KF301-5.0-2P", "DCHUB:KF301-5.0-2P",
                                    149.86, 55.88, ["1", "2"], "Unregulated battery input"))
    labels.extend([
        global_label("GND", 144.78, 54.61, 180, "j5-gnd"),
        global_label("VBATT", 144.78, 57.15, 180, "j5-vbatt"),
    ])

    symbols.append(schematic_symbol("DCHUB:C_POL", "C1", "470uF 16V",
                                    "DCHUB:CP_Radial_D8.0mm_P3.50mm_Vertical",
                                    149.86, 81.28, ["1", "2"], "Polarized bulk capacitor"))
    labels.extend([
        global_label("VBATT", 144.78, 81.28, 180, "c1-vbatt"),
        global_label("GND", 154.94, 81.28, 0, "c1-gnd"),
    ])

    notes = [
        ("PASSIVE 1-to-3 DYNAMIXEL TTL / POWER HUB", 25.4, 20.32, True),
        ("J1 is the nominal controller input; J2-J4 are nominal branches. All four ports are electrically identical.", 25.4, 25.4, False),
        ("Pin map: 1=GND, 2=VBATT, 3=DATA. J5: 1=GND, 2=VBATT. C1 polarity is mandatory.", 25.4, 30.48, False),
        ("No fuse, regulator, reverse-polarity protection or over-voltage protection is present on this board.", 25.4, 35.56, True),
        ("A direct 2S rail exceeds the retail XL330-M288-T published 3.7-6.0 V range; fabrication does not authorize power-up.", 25.4, 40.64, True),
    ]
    note_text = []
    for index, (body, x, y, bold) in enumerate(notes):
        note_text.append(f"""(text \"{body}\" (exclude_from_sim no) (at {x:g} {y:g} 0)
  {sch_font(1.2, bold=bold, justify='left bottom')}
  (uuid \"{uid('sch-note-' + str(index))}\")
)""")

    label_text = "\n  ".join(labels)
    notes_text = "\n  ".join(note_text)
    symbol_text = "\n  ".join(symbols)

    return f"""(kicad_sch
  (version 20250114)
  (generator \"eeschema\")
  (generator_version \"10.0.6\")
  (uuid \"{uid('schematic-root')}\")
  (paper \"A4\")
  (title_block
    (title \"Microduck DCHUB passive 4-port long-strip distribution board\")
    (date \"2026-09-29\")
    (rev \"v1.1 LONG-STRIP FABRICATION RELEASE\")
    (company \"Fanduck personal research project\")
    (comment 1 \"THIRD-PARTY DERIVATIVE; NOT POLLEN ORIGINAL\")
    (comment 2 \"NO FUSE / NO REGULATION / DO NOT POWER UNTIL HARNESS VALIDATION\")
  )
  (lib_symbols
    {lib_symbol_x3p()}
    {lib_symbol_terminal()}
    {lib_symbol_cap()}
  )
  {label_text}
  {notes_text}
  {symbol_text}
  (sheet_instances (path \"/\" (page \"1\")))
  (embedded_fonts no)
)
"""


def make_symbol_library() -> str:
    symbols = [
        lib_symbol_x3p().replace('(symbol "DCHUB:X3P"', '(symbol "X3P"', 1),
        lib_symbol_terminal().replace('(symbol "DCHUB:BATT_IN"', '(symbol "BATT_IN"', 1),
        lib_symbol_cap().replace('(symbol "DCHUB:C_POL"', '(symbol "C_POL"', 1),
    ]
    body = "\n  ".join(symbols)
    return f"""(kicad_symbol_lib
  (version 20231120)
  (generator \"kicad_symbol_editor\")
  (generator_version \"10.0.6\")
  {body}
)
"""


def make_terminal_mod() -> str:
    return f"""(footprint \"KF301-5.0-2P\"
  (version 20260206)
  (generator \"pcbnew\")
  (layer \"F.Cu\")
  (descr \"Generic KF301-compatible 2-position 5.00 mm pitch screw terminal\")
  (tags \"KF301 5.0mm screw terminal THT\")
  (property \"Reference\" \"REF**\" (at 0 6.0 0) (layer \"F.SilkS\") {effects(0.8, 0.12)})
  (property \"Value\" \"KF301-5.0-2P\" (at 0 -6.0 0) (layer \"F.Fab\") {effects(0.8, 0.12)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_rect (start -3.8 -5) (end 3.8 5) (stroke (width 0.15) (type solid)) (fill no) (layer \"F.SilkS\"))
  (fp_line (start 2.5 -5) (end 2.5 5) (stroke (width 0.15) (type solid)) (layer \"F.SilkS\"))
  (fp_rect (start -4.1 -5.3) (end 4.1 5.3) (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\"))
  (fp_rect (start -3.8 -5) (end 3.8 5) (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\"))
  (pad \"1\" thru_hole roundrect (at 0 2.5) (size 2.5 2.5) (drill 1.4) (layers \"*.Cu\" \"*.Mask\") (roundrect_rratio 0.15))
  (pad \"2\" thru_hole circle (at 0 -2.5) (size 2.5 2.5) (drill 1.4) (layers \"*.Cu\" \"*.Mask\"))
  (embedded_fonts no)
)
"""


def make_jst_mod() -> str:
    return f"""(footprint \"JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical\"
  (version 20260206)
  (generator \"pcbnew\")
  (layer \"F.Cu\")
  (descr \"JST EH B3B-EH-A, 3 positions, 2.50 mm pitch, vertical THT\")
  (tags \"JST EH B3B-EH-A X3P Dynamixel\")
  (property \"Reference\" \"REF**\" (at 2.5 -2.8 0) (layer \"F.SilkS\") {effects(0.8, 0.12)})
  (property \"Value\" \"B3B-EH-A(LF)(SN)\" (at 2.5 3.4 0) (layer \"F.Fab\") {effects(0.8, 0.12)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_line (start -2.91 0.11) (end -2.91 2.61) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -2.91 2.61) (end -0.41 2.61) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -2.61 0) (end -2.11 0) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -2.61 0.81) (end -1.61 0.81) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -2.11 -1.21) (end 7.11 -1.21) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -2.11 0) (end -2.11 -1.21) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start -1.61 0.81) (end -1.61 2.31) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start 6.61 0.81) (end 6.61 2.31) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start 7.11 -1.21) (end 7.11 0) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start 7.11 0) (end 7.61 0) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_line (start 7.61 0.81) (end 6.61 0.81) (stroke (width 0.12) (type solid)) (layer \"F.SilkS\"))
  (fp_rect (start -2.61 -1.71) (end 7.61 2.31) (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\"))
  (fp_rect (start -3 -2.1) (end 8 2.7) (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\"))
  (fp_rect (start -2.5 -1.6) (end 7.5 2.2) (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\"))
  (pad \"1\" thru_hole roundrect (at 0 0) (size 1.8 2.0) (drill 0.95) (layers \"*.Cu\" \"*.Mask\") (roundrect_rratio 0.14))
  (pad \"2\" thru_hole oval (at 2.5 0) (size 1.8 2.0) (drill 0.95) (layers \"*.Cu\" \"*.Mask\"))
  (pad \"3\" thru_hole oval (at 5 0) (size 1.8 2.0) (drill 0.95) (layers \"*.Cu\" \"*.Mask\"))
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Connector_JST.3dshapes/JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical.step\"
    (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 0)))
)
"""


def make_jst_rot90_mod() -> str:
    return f"""(footprint \"JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90\"
  (version 20260206)
  (generator \"pcbnew\")
  (layer \"F.Cu\")
  (descr \"JST EH B3B-EH-A, vertical board layout, 2.50 mm pitch\")
  (tags \"JST EH B3B-EH-A X3P Dynamixel rotated\")
  (property \"Reference\" \"REF**\" (at 3 2.5 90) (layer \"F.SilkS\") {effects(0.8, 0.12)})
  (property \"Value\" \"B3B-EH-A(LF)(SN)\" (at -3.4 2.5 90) (layer \"F.Fab\") {effects(0.8, 0.12)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_rect (start -2.31 -2.61) (end 1.71 7.61) (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\"))
  (fp_line (start -2.31 -2.61) (end -0.81 -2.61) (stroke (width 0.3) (type solid)) (layer \"F.SilkS\"))
  (fp_rect (start -2.7 -3) (end 2.1 8) (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\"))
  (fp_rect (start -2.2 -2.5) (end 1.6 7.5) (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\"))
  (pad \"1\" thru_hole roundrect (at 0 0) (size 1.8 2.0) (drill 0.95) (layers \"*.Cu\" \"*.Mask\") (roundrect_rratio 0.14))
  (pad \"2\" thru_hole oval (at 0 2.5) (size 2.0 1.8) (drill 0.95) (layers \"*.Cu\" \"*.Mask\"))
  (pad \"3\" thru_hole oval (at 0 5) (size 2.0 1.8) (drill 0.95) (layers \"*.Cu\" \"*.Mask\"))
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Connector_JST.3dshapes/JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical.step\"
    (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 90)))
)
"""


def make_cap_mod() -> str:
    return f"""(footprint \"CP_Radial_D8.0mm_P3.50mm_Vertical\"
  (version 20260206)
  (generator \"pcbnew\")
  (layer \"F.Cu\")
  (descr \"Polarized radial electrolytic, 8 mm diameter, 3.50 mm lead pitch\")
  (tags \"470uF 16V low impedance radial electrolytic\")
  (property \"Reference\" \"REF**\" (at 1.75 -5.25 0) (layer \"F.SilkS\") {effects(0.8, 0.12)})
  (property \"Value\" \"470uF 16V\" (at 1.75 5.25 0) (layer \"F.Fab\") {effects(0.8, 0.12)})
  (attr through_hole)
  (duplicate_pad_numbers_are_jumpers no)
  (fp_circle (center 0 1.75) (end 4.08 1.75) (stroke (width 0.12) (type solid)) (fill no) (layer \"F.SilkS\"))
  (fp_circle (center 0 1.75) (end 4.25 1.75) (stroke (width 0.05) (type solid)) (fill no) (layer \"F.CrtYd\"))
  (fp_circle (center 0 1.75) (end 4 1.75) (stroke (width 0.1) (type solid)) (fill no) (layer \"F.Fab\"))
  (pad \"1\" thru_hole rect (at 0 0) (size 2.2 2.2) (drill 0.9) (layers \"*.Cu\" \"*.Mask\"))
  (pad \"2\" thru_hole circle (at 0 3.5) (size 2.2 2.2) (drill 0.9) (layers \"*.Cu\" \"*.Mask\"))
  (embedded_fonts no)
  (model \"${{KICAD10_3DMODEL_DIR}}/Capacitor_THT.3dshapes/CP_Radial_D8.0mm_P3.50mm.step\"
    (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 90)))
)
"""


def write_csvs() -> None:
    with (ROOT / "BOM_manual_assembly.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.writer(fh)
        writer.writerow([
            "References", "Qty", "Category", "Manufacturer", "MPN / specification", "Value",
            "Footprint", "Assembly", "Evidence status", "Notes",
        ])
        writer.writerow([
            "J1,J2,J3,J4", 4, "X3P connector", "JST", "B3B-EH-A(LF)(SN)", "3-pin EH, 2.50 mm",
            "DCHUB:JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90", "Manual THT", "Manufacturer confirmed",
            "JST rates EH at 3 A AC/DC with AWG22; each installed branch still requires load verification.",
        ])
        writer.writerow([
            "J5", 1, "Battery terminal", "Generic / owner-specified", "KF301-5.0-2P", "2-pin, 5.00 mm pitch",
            "DCHUB:KF301-5.0-2P", "Manual THT", "Third-party / verify purchased part",
            "Body <=7.6 x 10.0 mm, lead diameter <=1.3 mm. Verify exact supplier drawing before soldering.",
        ])
        writer.writerow([
            "C1", 1, "Bulk capacitor", "Panasonic", "EEU-FR1C471", "470 uF, 16 V, 105 C",
            "DCHUB:CP_Radial_D8.0mm_P3.50mm_Vertical", "Manual THT", "Manufacturer confirmed",
            "Polarized; 8.0 x 11.5 mm, P3.5 mm, FR low-impedance series.",
        ])

    with (ROOT / "NETLIST_and_pinmap.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Net", "Connected pins", "Purpose", "Validation status"])
        writer.writerow(["GND", "J1.1,J2.1,J3.1,J4.1,J5.1,C1.2", "Battery return / signal reference", "Official HAT/X3P mapping; assembled board not yet continuity-tested"])
        writer.writerow(["VBATT", "J1.2,J2.2,J3.2,J4.2,J5.2,C1.1", "Unregulated battery rail", "Topology requested by owner; voltage/load safety not validated"])
        writer.writerow(["DATA", "J1.3,J2.3,J3.3,J4.3", "Shared half-duplex Dynamixel TTL data", "Official HAT/X3P mapping; star branch behavior not yet tested"])


def write_project_files() -> None:
    (ROOT / f"{PROJECT}.kicad_pcb").write_text(make_board(), encoding="utf-8")
    (ROOT / f"{PROJECT}.kicad_sch").write_text(make_modern_schematic(), encoding="utf-8")
    (ROOT / f"{PROJECT}.sch").unlink(missing_ok=True)
    (ROOT / f"{PROJECT}.kicad_pro").write_text(
        json.dumps(
            {
                "board": {},
                "boards": [],
                "cvpcb": {},
                "erc": {},
                "libraries": {},
                "meta": {"filename": f"{PROJECT}.kicad_pro", "version": 1},
                "net_settings": {"classes": [], "meta": {"version": 3}},
                "pcbnew": {},
                "schematic": {},
                "text_variables": {},
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    (ROOT / "fp-lib-table").write_text(
        '(fp_lib_table\n  (lib (name "DCHUB")(type "KiCad")(uri "${KIPRJMOD}/DCHUB.pretty")(options "")(descr "DCHUB local footprints"))\n)\n',
        encoding="utf-8",
    )
    (ROOT / "sym-lib-table").write_text(
        '(sym_lib_table\n  (lib (name "DCHUB")(type "KiCad")(uri "${KIPRJMOD}/DCHUB.kicad_sym")(options "")(descr "DCHUB local symbols"))\n)\n',
        encoding="utf-8",
    )
    (ROOT / "DCHUB.kicad_sym").write_text(make_symbol_library(), encoding="utf-8")
    lib = ROOT / "DCHUB.pretty"
    lib.mkdir(exist_ok=True)
    (lib / "KF301-5.0-2P.kicad_mod").write_text(make_terminal_mod(), encoding="utf-8")
    (lib / "JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical.kicad_mod").write_text(make_jst_mod(), encoding="utf-8")
    (lib / "JST_EH_B3B-EH-A_1x03_P2.50mm_Vertical_Rot90.kicad_mod").write_text(make_jst_rot90_mod(), encoding="utf-8")
    (lib / "CP_Radial_D8.0mm_P3.50mm_Vertical.kicad_mod").write_text(make_cap_mod(), encoding="utf-8")
    (lib / "CP_Radial_D8.0mm_P3.50mm.kicad_mod").unlink(missing_ok=True)
    write_csvs()


if __name__ == "__main__":
    write_project_files()
    print(f"Generated {PROJECT} in {ROOT}")
