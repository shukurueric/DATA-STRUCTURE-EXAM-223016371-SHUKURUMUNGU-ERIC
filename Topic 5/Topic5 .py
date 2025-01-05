import heapq

class BuildingManagementHeap:
    def __init__(self):
        self.heap = []  

    def add_data(self, priority, data):
        heapq.heappush(self.heap, (priority, data))

    def get_top_priority(self):
        if self.heap:
            return self.heap[0]
        return None
    def process_top_priority(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    def display_heap(self):
        return sorted(self.heap)
bms_heap = BuildingManagementHeap()
bms_heap.add_data(2, "Adjust HVAC temperature")
bms_heap.add_data(1, "Fire alarm triggered")
bms_heap.add_data(3, "Schedule lighting maintenance")
bms_heap.add_data(4, "Elevator maintenance overdue")
print("Heap Data:", bms_heap.display_heap())
print("Top Priority Data:", bms_heap.get_top_priority())
print("Processing Top Priority:", bms_heap.process_top_priority())
print("Updated Heap Data:", bms_heap.display_heap())
