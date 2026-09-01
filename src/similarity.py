# hardcoded threshholds for the similarity rating
#RGB and HSV are far less meaningful than CIE76 and CIEDE2000
RGB_THRESHOLDS = [20, 50, 100, 175]
HSV_THRESHOLDS = [0.05, 0.10, 0.20, 0.35]
CIE76_THRESHOLDS = [2, 5, 10, 20]
CIEDE2000_THRESHOLDS = [2, 5, 10, 20]


def get_similarity_level(distance, thresholds):
    if distance <= thresholds[0]:
        return "Very good match", "green"
    if distance <= thresholds[1]:
        return "Good match", "limegreen"
    if distance <= thresholds[2]:
        return "Moderate match", "gold"
    if distance <= thresholds[3]:
        return "Bad match", "orange"
    return "Very Bad match", "red"