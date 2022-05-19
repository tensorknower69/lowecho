#!/usr/bin/env python

import argparse
import sys
import time
import random
from typing import NamedTuple

def lowecho(inpipe, outpipe, *, interval, interval_stdev, count, count_stdev, skip_spaces):
    while True:
        to_read = max(1, round(random.normalvariate(count, count_stdev)))

        while to_read > 0:
            in_ = inpipe.read(to_read)
            if not in_:
                return

            outpipe.write(in_)
            outpipe.flush()

            if skip_spaces:
                to_read -= len([ch for ch in in_ if not ch.isspace()])
            else:
                break

        to_wait = max(0, random.normalvariate(interval, interval_stdev))
        time.sleep(to_wait)

PRESETS = {
        "default"   : {"interval": 0.01 , "interval_stdev": 0   , "count": 1 , "count_stdev": 0  },
        "typewriter": {"interval": 0.20 , "interval_stdev": 0.1 , "count": 1 , "count_stdev": 0  },
        "coding"    : {"interval": 0.15 , "interval_stdev": 0.05, "count": 1 , "count_stdev": 0.5},
        "noob"      : {"interval": 0.5  , "interval_stdev": 0.3 , "count": 1 , "count_stdev": 0  },
        "retrowave" : {"interval": 0.25 , "interval_stdev": 0.05, "count": 3 , "count_stdev": 2  },
        "hacking"   : {"interval": 0.007, "interval_stdev": 0   , "count": 1 , "count_stdev": 0  },
        "tty"       : {"interval": 0.007, "interval_stdev": 0   , "count": 5 , "count_stdev": 3  },
        "dataleak"  : {"interval": 0.001, "interval_stdev": 0   , "count": 10, "count_stdev": 0  },
        }

def exec_main():
    root = argparse.ArgumentParser("lowecho", formatter_class=argparse.RawTextHelpFormatter)

    root.add_argument("-p", "--preset", default="default", choices=PRESETS.keys(),
            help="default values for all options, where:" + "".join([f"\n- {key}: " + ", ".join([f"{what}={value}" for what, value in values.items()]) for key, values in PRESETS.items()]))
    root.add_argument("-s", "--skip-spaces",
            action="store_true", help="skip all spaces, newlines, tabs... etc")
    root.add_argument("-i", "--interval",
            type=float, help="interval in seconds between each char (rounded off)")
    root.add_argument("-I", "--interval-stdev", dest="interval_stdev",
            type=float, help="stdev for interval")
    root.add_argument("-c", "--count",
            type=float, help="number of chars to print out on each step (rounded off)")
    root.add_argument("-C", "--count-stdev", dest="count_stdev",
            type=float, help="stdev for count")

    args = root.parse_args()
    preset = PRESETS[args.preset]
    del args.__dict__["preset"]
    try:
        lowecho(sys.stdin, sys.stdout, **{**preset, **{what: value for what, value in args.__dict__.items() if not (value is None)}})
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    exec_main()
