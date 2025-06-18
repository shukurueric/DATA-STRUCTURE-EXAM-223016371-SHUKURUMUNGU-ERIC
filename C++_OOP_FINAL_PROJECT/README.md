## 97.Restaurant Order Manager

### My project deal with ordering in restaurant as manager but in program of C++

Description: Build a restaurant order manager where static menu items are referenced by 
dynamic pointers; take-out and dine-in orders compute totals polymorphically.
Tasks:

• Define struct MenuItem { char name[30]; float price; }; and 
store a static MenuItem menu[20];.

• Create an abstract class OrderBase with virtual float totalCost() = 
0;, then derive TakeOutOrder : OrderBase and DineInOrder : 
OrderBase to demonstrate inheritance and polymorphism.

• Each OrderBase holds a dynamic MenuItem** items array and int 
nItems; use pointer arithmetic to sum prices plus packaging/service fees.

• Store OrderBase* in a dynamic OrderBase** orders; calling 
orders[i]->totalCost() dispatches correctly.

• Implement addOrder(OrderBase*) and removeOrder(int orderId) by
resizing OrderBase**.
### And also i have out put for my project that show that the project run well.
![image](https://github.com/user-attachments/assets/ff5b7c4b-13d7-44ce-aac0-dd95346cc838)


