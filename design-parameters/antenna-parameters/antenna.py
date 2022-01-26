from math import *
import numpy as np

# antenna basics (Satellite Communication Systems)

def half_power_beamwidth(N: float, op_lambda: float, D: float) -> float:
    '''
    The half-power beamwidth of an antenna is defined as the angular separation 
    between the half-power (or -3 dB) signal points on the radiation pattern. For 
    an antenna with a non-symmetric radiation pattern, each cut of the three-dimensional 
    pattern containing the boresight has its individual half-power beamwidth.

    Args:
        N: typically 70 for a tapered distribution, 58 for uniform distribution
        op_lambda: operational wavelength [m]
        D: antenna diameter [m]

    Returns:
        Half-power beamwidth of the antenna
    '''
    return N*op_lambda/D

def antenna_gain(A: float, op_lambda: float, eta: float) -> float:
    '''
    Calculate antenna gain from physical parameters.

    Args:
        A: aperture area of antenna [m^2]
        op_lambda: operational wavelength [m]
        eta: antenna efficiency (typically between 50% & 70% for parabolic
        antennas) (horn antennas can be 90%)

    Returns:
        Antenna gain
    '''
    return eta*4*pi*A/op_lambda**2

def avg_rad_intensity(P_r: float) -> float:
    '''
    Calculate average radiation intensity.

    Args:
        P_r: total radiated power from an antenna (note that this is the
        power launched into the free space) [W]
    
    Returns:
        Average radiation intensity [W]
    '''

    return P_r/(4*pi)



    


