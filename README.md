# lowecho

echo step by step

works on python 3.10.4 and possibly other too

## help

```
$ ./lowecho.py -h

usage: lowecho [-h]
               [-p {default,typewriter,coding,noob,retrowave,hacking,tty,dataleak}]
               [-s] [-i INTERVAL] [-I INTERVAL_STDEV] [-c COUNT]
               [-C COUNT_STDEV]

options:
  -h, --help            show this help message and exit
  -p {default,typewriter,coding,noob,retrowave,hacking,tty,dataleak}, --preset {default,typewriter,coding,noob,retrowave,hacking,tty,dataleak}
                        default values for all options, where:
                        - default: interval=0.01, interval_stdev=0, count=1, count_stdev=0
                        - typewriter: interval=0.2, interval_stdev=0.1, count=1, count_stdev=0
                        - coding: interval=0.15, interval_stdev=0.05, count=1, count_stdev=0.5
                        - noob: interval=0.5, interval_stdev=0.3, count=1, count_stdev=0
                        - retrowave: interval=0.25, interval_stdev=0.05, count=3, count_stdev=2
                        - hacking: interval=0.007, interval_stdev=0, count=1, count_stdev=0
                        - tty: interval=0.007, interval_stdev=0, count=5, count_stdev=3
                        - dataleak: interval=0.001, interval_stdev=0, count=10, count_stdev=0
  -s, --skip-spaces     skip all spaces, newlines, tabs... etc
  -i INTERVAL, --interval INTERVAL
                        interval in seconds between each char (rounded off)
  -I INTERVAL_STDEV, --interval-stdev INTERVAL_STDEV
                        stdev for interval
  -c COUNT, --count COUNT
                        number of chars to print out on each step (rounded off)
  -C COUNT_STDEV, --count-stdev COUNT_STDEV
                        stdev for count
```
