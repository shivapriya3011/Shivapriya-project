data=[
    [6, 1, 500, 1, 25],
    [9, 3, 800, 0, 5],
    [14, 6, 1200, 0, 0],
    [18, 9, 300, 1, 40],
    [22, 12, 1500, 1, 60],
    [7, 2, 400, 0, 10],
    [13, 7, 1000, 0, 15],
    [19, 11, 600, 1, 35],
    [21, 5, 700, 0, 5],
    [8, 8, 1100, 0, 0]
]



print("Average Delay by Departure Hour")

hour_delay = {}
hour_count = {}

for flight in data:
    hour = flight[0]
    delay = flight[4]
    
    if hour not in hour_delay:
        hour_delay[hour] = 0
        hour_count[hour] = 0
    
    hour_delay[hour] += delay
    hour_count[hour] += 1

for hour in hour_delay:
    avg = hour_delay[hour] / hour_count[hour]
    print("Hour:", hour, "Average Delay:", avg)



def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"


for flight in data:
    month = flight[1]
    delay = flight[4]
    
    season = get_season(month)
    flight.append(season)
    
    if delay > 15:
        flight.append(1)  
    else:
        flight.append(0)  



def predict_delay(dep_hour, month, distance, weather):
    
    score = 0
    
    
    if weather == 1:
        score += 30
    
   
    if dep_hour >= 18:
        score += 15
    
 
    if distance > 1000:
        score += 10
    
    
    if get_season(month) == "Winter":
        score += 20
    
    return score

print("\nSample Prediction:")
predicted = predict_delay(20, 12, 1400, 1)
print("Predicted Delay Minutes:", predicted)



weather_delays = 0
night_delays = 0
winter_delays = 0

for flight in data:
    if flight[3] == 1:
        weather_delays += 1
    if flight[0] >= 18:
        night_delays += 1
    if flight[5] == "Winter":
        winter_delays += 1

print("\nImportant Factors Causing Delay:")
print("Weather related flights:", weather_delays)
print("Night flights:", night_delays)
print("Winter flights:", winter_delays)
