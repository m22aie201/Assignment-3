namespace Assignment_3_API
{
    public interface IWeatherService
    {
        Task<string> GetCurrentWeather(string city, string country);
    }
}
