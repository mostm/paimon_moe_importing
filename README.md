# paimon_moe_importing
Export your history from hotgames.gg and import it to paimon.moe tool

## Setting up
1. `git clone https://github.com/mostm/paimon_moe_importing.git`
2. `cd paimon_moe_importing`
3. `pipenv sync`

## Running
Execute `pipenv run python banner_parser.py` to generate history banner list based on Fandom wiki (I hope they don't rework that...)
Execute `pipenv run python main.py` to generate Excel file for usage on the site, seems to work properly.
