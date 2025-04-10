c: int = 299792458  # The speed of light in m/s

def energy():
    m: float = float(input("Enter kilos of mass: "))
    print("e = m * C^2")
    print("Mass = " + str(m) + " kg")
    print("C = " + str(c) + " m/s")
    print("e = " + str(m * c**2) + " joules")

if __name__ == "__main__":
    energy()