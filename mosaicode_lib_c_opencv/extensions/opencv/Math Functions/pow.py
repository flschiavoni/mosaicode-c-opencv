#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Pow class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Pow(BlockModel):
    """
    This class contains methods related the Pow class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.language = "c"
        self.framework = "opencv"
        self.help = "Eleva cada ponto de uma " + \
            "imagem a um valor fixo de potência."
        self.label = "Pow"
        self.color = "230:230:60:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Math Functions"
        self.properties = [{"label": "Exponent",
                            "name": "exponent",
                            "value":1,
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10
                            }
                           ]

# --------------------------- C/OpenCv Code------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        pow($port[input_image]$, $prop[exponent]$, $port[output_image]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------
