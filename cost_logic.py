from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_distance(city1, city2):
    geolocator =  Nominatim(user_agent="logistics_app")
    loc1 = geolocator.geocode(city1)
    loc2 = geolocator.geocode(city2)

    if not loc1 or not loc2:
        return None
    
    return geodesic(
        (loc1.latitude,loc1.longitude),
        (loc2.latitude,loc2.longitude)
    ).km

def estimate_cost(distance_km,
vehicle_type, fuel_price):
    mileage = {
        "Mahindra Jeeto" : 24,
        "Ashok Leyland Ecomet" : 8,
        "BharatBenz" : 9
    }

    margin = {
        "Mahindra Jeeto" : 300,
        "Ashok Leyland Ecomet" : 500,
        "BharatBenz" : 1000
    }
    if vehicle_type not in mileage:
        return None
    
    fuel_needed = distance_km / mileage[vehicle_type]
    fuel_cost = fuel_needed * fuel_price
    total_cost = fuel_cost + margin[vehicle_type]

    return{
        "distance_km" :round(distance_km, 2),
        "fuel_cost" : round(fuel_cost,2),
        "total_cost" : round(total_cost,2)
    }