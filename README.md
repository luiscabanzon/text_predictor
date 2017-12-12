# Text Predictor
[Author: Luis Cabanzon](https://luiscabanzon.com/)

N-gram based text predictor. Currently only in Ensglish and trained with a corspus of 50,000 document.
Next irerations:
- Increase corpus size.
- Additional languages (German, Russian).

Currently data is stored in JSON, for the sake of simplicity and portability. Future iterations may migrate to an SQLite or MongoDB database.

Once the API is running (built with Flask), predictions are retrieved from the path http://localhost:5000/predict/ followed by the input text with "-" instead of spaces (e.g. http://localhost:5000/predict/i-would-like-to).
The JSON response contains 2 lists, one with a list of candidates for the next word and another list with candidates for the next 2 words).
