from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info
from os import path as ospath, environ
from subprocess import run as srun
from requests import get as rget
from dotenv import load_dotenv, dotenv_values
if ospath.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)
basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)
load_dotenv('config.env', override=True)
try:
    if bool(environ.get('_____REMOVE_THIS_LINE_____')):
        log_error('The README.md file there to be read! Exiting now!')
        exit()
except:
    pass
BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    log_error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)
bot_id = BOT_TOKEN.split(':', 1)[0]
UPSTREAM_REPO = "https://github.com/drzlm/mirror-leech-telegram-bot"
UPSTREAM_BRANCH = 'master'
if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])
    update = srun([f"git init -q \
                     && git config --global user.email e.anastayyar@gmail.com \
                     && git config --global user.name mltb \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
    if update.returncode == 0:
        log_info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        log_error(
            'Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
