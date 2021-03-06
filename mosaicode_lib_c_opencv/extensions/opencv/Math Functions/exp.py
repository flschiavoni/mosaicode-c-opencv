#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Exp class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Exp(BlockModel):
    """
    This class contains methods related the Exp class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Aplica a função exponencial a uma imagem, ou seja, " + \
            "eleva a constante neperiana ao valor " + \
            "de intensidade luminosa de cada ponto da imagem."
        self.label = "Exp"
        self.color = "230:230:60:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"input_image",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.group = "Math Functions"

# --------------------------C/OpenCv code------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Mat block$id$_img_t;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        cvtColor($port[input_image]$, block$id$_img_t, COLOR_RGB2GRAY);
        block$id$_img_t.convertTo(block$id$_img_t, CV_32F);
        block$id$_img_t = block$id$_img_t + 1;
        exp(block$id$_img_t, block$id$_img_t);
        convertScaleAbs(block$id$_img_t, block$id$_img_t);
        normalize(block$id$_img_t, $port[output_image]$, 0, 255, NORM_MINMAX);
    }
"""
   
        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
    block$id$_img_t.release();
"""

# -----------------------------------------------------------------------------
