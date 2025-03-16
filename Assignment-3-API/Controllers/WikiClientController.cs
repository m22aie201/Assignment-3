using Microsoft.AspNetCore.Mvc;

namespace Assignment_3_API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WikiClientController : ControllerBase
    {
        IWeatherService _wetherService;
        IAnimalFactsService _animalFactsService;
        private readonly ILogger<WikiClientController> _logger;

        public WikiClientController(ILogger<WikiClientController> logger, IWeatherService weatherService, IAnimalFactsService animalFactsService)
        {
            _logger = logger;
            _wetherService = weatherService;
            _animalFactsService = animalFactsService;
        }

        [HttpGet("/weather")]
        public string Get(string city, string country = "")
        {
            return _wetherService.GetCurrentWeather(city, country).Result;
        }

        [HttpGet("/cat")]
        public string GetCatFacts()
        {
            return _animalFactsService.GetCatFacts().Result;
        }
    }
}