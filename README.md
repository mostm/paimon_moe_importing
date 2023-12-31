# paimon_moe_importing
Export your history from hotgames.gg and import it to paimon.moe tool

## Setting up
0. If you don't have pipenv, run `pip install pipenv`
1. `git clone https://github.com/mostm/paimon_moe_importing.git`
2. `cd paimon_moe_importing`
3. `pipenv sync`

## Getting the history from hotgames.gg
1. Go to https://genshin.hotgames.gg/wish-counter
2. Press F12 to open the developer menu and go to the `Network` tab.
3. While it is open, refresh the page.
4. After a few seconds, use the `Filter by URL` bar and type  `genshin_wish_history`
5. Right click on the request that appears and click `Open in new tab`
6. Press `Ctrl + S` and save the json file in the `paimon_moe_importing` folder without renaming it (it sould be called `genshin_wish_history.json`).

## Running
- Execute `pipenv run python banner_parser.py` to generate history banner list based on Fandom wiki (I hope they don't rework that...)
- Execute `pipenv run python main.py` to generate Excel file for usage on the site, seems to work properly. The generated file is called `generated_history.xlsx`.
- On paimon.moe, click on `Settings` at the top of the wish page and click on `Import from Excel`. Drag and drop or select the `generated_history.xlsx` file.
