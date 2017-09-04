#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewInt class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewInt(BlockModel):
    """
    This class contains methods related the NewInt class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Creates new literal value (Int)."
        self.label = "New Int"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.int",
                        "name":"value",
                         "conn_type":"Output",
                        "label":"Value"}]
        self.group = "Basic Data Type"

        self.properties = [{"name": "Value",
                            "label": "intVal",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = 'int  block$id$_int_o0 = $intVal$; // New Int Out\n'
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------