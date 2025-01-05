def radix_sort(bms_data):
    max_priority = max(building["priority"] for building in bms_data)
    exp = 1  
    while max_priority // exp > 0:
        bms_data = counting_sort_by_digit(bms_data, exp)
        exp *= 10  
    return bms_data

def counting_sort_by_digit(bms_data, exp):
    output = [None] * len(bms_data)
    count = [0] * 10  
    for building in bms_data:
        index = building["priority"] // exp % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(bms_data) - 1, -1, -1):
        building = bms_data[i]
        index = building["priority"] // exp % 10
        output[count[index] - 1] = building
        count[index] -= 1

    return output
bms_data = [
    {"name": "Building A", "priority": 3, "location": "New York", "status": "Active"},
    {"name": "Building B", "priority": 1, "location": "Los Angeles", "status": "Inactive"},
    {"name": "Building C", "priority": 5, "location": "Chicago", "status": "Active"},
    {"name": "Building D", "priority": 2, "location": "San Francisco", "status": "Inactive"}
]
sorted_bms_data = radix_sort(bms_data)
for building in sorted_bms_data:
    print(building)
