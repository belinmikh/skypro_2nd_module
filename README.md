# **WIDGET FOR SHOWING LAST FEW SUCCEED TRANSACTIONS** 

## version 10.0:
    
    > main logic created using tkinter

# Scroll through the commands to read the description of previous versions
## run main logic:
```shell
python main.py
```
#### initialized with poetry, to install dependencies run:
```shell
poetry install
```
#### if you are not on Windows os, you should install tkinter
#### command example for Ubuntu:
```shell
sudo apt-get install python3-tk
```
#### run pytest coverage check to get html report:
```shell
pytest --cov=src --cov-report=html
```
### v7.0 Python Console manual get-request test:
```python
from src.external_api import convert_to_rub
amount = convert_to_rub(20.0, 'USD')
print(f"... but 20$ is 20$ ({amount} RUB)")
```
### test reading json-file, that is achievable at data/operations.json:
```python
from src.utils import read_json_local
A = read_json_local('data/operations.json')
print(type(A))
for i in range(5):
    print(f"{type(A[i])}: {A[i]}")
print("... and many others which I don't want to print because I'm just showing possibility")
```
### run v5.0 manual tests _(you can see i/o that way)_
### all new functionality at the same time (don't recommend, looks like a chaos):
```shell
python main.py v5.0
```
### or just one of new functions:
```shell
python main.py v5.0 card_number_generator
```
```shell
python main.py v5.0 filter_by_currency
```
```shell
python main.py v5.0 transaction_descriptions
```
### run v3.1 and v2.3 manual tests _(you can see i/o that way)_:
```shell
python main.py v3.1
```
```shell
python main.py v2.3
```

## version 9.0:

    > new functions added to fileio new module,
        use just general function file_to_list()
        to convert .xlsx or .csv files to list
        of transactions in dictionaries

## version 8.0:
    
    > added logger to masks and utils modules with logging library

## version 7.1:
    
    > reading empty file bug fixed

## version 7.0:

    > added convert_to_rub function in new external_api module,
        which provides GET-request to Exchange Rated Data APILayer
        (you must have API key in .env, check the example)
    > added read_json_local function in new utils module,
        which transforms .json file with transactions
        to list of dictionaries
    > added get_rub_amount in utils module,
        which gets amount out of transaction dictionary
        and converts it to RUB amount if necessary

## version 6.0:

    > added output() function for technical usage in logging 
    > added logging decorator at new decorators.py module, usage:
        @log()
        def func(...):
            # logging to console
            ...
        @log('file.txt')
        def func(...):
            # logging to file.txt
            ...

## version 5.0:

    > added card_number_generator, filter_by_currency, transaction_descriptions
        new functions in generators.py new module
        (see full description in docstring)
    > added new function extract() in tools.py new module,
        (something tells me I'll use it again,
        just got freak out by idea of nested
        key existance checking and evaluating
        values from it, bruh...
        see full description in docstring)

## version 4.0:

    > added pytest and pytest-cov to dev group
    > covered all created functions with tests
    > current coverage 100%
    > minor bug fixes

source: [https://www.asciiart.eu/text-to-ascii-art](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

    ███████╗██╗███╗   ██╗ █████╗ ██╗     ██╗  ██╗   ██╗.............................
    ██╔════╝██║████╗  ██║██╔══██╗██║     ██║  ╚██╗ ██╔╝.............................
    █████╗  ██║██╔██╗ ██║███████║██║     ██║   ╚████╔╝ .............................
    ██╔══╝  ██║██║╚██╗██║██╔══██║██║     ██║    ╚██╔╝  .............................
    ██║     ██║██║ ╚████║██║  ██║███████╗███████╗██║▄█╗.............................
    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝.............................
    .................................%%%%%...%%..%%..%%%%%%..%%%%%%...%%%%...%%%%%%.
    .................................%%..%%...%%%%.....%%....%%......%%........%%...
    .................................%%%%%.....%%......%%....%%%%.....%%%%.....%%...
    .................................%%........%%......%%....%%..........%%....%%...
    .................................%%........%%......%%....%%%%%%...%%%%.....%%...
    ..   ..............:^:::::...:^^:....::::::^::^^::::::::^^^^::^::^^^^^:^^^~~~^::
            ...       .:^^::^:...:^^^^^~!777?JJJ?!!^:::::::^^^^:::^::^^^^^^^^^~~~^::
        .   ...........:^^::^:...:^~7JY555555PPPP5J~^^:::::^^^^^::^::^^^^^^^^~~~^^^^
    ............:..::.:^^^::::..^7JYY555555YYYYY55YY?!~.:::::::::::::^^^^^^^~~~~^^^^
    ...................:^^:::.!J555YYYYY55555555YY5J~::.:~!7???77!~^::^^^^^^~~~~^^^^
    ...................:^:::::JYYYYYYYY5555PPP5YYYY5J?!~YGGGPP5YYYJJ7~^:^^^^~~!!^^^^
    ...................:^:::::JYY55555YYY5555555YJ5P5J7^?PPPPP5J7!!!7??7^^^^~~~~^^^^
    ...................:^:::::J5YYYYY555PPPYYPGP5YYJJ???Y5555555J!~~~?JYJ~^~!!!~^^^^
    ...................:^::::.!YJY55PGGGGGPP_______!7WWWWWWWWWWWWWWWWWWWP?^!!!7~^^^:
    ...................:^::::.~JYY5PPPPP555J!     |?|*******************|J~7!!7~^^~~
    ...................:^::::.~JJYY5555555?:|     |Y|*******************|J!7???7777?
    ...................:^::::~?JJYY5555YYJ~:|     |J|********/\*********|JJ55PPPGP5Y
    :::::::::::.......::^::^7JYYYYY5YYJJJ?^:|     |J--------//\\--------YYPJJYYY5YYY
    ^^^^^^^^:::::::____^^~?JJJYYJJYYJJJJ?!..|     |?7??J?J5P55YJJJJYYJJJYP5^:^^^^^~7
    ::::::::::::__/::::~7?JJJJYYYYYYYYJ7^~..|     |??JYJJJY5P55YYYY55YJJ5Y7~~!~^^!7?
    ^^^^^^^^^^^/::::::?Y?JJJYYYYYYYJ7~^::~..|*****|J?JJY555GG**555P5YYJ77!~!!!~^~7?J
    ^^^^^^^^^^/:::::.^B5JYYYYYYYYJ7~^^^^~!..|*****|????J************YYJ!~~~~!!~^~!??
    77777!!~/^::::::.^?55YYYYYYJ?!~~~~~~~...|*****|???YYY555****5YY55Y7~~~~~!~^^~!7~
    7777!~/^:::::::.:^::!J5PP557^~~~~~~~~...|*****|^!?JJJYYYY5555YYYJJ^:^~~~~~^^~!!~
    !!!!:|^:::::::::^^^:::^!7?7~^~^^^^^^^~...\***/:.:7JYY55PPPP55YY55J^.:^^^^^^^^!~^
    !!~:.|^^^^^^^^^^^^:::::::::^:::::...:::::........:?YYY55555555P55P^:..:^^:::^~~:
    !^:..|~77!~~^^^^^^:::^::::::....::..:::::::::::.:.:!YPP555PPP5PGP~.:....:::^^~^:
    ^:::::\^~~~~~^^^^^^^^:::...::::::::::::::::::::::::.:~?YPPPPPGBJ:::^.......::^^:
    ::::::::------\______::::::::::::^::::::::::::::::::::.:^?5GG5!::::^:...........
    :::::::::::::::::::::\------:::^^^^::::::::::::::::::::::~J5J7^::::::...........

## version 3.1:

    //Made for <jul, 22> tasks//

    > Added sort_by_date function in processing module
        (see full description in docstring)
    > Test of new function available at main.py

## version 3.0:

    //Made for <jul, 22> tasks//

    > GitHub is on!
    > Added filter_by_state function in new processing module
        (see full description in docstring)
    > Test of new module available at main.py
    > Every docstring corrected

## version 2.3:

    //Made for experimental issues//

    Yes, we'll have pytest soon, but it was horrible to see mypy crying, so:

    > Added function for testing other functions
        (functest at main.py)

## version 2.2:
    
    //Made for <jul, 17> tasks//
    
    > Function get_time is available
        at new module widget.py
        (there is a docstring description)
    > See some new features tests at main.py

## version 2.1:

    //Made for <jul, 17> tasks//

    > Function mask_account_card is available
        at new module widget.py
        (there is a docstring description)
    > See some new features tests at main.py

## version 2.0:

    //Made for <jul, 17> tasks//

    > Git is on!
    > Code of first commit equals to v1.0

## version 1.0:
    
    //Made for <jul, 15> tasks//
    
    > Basic project structure have been created
    > Some code design tools have been initialized:
        - flake8
        - black
        - mypy
        - isort
    > Mask functions (src/masks.py) have been created:
        - get_mask_card_number for hiding card number
        - get_mask_account for hiding account number
    > Tests for new functions have been added to main.py
        (temporarily, it will be replaced to tests/ in future versions)

### _sky.pro // indpd58.0 // Belin Mikhail_