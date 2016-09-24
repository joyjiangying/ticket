#! /usr/bin/env python3
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   ??????
    -g          ??
    -d          ??
    -t          ??
    -k          ??
    -z          ??

Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
from stations import stations
import requests

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    print(arguments)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # ??URL
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
     r = requests.get(url, verify=False)
    print(r.json())
 


if __name__ == '__main__':
    cli()
