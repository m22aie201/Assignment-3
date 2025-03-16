namespace Assignment_3_API
{
    public class WeatherService : IWeatherService
    {
        public async Task<string> GetCurrentWeather(string city, string country)
        {
            using HttpClient client = new HttpClient();
            string response = string.Empty;

            try
            {
                string url = $"https://api.weatherbit.io/v2.0/current?&city={city}";

                if (!string.IsNullOrEmpty(country))
                {
                    url += $"&country={country}";
                }

                url += $"&key=f2199fd7aa4041b185e341b8cfb1948c";
                HttpResponseMessage httpResponse = await client.GetAsync(url);

                httpResponse.EnsureSuccessStatusCode();

                response = await httpResponse.Content.ReadAsStringAsync();
            }
            catch (HttpRequestException e)
            {
                throw new Exception(e.Message);
            }

            return response;
        }
    }
}
