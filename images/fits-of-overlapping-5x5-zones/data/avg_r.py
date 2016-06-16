import json


coords = [[7, 13], [9, 15]]
argvs = [[638], [1012], [440], [803]]

sums = []
for argv in argvs:
    r = []
    for coord in coords:
        with open("coords_{0}_{1}_5x5_argv_{2}.json".format(*(coord + argv)), 'r') as f:
            data = json.load(f)
        r.append(sum(data["comp_est"][3:])/25.0)
    sums.append(r)

print(sums)
