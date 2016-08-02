from __future__ import print_function
from stevedore import driver
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dog',
        nargs='?',
        default='dog',
        help='nothing',)
    parserd_args = parser.parse_args()
    mgr = driver.DriverManager(
        namespace='stevedore.example.sayhello',
        name=parserd_args.dog,
        invoke_on_load=True,
    )

    mgr.dirver.sayhello('jj')
