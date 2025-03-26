// Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
const API_KEY = '77b3c9ee14bef7b6097ec01a833c37e8';
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

/**
 * Fetch weather data for a given city.
 * @param {string} city - The name of the city.
 */
async function getWeather(city) {
    try {
        const response = await fetch(`${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }
        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        console.error('Failed to fetch weather data:', error.message);
    }
}

/**
 * Display weather data in the console.
 * @param {object} data - The weather data object.
 */
function displayWeather(data) {
    console.log(`Weather in ${data.name}, ${data.sys.country}:`);
    console.log(`Temperature: ${data.main.temp}°C`);
    console.log(`Weather: ${data.weather[0].description}`);
    console.log(`Humidity: ${data.main.humidity}%`);
    console.log(`Wind Speed: ${data.wind.speed} m/s`);
}

// Example usage: Replace 'London' with the desired city name
getWeather('London');