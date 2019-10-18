#!/usr/bin/env python
"""
   Functions for temperature convertion
"""

def from_C_to_F(tC):
    return (tC * 1.8) + 32

def from_F_to_C(tF):
    return (tF - 32) * 5.0/9.0

def from_C_to_K(tC):
    return tC + 273.0

def from_K_to_F(tK):
    tC = tK - 273.0
    return from_C_to_F(tC)

def from_F_to_K(tF):
    return from_F_to_C(tF) + 273.0
