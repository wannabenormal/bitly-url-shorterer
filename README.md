# Bitly url shorterer

This script convert the link into bitly-link or count clicks for bitly-link.

### How to install

1. You should be registered in [bit.ly](https://bit.ly)
2. Get your Access Token from [your profile settings page](https://app.bitly.com/settings/api/).
It should look like `8549a1c19c305f84d7d5d40049886dd7809daefa`
3. Put your accsess token in `.env` file (you need create it):
```
BITLY_TOKEN="YOUR_ACCESS_TOKEN"
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
You may want to isolate your environment with [venv](https://docs.python.org/3/library/venv.html)

4. Run the script with `python` (or `python3`) with link as an argument:
```
python main.py https://google.com
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).