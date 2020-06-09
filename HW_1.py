def tripCost(distanceKM, vehSpeedKPH, kWHoursPer100KM, electricityCostPerKWH,
             hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay):

    hours = distanceKM / vehSpeedKPH

    kilowattHours = (distanceKM*100)/kWHoursPer100KM

    totalElectricBill = electricityCostPerKWH*kilowattHours

    time = hours/8.0
    nights = math.ceil(time) - 1
    remainingTrip = time - nights


    totalHotelBill = hotelCostPerNight*nights
    totalFoodBill = (breakfastCostPerDay + dinnerCostPerDay) * nights
    lunchBill = nights*lunchCostPerDay
    if remainingTrip < 0.5:
        lunchBill += lunchCostPerDay
    totalFoodBill += lunchBill

    totalCost = totalHotelBill + totalFoodBill + totalElectricBill
    print("The trip of {} kilometers requires {} hours ( {} nights hotel) and costs {}," +
          " including ${:.2f} for electricity, ${:.2f} for food, and ${:.2f} for hotel.".format(distanceKM, hours, nights, totalCost, totalElectricBill, totalFoodBill, totalHotelBill))

    return

def testTripCost():
    tripCost(200.00, 40.00, 16.6, 0.12, 100.0, 5.0, 7.0, 13.0)
    print("Cost should be $10.98.")
    tripCost(100.00, 10.00, 16.6, 0.12, 100.0, 5.0, 7.0, 13.0)
    print("Cost should be $126.99.")
