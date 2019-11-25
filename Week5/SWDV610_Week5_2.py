# Patrick Johnson        11/24/2019 #
# SWDV 610 3W 19/FA2    Week 5 - #2 #
#####################################
# Build a script that utilizes at least one list and one dictionary

# Dictionary of color names, with RGB values stored as lists.
colors = { "Red":   [255,  0,  0],
           "Blue":  [  0,  0,255],
           "Green": [  0,255,  0],
           "Linen": [250,240,230]}

for color in colors:
    rgb = colors[color]
    print("Name: {:12} Red: {:3}   Green: {:3}   Blue: {:3} "
          .format(color,rgb[0],rgb[1],rgb[2]))