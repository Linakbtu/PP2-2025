import json

with open("sample-data.json") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 60)
print("DN".ljust(50) + "Speed".ljust(10) + "MTU")
print("-" * 60)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    speed = attr.get("speed", "inherit")
    mtu = attr.get("mtu", "")

    print(dn.ljust(50) + speed.ljust(10) + mtu)
