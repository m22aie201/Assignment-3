namespace Assignment_3_API
{
    public class AnimalFactsService : IAnimalFactsService
    {
        public async Task<string> GetCatFacts()
        {
            using HttpClient client = new HttpClient();
            string response = string.Empty;

            try
            {
                string url = "https://catfact.ninja/fact";
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
