class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"The fare is:{self.fare}")
        print(f"The distance is: {self.distance}")
        print(f"The rate per km is: {self.rate_per_km}")

def main():
    # your program
    taxi1 = TaxiRide(1)
    taxi1.distance = 4
    taxi1.rate_per_km = 2
    taxi1.calculate_fare()
    taxi1.print_receipt()
    
    taxi2 = TaxiRide(2)
    taxi2.distance = 5
    taxi2.rate_per_km = 3
    taxi2.calculate_fare()
    taxi2.print_receipt()
if __name__ == "__main__":
    main()
