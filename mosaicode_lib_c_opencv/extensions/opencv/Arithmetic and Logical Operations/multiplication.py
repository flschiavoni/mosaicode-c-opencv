#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Multiplication class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Multiplication(BlockModel):
    """
    This class contains methods related the Multiplication class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Realiza a multiplicação de duas imagens."
        self.label = "Multiplication"
        self.color = "180:10:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"first_image",
                          "label":"First Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "conn_type":"Input",
                          "label":"Second Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and Logical Operations"

#------------------------------------- C/OpenCV Code -----------------------------        

        self.codes["declaration"] = \
"""        
    Mat $port[first_image]$;
    Mat $port[second_image]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[first_image]$.empty() && !$port[second_image]$.empty()){
        Size size$id$($port[first_image]$.cols, $port[first_image]$.rows);
        resize($port[second_image]$, $port[second_image]$, size$id$);
        multiply($port[first_image]$, $port[second_image]$, $port[output_image]$);
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[first_image]$.release();
    $port[second_image]$.release();
    $port[output_image]$.release();
"""
                
# -----------------------------------------------------------------------------
