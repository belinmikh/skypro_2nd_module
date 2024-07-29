# **WIDGET FOR SHOWING LAST FEW SUCCEED TRANSACTIONS** 
# Scroll through the commands to read the description of the versions
#### initialized with poetry, to install dependencies run:
```shell
poetry install
```
#### run pytest coverage check to get html report:
```shell
pytest --cov=src --cov-report=html
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