import json
from pathlib import Path
import random
import os


# def persist(pagedata):
#     with open('pagedata.html', 'w', encoding="utf-8") as f:
#         f.write(pagedata)
#
# def read():
#     with open('pagedata.html', 'r', encoding="utf-8") as f:
#         data = f.read()
#         return data

def randnam():
    folder = "D:\\CaptureTraining\\rnam"
    file = "Mesa Dual Rectifier 3ch 6L6 Red G7 ESR=0.01334 @ 12.2 dBu - vossen.nam"

    with open(folder + os.sep + file, "r") as f:
        model = json.load(f)

    weights = model['weights']

    for k in range(10):
        with open( folder + os.sep + "VAR {} - {}".format(k, file), "w") as f:
            model['weights'] = [m + random.uniform(-0.06, 0.06) for m in weights]
            json.dump(model, f)




def run():
    folder = "D:\\CaptureTraining\\dnf_test"

    pathlist = Path(folder).rglob('*.nam')
    for path in pathlist:
        oldname = str(path)
        with open(oldname, "r") as f:
            z = json.load(f)
            hash = z['weights']
            # z['weights'] = []
            # print("{} to {}".format(min(hash), max(hash)))
            print(len(hash))

            # print()


if __name__ == '__main__':
    randnam()
    # run()
