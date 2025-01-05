import heapq

class BuildingManagementHeap:
    def __init__(self):
        self.heap = []  

    def add_task(self, priority, task):
        heapq.heappush(self.heap, (priority, task))

    def process_task(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None 

    def view_tasks(self):
        """View all tasks in the heap without removing them."""
        return sorted(self.heap)
bms_heap = BuildingManagementHeap()
bms_heap.add_task(3, "Inspect HVAC filters")
bms_heap.add_task(1, "Respond to fire alarm")
bms_heap.add_task(2, "Adjust lighting settings for meeting room")
bms_heap.add_task(5, "Schedule maintenance for elevators")
print("All tasks:", bms_heap.view_tasks())
print("Processing task:", bms_heap.process_task())
print("Processing task:", bms_heap.process_task())
print("Remaining tasks:", bms_heap.view_tasks())
