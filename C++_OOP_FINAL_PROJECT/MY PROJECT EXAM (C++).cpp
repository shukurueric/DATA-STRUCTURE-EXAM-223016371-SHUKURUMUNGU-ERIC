#include <iostream>
#include <cstring>
using namespace std;

struct MenuItem {
    char name[30];
    float price;
};

MenuItem menu[20] = {
    {"Burger", 5.5},
    {"Pizza", 8.0},
    {"Salad", 4.5},
    {"Soda", 1.5},
    {"Fries", 2.0}
};

class OrderBase {
protected:
    MenuItem** items;
    int nItems;

public:
    OrderBase(MenuItem** items_, int n) {
        nItems = n;
        items = new MenuItem*[n];
        for (int i = 0; i < n; ++i) {
            items[i] = items_[i];
        }
    }

    virtual float totalCost() = 0; 

    virtual ~OrderBase() {
        delete[] items;
    }
};

class TakeOutOrder : public OrderBase {
public:
    TakeOutOrder(MenuItem** items_, int n) : OrderBase(items_, n) {}

    float totalCost() {
        float sum = 0;
        for (int i = 0; i < nItems; ++i)
            sum += items[i]->price;
        return sum + 1.0f; 
    }
};

class DineInOrder : public OrderBase {
public:
    DineInOrder(MenuItem** items_, int n) : OrderBase(items_, n) {}

    float totalCost() {
        float sum = 0;
        for (int i = 0; i < nItems; ++i)
            sum += items[i]->price;
        return sum + 2.0f; 
    }
};

class OrderManager {
private:
    OrderBase** orders;
    int nOrders;

public:
    OrderManager() {
        orders = NULL;
        nOrders = 0;
    }

    void addOrder(OrderBase* order) {
        OrderBase** newOrders = new OrderBase*[nOrders + 1];
        for (int i = 0; i < nOrders; ++i)
            newOrders[i] = orders[i];
        newOrders[nOrders] = order;
        delete[] orders;
        orders = newOrders;
        ++nOrders;
    }

    void removeOrder(int index) {
        if (index < 0 || index >= nOrders) return;
        delete orders[index];
        OrderBase** newOrders = new OrderBase*[nOrders - 1];
        for (int i = 0, j = 0; i < nOrders; ++i) {
            if (i != index)
                newOrders[j++] = orders[i];
        }
        delete[] orders;
        orders = newOrders;
        --nOrders;
    }

    void printOrders() {
        for (int i = 0; i < nOrders; ++i) {
            cout << "Order #" << i << " Total: $" << orders[i]->totalCost() << endl;
        }
    }

    ~OrderManager() {
        for (int i = 0; i < nOrders; ++i)
            delete orders[i];
        delete[] orders;
    }
};

int main() {
    OrderManager manager;

    MenuItem* items1[] = {&menu[0], &menu[1]}; 
    manager.addOrder(new TakeOutOrder(items1, 2));

    MenuItem* items2[] = {&menu[2], &menu[3], &menu[4]}; 
    manager.addOrder(new DineInOrder(items2, 3));

    manager.printOrders();

    manager.removeOrder(0);
    cout << "\nAfter removing first order:\n";
    manager.printOrders();

    return 0;
}
