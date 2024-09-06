mapping = {}
with open("data/Region-Country_Mapping.csv") as mapping_file:
    for line in mapping_file:
        region, country, *_ = line.strip().split(",")
        mapping[region] = country

with open("data/AIV_HA.fasta") as in_file, open("data/tip_to_country.csv", "w") as outfile:
    outfile.write("name,country\n")
    for line in in_file:
        if not line.startswith(">"):
            continue
        tip = line.strip()[1:]
        region = tip.split("/")[2]
        country = mapping[region]
        outfile.write(f"{tip},{country}\n")

        