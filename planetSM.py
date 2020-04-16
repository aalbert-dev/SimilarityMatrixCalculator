# similiarty between two plants as defined below with gravitational constants K1, K2, K3
# similarity(d1, d2, r1, r2, m1, m2) = (K1 * (d1 - d2) ** 2 + K2 * (r1 - r2) ** 2 + K3 * (m1 - m2) ** 2) ** 0.5
def similarity(d1, d2, r1, r2, m1, m2):
    return (3.5 * 10 ** -7 * (d1 - d2) ** 2 + 1.6 * 10 ** -5 * (r1 - r2) ** 2 + 1.1 * 10 ** -27 * (m1 - m2) ** 2) ** 0.5

# calculate and print similiarity function for each pair of planets
def calculateMatrix():
    for planet1 in planets:
        row = ""
        for planet2 in planets:
            row += str(similarity(planet1[1], planet2[1], planet1[2], planet2[2], planet1[3], planet2[3])) + " "
        print(row)

# print average similiarty of all planets as sum of similarities / num planets
def calculateAverage():
    for planet1 in planets:
        total = 0
        for planet2 in planets:
            total += similarity(planet1[1], planet2[1], planet1[2], planet2[2], planet1[3], planet2[3])
    print("Average: " + str(total // 81))

# sample planets with fields: "planet name", distance to sun, radius, and mass
planets = [ ("Jupiter", 778000, 71492, 1.90 ** 27),
            ("Saturn", 1429000, 60268, 5.69 ** 26),
            ("Uranus", 2870990, 25559, 8.69 **25),
            ("Neptune", 4504300, 24764, 1.02 ** 26),
            ("Earth", 149600, 6378, 5.98 ** 24),
            ("Venus", 108200, 6052, 4.87 ** 24),
            ("Mars", 227940, 3398, 6.42 ** 23),
            ("Mercury", 57910, 2439, 3.30 ** 23),
            ("Pluto", 5913520, 1160, 1.32 ** 22) ]

# run program        
calculateMatrix()
calculateAverage()  