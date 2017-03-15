# boggler
selenium bot for boggle (wordplays.com)

## How to run

Create and enter a virtual environment, run `pip install -r requirements.txt`

Edit boggler.py and insert your wordplays.com credentials (USER and PASSW variables).

To run the bot: `python boggler.py` and that's it.

The bot will start chrome (with ublock origin installed), go to boggle, read the dictionary, generate anagrams, and start entering them.
To increase performance we could check which anagrams generate contiguous regions but since the time isn't counted towards the score it doesn't matter.
Almost guaranteed to get the highest score every time.

## Hall of fame
![s1](http://i.imgur.com/PsKA1zW.png)
![s2](http://i.imgur.com/1OuxTF0.png)
![s3](http://i.imgur.com/vEVGyvC.png)
![s4](http://i.imgur.com/EGSHiim.png)
