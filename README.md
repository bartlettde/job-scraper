# Job Scraper
The goal of this project is to create a program that periodically checks the website of a number of specific companies for job opportunities and then send me a list with key information and a link to the application page. To learn more about this project, I wrote a brief blog post about the process and the decisions I made, which can be found [here](https://www.dbartlett.co.uk/).

## Current Companies Supported
Below is the list of websites that this project currently scrapes. More employers may be added in future.
- IDEO
- Frog Design
- Ammunition Group

## Prerequisite
Using Pip, install these packages before trying to install:
- Beautiful Soup 4 (Webscraping library)
- Pyfiglet (Optional - Creates a cool ASCII banner on startup

## Installation
The guide below talks through the process of installing this program on a Raspberry Pi, however these steps should work for any set up.
To install, follow the steps below:
- In the terminal, go to the folder on your machine that you would like to save this project in
- Run `git clone https://github.com/bartlettde/job-scraper.git`
- Go into the newly cloned folder
- Ensure the libraries above are installed
- Run `python3 main.py`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
