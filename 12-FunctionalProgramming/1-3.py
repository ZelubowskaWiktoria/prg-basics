# Takes speed in m/s
n1 = int(input("Enter speed in m/s: "))


# Calculates speed in km/h
def ms_to_kmh(ms):
    result = n1 * 3,6
    return result

print(f"The speed is {result} km/h")