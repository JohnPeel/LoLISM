League of Legends - Item Set Manager
====================================

```
usage: LoLISM [-h] [-F {json,link,json-oneline}] [-L LOL]
              [-s SUMMONER | -P FILE] (-m ITEMSET | -l LINK | -f FILE)
              (-i | -p)

optional arguments:
  -h, --help            show this help message and exit
  -F {json,link,json-oneline}, --format {json,link,json-oneline}
                        Select json, link, json-oneline.
  -L LOL, --lol_location LOL
                        Location of your LoL installation. (Example: "C:/Riot
                        Games/League of Legens")
  -s SUMMONER, --summoner SUMMONER
                        Summoner Name
  -P FILE, --prop_file FILE
                        Summoner Properties File
  -m ITEMSET, --itemset ITEMSET
                        ItemSet on selected Summoner
  -l LINK, --link LINK  ItemSet link
  -f FILE, --file FILE  ItemSet JSON file (- is stdin)
  -i, --inject          Inject ITEMSET into SUMMONER.
  -p, --print           Print ITEMSET to stdout. [DEFAULT]
```

```
usage: LoLISM-gui [-h] (-l LINK | -j JSON)

League of Legends - Item Set Manager

optional arguments:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  ItemSet Link
  -j JSON, --json JSON  JSON File
```