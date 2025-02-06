# Bingo Card Generator

I was organizing an event in which we were going to have a few rounds of bingo, and I saw that we didn't have the cards.

I decided to challenge myself and write this algorithm on my own, generating random bingo cards and outputting them to a pdf so that I could print them out later.

## Cards params

On **main.py** you can set the followings params:
- ***center_image_path***: path to the image you want to place in the middle of the card 
- ***number_of_cards***: number of cards you want to generate
- ***filename***: output filename

## Generate card using Docker

To generate the command using docker just run the code below:
```bash
docker-compose up app
```

## Generate card using your machine's python

To generate the commands using python just run the code below:
```bash
pip install -r requirements.txt
```
```bash
python main.py
```