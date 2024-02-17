# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 07:07:04 2024

@author: mcode
"""

from cx_Freeze import setup, Executable

setup(
    name="calculator",
    version="1.0.6",
    executables=[Executable("calculator-V1.0.6.py")]
)
