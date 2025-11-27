from mcp.server.fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the MCP server
mcp = FastMCP("Weather Service")

# Get API key from environment variable
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a specified city.
    
    Args:
        city: The name of the city (e.g., "London", "Chennai", "New York").
    """
    if not API_KEY:
        return "Error: OPENWEATHER_API_KEY environment variable not set. Please get a free API key from https://openweathermap.org/api"
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            return f"{city}: {description}, {temp}°C (Humidity: {humidity}%)"
        elif response.status_code == 404:
            return f"City '{city}' not found. Please check the spelling."
        else:
            return f"Error fetching weather data: {response.status_code}"
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def calculate_travel_time(origin: str, destination: str, mode: str = "car") -> str:
    """
    Calculate estimated travel time between two cities.
    
    Args:
        origin: Starting city
        destination: Destination city
        mode: Mode of transport (car, train, plane)
    """
    # Simulated logic
    base_time = 2 # hours
    if mode == "plane":
        return f"Estimated flight time from {origin} to {destination} is {base_time} hours."
    elif mode == "train":
        return f"Estimated train ride from {origin} to {destination} is {base_time * 3} hours."
    else:
        return f"Estimated drive from {origin} to {destination} is {base_time * 5} hours."

@mcp.tool()
def get_forecast(city: str, days: int = 3) -> str:
    """
    Get a weather forecast for the next few days.
    
    Args:
        city: The name of the city.
        days: Number of days to forecast (1-5, default 3).
    """
    if not API_KEY:
        return "Error: OPENWEATHER_API_KEY environment variable not set."
    
    # OpenWeatherMap free tier supports 5-day forecast
    days = min(days, 5)
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            forecasts = []
            
            # API returns 3-hour intervals, take one per day (every 8th entry)
            for i in range(0, min(days * 8, len(data["list"])), 8):
                item = data["list"][i]
                date = item["dt_txt"].split()[0]
                temp = item["main"]["temp"]
                description = item["weather"][0]["description"].capitalize()
                forecasts.append(f"{date}: {description}, {temp}°C")
            
            return f"Forecast for {city}:\n" + "\n".join(forecasts)
        elif response.status_code == 404:
            return f"City '{city}' not found."
        else:
            return f"Error fetching forecast: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_alerts(city: str) -> str:
    """
    List active weather alerts for a city.
    
    Args:
        city: The name of the city.
    """
    # Simulated alerts
    if city.lower() in ["london", "seattle"]:
        return "ALERT: Heavy Rain Warning in effect until 8:00 PM."
    elif city.lower() in ["tokyo", "san francisco"]:
        return "ALERT: High Wind Advisory."
    else:
        return "No active weather alerts for this location."

if __name__ == "__main__":
    # This runs the server over Stdio by default
    mcp.run()
