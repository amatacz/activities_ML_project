import pandas as pd
import numpy as np

def time_to_seconds(time_str):
    """ Converts time from HH:MM:SS to seconds"""
    if pd.isna(time_str) or time_str == '':
        return np.nan
    
    parts = str(time_str).split(':')

    if len(parts) == 3:
        h, m, s = map(float, parts)
    elif len(parts) == 2:
        h = 0.0
        m, s = map(float, parts)
    else:
        return 0.0
    
    return h * 3600 + m * 60 + s

def pace_to_seconds_per_km(pace_str):
    """ Converts pace from M:SS/km to seconds/km """

    if pd.isna(pace_str) or pace_str == '':
        return np.nan
    
    parts = str(pace_str).split(":")

    if len(parts) == 2:
        m, s = map(float, parts)
        return m * 60 + s
    

def calc_avg_speed(time, distance):
    """ Calculates average speed based on known values:
     time -> in seconds
     distance -> in kms
      """
    if pd.isna(time) or time <= 0:
        return np.nan
    
    if pd.isna(distance) or distance == 0.0:
        return np.nan
    
    speed = (distance/time) * 3600

    return round(speed, 2)

def calc_hr_zone(avg_hr, age=32):
    """
    Calculates HeartRate Zone for recorded activity.
    """

    hr_max = 220-age

    if avg_hr/hr_max >= 0.90:
        return 5
    elif avg_hr/hr_max >= 0.80:
        return 4
    elif avg_hr/hr_max >= 0.70:
        return 3
    elif avg_hr/hr_max >= 0.60:
        return 2
    else:
        return 1
    
def calc_calories_burning_intensity(kcal, time):
    """
    Calculates burned calories per minute.

    Kcal -> int
    time -> sec
    """

    if pd.isna(time) or time <= 0:
        return 0.0
    
    if pd.isna(kcal) or kcal <= 0:
        return 0.0
    burning_intensity = kcal/(time/60) 
    return round(burning_intensity, 2)

    
    