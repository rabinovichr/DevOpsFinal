# DevOpsFinal
Robert and Francis

[Finnhub](https://finnhub.io)

[Finnhub Python](https://github.com/Finnhub-Stock-API/finnhub-python)

This is what we want to use from finnhub to get the quote for a stock:

``` bash
import finnhub
finnhub_client = finnhub.Client(api_key="YOUR API KEY")
finnhub_client.quote('AAPL')
```
This is the response:
```json
{
  "c": 261.74,
  "h": 263.31,
  "l": 260.68,
  "o": 261.07,
  "pc": 259.45,
  "t": 1582641000 
}
```