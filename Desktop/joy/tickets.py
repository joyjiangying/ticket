#! /usr/bin/env python3
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   display help mene
    -g          gaotie
    -d          dongche
    -t          tekuai
    -k          kuaisu
    -z          zhida

Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
import requests
from stations import stations

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    print(from_station)
    to_station = stations.get(arguments['<to>'])
    print(to_station)
    date = arguments['<date>']
    print(date)
    # create URL
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date ,from_station,to_station)
    print(url)
    r = requests.get(url, verify=False)

    print(r.json())
if __name__ == '__main__':
    cli()
