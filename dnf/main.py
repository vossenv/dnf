import json

from pathlib import Path
import numpy as np


def run():

    folder = '/Users/swampfox/Documents/Audio/NAM/all_models'

    # folder = "D:\\CaptureTraining\\dnf_test"
    #
    pathlist = Path(folder).rglob('*.nam')
    for path in pathlist:
        oldname = str(path)
        # print(oldname)

        with open(oldname, "r") as f:
            z = json.load(f)
            hash = z['weights']

            # z['weights'] = []
            # print("{} to {}".format(min(hash), max(hash)))
            print(sum(hash))

    print('banana')


if __name__ == '__main__':
    run()
