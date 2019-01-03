# Wizard's Apprentice (1.0.0)
The wizard needs your help - he needs to fight the evil dragon, but he forgot what the tool for his latest spell looks like. Take pictures of what his tool looks like and the wizard will award you with points - compete with your friends for top points.

## Authors
Joyce Liao, Hannah Sindorf, Scott Currie

## Overview
Users are given a randomized prompt consisting of a few keywords (e.g. "blue sports car and a person"). When they submit a photo that they believe fills those keywords, it is evaluated by google vision API and the returned tags are matched against the prompt. When the prompt is fulfilled, points are awarded and a new prompt is generated.

Users have a unique login where their own points are tracked.

## Stretch goals
- video game-styled UI with characters.
- make it a social game. Users share the same prompt and only the winning user is awarded points. Photos are posted into a public feed.
- look at photo headers to determine that the photo was taken the same day (to avoid cheating)
- add a report feature in case it's obvious the photo is just a stock photo

## Getting Started
Navigate to https://rebrand.ly/wizards_apprentice.  

To run locally:  
1. Enter a new virtual environment: `pipenv shell --python 3.6`
2. Install dependencies: `pipenv install`
3. Create .env file in the root of the project.
4. Create a postgresql database for the app
5. Run Flask db init, migration, upgrade
6. Run the app: `flask run`
7. Navigate to http://localhost:5000

## Architecture
Requires Python >= 3.6, Flask, PostgreSQL, Pillow

### Frontend
Server-side rendered HTML templates using Jinja2.

### Backend
Flask, PostgreSQL. Deployed on EC2 (Ubuntu 18.04) running Nginx and Gunicorn

## Credits

### Sample code/tutorials used

- [Uploading files to S3 from Flask](http://zabana.me/notes/upload-files-amazon-s3-flask.html)
- [Styling HTML5 form file uploads](https://tympanus.net/codrops/2015/09/15/styling-customizing-file-inputs-smart-way/)

### Assets Used

- [Free Pixel Art Forest](https://edermunizz.itch.io/free-pixel-art-forest) - Website background
- [NES.css](https://github.com/nostalgic-css/NES.css) - NES-style CSS framework


## Change Log
12-27-2018    09:00:00    Project Started  
12-27-2018    10:30:00    Flask app set up  
12-27-2018    11:30:00    Google Vision API submissions working  
12-27-2018    12:00:00    User registration/authorization set up  
12-27-2018    12:00:00    Database layer implemented  
12-27-2018    15:00:00    App deployed to AWS  
12-27-2018    15:30:00    Submission evaluations working  
12-27-2018    17:00:00    First tests of front end user experience  
12-28-2018    09:00:00    Begin Day 2  
12-28-2018    14:00:00    Improved submission evaluation logic  
12-28-2018    15:30:00    Player history and all players history complete  
12-28-2018    16:00:00    Basic styling complete 
01-02-2019    09:00:00    Begin Day 3  
01-02-2019    11:00:00    Time conversions from UTC to PDT working  
01-02-2019    12:00:00    Color detection improved  
01-02-2019    13:30:00    Testing on auth routes complete  
01-02-2019    16:00:00    Admin page added    
