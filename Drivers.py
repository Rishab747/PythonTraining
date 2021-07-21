drivers = [
    {
        "name": "Holt",
        "status": "0",
        "distance": 9
    },
    {
        "name": "Charles",
        "status": "1",
        "distance": 4
    },
    {
        "name": "Rosa",
        "status": "0",
        "distance": 15
    },
    {
        "name": "Amy",
        "status": "1",
        "distance": 7
    },
    {
        "name": "Jake",
        "status": "1",
        "distance": 2
    },
    {
        "name": "Terry",
        "status": "0",
        "distance": 10
    }
]

customer = {
    "name": "Gina",
    "mobile_number": "99999 11111",
    "Email": "professor@example.com",
    "distance": 5
}

n = len(drivers)

for k in range(n):
    for j in range(0, n-k-1):
        if drivers[j]["distance"] > drivers[j+1]["distance"]:

            drivers[j], drivers[j+1] = drivers[j+1], drivers[j]


for i in range(len(drivers)):

    if drivers[i]["status"] == 0:
        continue
    if drivers[i]["distance"] > customer["distance"]:
        continue

    print("Driver Name", drivers[i]["name"])
    print("Cab Booked. Details Sent!", customer["mobile_number"])
    print("Cab Booked. Details Sent!", customer["Email"])
    break




