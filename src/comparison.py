import math


def calculate_rgb_euclidian_dist(colour1, colour2):
    r_component = (colour1.rgb[0] - colour2.rgb[0])**2
    g_component = (colour1.rgb[1] - colour2.rgb[1])**2
    b_component = (colour1.rgb[2] - colour2.rgb[2])**2
    return math.sqrt(r_component + g_component + b_component)

def calculate_hsv_dist(colour1, colour2):
    h1_radian = math.radians(colour1.hsv[0])
    s1 = colour1.hsv[1] / 360.0
    v1 = colour1.hsv[2] / 360.0
    x1_component = math.cos(h1_radian) * s1 * v1
    y1_component = math.sin(h1_radian) * s1 * v1
    z1_component = v1

    h2_radian = math.radians(colour2.hsv[0])
    s2 = colour2.hsv[1] / 360.0
    v2 = colour2.hsv[2] / 360.0
    x2_component = math.cos(h2_radian) * s2 * v2
    y2_component = math.sin(h2_radian) * s2 * v2
    z2_component = v2

    return math.sqrt((x1_component-x2_component)**2 + (y1_component - y2_component)**2 + (z1_component - z2_component)**2)

def calculate_cie76_distance(colour1, colour2):
    l_component = colour1.lab[0] - colour2.lab[0]
    a_component = colour1.lab[1] - colour2.lab[1]
    b_component = colour1.lab[2] - colour2.lab[2]

    return math.sqrt(l_component **2 + a_component **2 + b_component **2)

def calculate_ciede2000_distance(colour1, colour2):
    l1, a1, b1 = colour1.lab
    l2, a2, b2 = colour2.lab
    chroma1 = math.sqrt(a1**2 + b1**2)
    chroma2 = math.sqrt(a2**2 + b2**2)

    #average Chroma
    avgChroma = (chroma1 + chroma2) / 2.0

    #scaling factor g
    g_factor = 0.5 * (1- math.sqrt((avgChroma**7/(avgChroma**7 + 25**7))))

    #adjust a values based on scaling factor g and the adjusted chroma
    a1_adjusted = (1+g_factor) * a1
    a2_adjusted = (1+g_factor) * a2
    chroma1_adjusted = math.sqrt(((a1_adjusted**2) + (b1**2)))
    chroma2_adjusted = math.sqrt(((a2_adjusted**2) + (b2**2)))

    #calculate hue angles via helper method
    hue_angle1 = calculate_hue_angle(a1_adjusted, b1)
    hue_angle2 = calculate_hue_angle(a2_adjusted, b2)

    #calculating deltas
    delta_lightness_prime = l2 - l1
    delta_chroma_prime = chroma2_adjusted - chroma1_adjusted
    delta_hue_angle_prime = 0.0
    #shift based on distance in 360° circle
    if(abs(hue_angle2 - hue_angle1) <= 180.0):
        delta_hue_angle_prime = hue_angle2 - hue_angle1
    elif(hue_angle2 - hue_angle1 > 180.0):
        delta_hue_angle_prime = hue_angle2 - hue_angle1 - 360.0
    else:
        delta_hue_angle_prime = hue_angle2 - hue_angle1 + 360.0

    delta_hue_distance = 2 * math.sqrt(chroma1_adjusted * chroma2_adjusted) * math.sin(math.radians(delta_hue_angle_prime) / 2)

    #calculate average lightness, chroma and hue
    average_lightness_prime = (l1+l2) / 2.0
    average_chroma_prime = (chroma1_adjusted + chroma2_adjusted) / 2.0
    average_hue_prime = 0.0
    if chroma1_adjusted == 0 or chroma2_adjusted == 0:
        average_hue_prime = hue_angle1 + hue_angle2
    elif abs(hue_angle1 - hue_angle2) <= 180.0:
        average_hue_prime = (hue_angle1 + hue_angle2) / 2.0
    elif hue_angle1 + hue_angle2 < 360.0:
        average_hue_prime = (hue_angle1 + hue_angle2 + 360.0) / 2.0
    else:
        average_hue_prime = (hue_angle1 + hue_angle2 - 360.0) / 2.0

    #calculate weights
    lightness_weight = 1 + (0.015 * (average_lightness_prime - 50)**2) / math.sqrt(20 + (average_lightness_prime - 50)**2)
    chroma_weight = 1 + 0.045 * average_chroma_prime
    t_factor = (1 - 0.17 * math.cos(math.radians(average_hue_prime - 30)) +
             0.24 * math.cos(math.radians(2 * average_hue_prime)) +
             0.32 * math.cos(math.radians(3 * average_hue_prime + 6)) -
             0.20 * math.cos(math.radians(4 * average_hue_prime - 63)))
    
    hue_weight = 1 + 0.015 * average_chroma_prime * t_factor

    #parameters (default is 1.0 all)
    kL = 1.0
    kC = 1.0
    kH = 1.0

    #rotation terms
    rotation_chroma_factor = (2 * math.sqrt(average_chroma_prime**7/ (average_chroma_prime**7 + 25**7)))
    delta_theta = (30* math.exp(-((average_hue_prime - 275) / 25) ** 2))
    rotation_term = -rotation_chroma_factor * math.sin(math.radians(2 * delta_theta))

    #calculate final terms
    lightness_parametric_factor = delta_lightness_prime / (kL * lightness_weight)
    chroma_parametric_factor = delta_chroma_prime / (kC * chroma_weight)
    hue_parametric_factor = delta_hue_distance / (kH * hue_weight)

    return math.sqrt(lightness_parametric_factor**2 + chroma_parametric_factor**2 +
                      hue_parametric_factor**2 + rotation_term * chroma_parametric_factor * hue_parametric_factor)

def calculate_hue_angle(a_adjusted, b):
    if(a_adjusted == 0 and b == 0):
        return 0
    h = math.degrees(math.atan2(b,a_adjusted))
    if h >= 0:
        return h
    else:
        return h + 360.0
