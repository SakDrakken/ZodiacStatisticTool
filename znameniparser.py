def load_data_to_dict(source: str):
    z = {}
    with open(source, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.replace(",", ".")
            item = line.split(";")
            item[2] = item[2].replace("\n", "")
            try:
                z[item[0]].append([float(item[1]), float(item[2])])
            except KeyError:
                z[item[0]] = []
                z[item[0]].append([float(item[1]), float(item[2])])
    return z


def add_up_values(source: str):
    z = {}
    with open(source, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.replace(",", ".")
            item = line.split(";")
            item[2] = item[2].replace("\n", "")
            try:
                z[item[0]][0] = z[item[0]][0] + float(item[1])
                z[item[0]][1] = z[item[0]][1] + float(item[2])
            except KeyError:
                z[item[0]] = [float(item[1]), float(item[2])]
    return z


def add_up_values_weighted(source: str):
    y = {}
    z = {}
    with open(source, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.replace(",", ".")
            item = line.split(";")
            item[2] = item[2].replace("\n", "")
            try:
                z[item[0]].append(float(item[1]))
                y[item[0]].append(float(item[2]))
            except KeyError:
                z[item[0]] = []
                y[item[0]] = []
                z[item[0]].append(float(item[1]))
                y[item[0]].append(float(item[2]))
    for key in z.keys():
        z[key] = round(sum(z[key]) / len(z[key]), 2)
    for key in y.keys():
        y[key] = round(sum(y[key]) / len(y[key]), 2)
    return z, y


def get_vajb_and_kkt_nonw(val_dicc: dict):
    vajb = {}
    kkt = {}
    for key in val_dicc.keys():
        try:
            vajb[key] += val_dicc[key][0]
        except KeyError:
            vajb[key] = val_dicc[key][0]
    for key in val_dicc.keys():
        try:
            kkt[key] += val_dicc[key][1]
        except KeyError:
            kkt[key] = val_dicc[key][1]
    return vajb, kkt


def get_vajb_and_kkt_w(z: dict, y: dict):
    vajb = {}
    kkt = {}
    for key in z.keys():
        try:
            vajb[key] += z[key]
        except KeyError:
            vajb[key] = z[key]
    for key in y.keys():
        try:
            kkt[key] += y[key]
        except KeyError:
            kkt[key] = y[key]
    return vajb, kkt


def round_up_values(val_dicc: dict):
    for keys in val_dicc.keys():
        val_dicc[keys][0] = round(val_dicc[keys][0], 2)
        val_dicc[keys][1] = round(val_dicc[keys][1], 2)
        print(keys, ":", val_dicc[keys])
    return val_dicc


if __name__ == '__main__':
    # dicc = load_data_to_dict("xd.txt")
    max_values = add_up_values("xd.txt")
    weight_val_z, weight_val_y = add_up_values_weighted("xd.txt")

    n_vajb, n_kkt = get_vajb_and_kkt_nonw(max_values)
    t_vajb, t_kkt = get_vajb_and_kkt_w(weight_val_z, weight_val_y)

    max_vajb = max(n_vajb, key=lambda key: n_vajb[key])
    max_kkt = max(n_kkt, key=lambda key: n_kkt[key])
    avg_vajb = max(t_vajb, key=lambda key: t_vajb[key])
    avg_kkt = max(t_kkt, key=lambda key: t_kkt[key])
    print("Z mého FB friendlistu:\nNejvíc lidí, se kterýma vajbuju jsou: ", max_vajb,
          "\nZnamení se kterým v průměru nejvíc vajbuju je: ", avg_vajb,
          "\nNejvíc lidí, co jsou kokoti, jsou: ", max_kkt,
          "\nZnamení, u kterého je největší koncentrace kokotů je: ", avg_kkt)
    # print(dicc)
