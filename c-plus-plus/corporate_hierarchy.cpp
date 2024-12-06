#include <iostream>
#include <vector>

class Human {
    public:
        std::string name;
        std::string surname;
        int age;

        Human(std::string n, std::string s, int a) {
            name = n;
            surname = s;
            age = a;
        }
};


class Employee : public Human {
    public:
        int salary;

        Employee() : Human("", "", 0), salary(0) {} 
        Employee(int a, std::string n, std::string s, int sal) : Human(n, s, a), salary(sal) {}
};


class Manager : public Employee {
    public:
        std::vector<Employee> employees;
        int count;

        Manager(int a, std::string n, std::string s, int sal) : Employee(a, n, s, sal), count(0) {}

        void hireEmployee(const Employee& e) {
            employees.push_back(e);
            ++count;
        }

        void fireEmployee(const std::string& employeeName) {
            for (auto it = employees.begin(); it != employees.end(); ++it) {
                if (it->name == employeeName) {
                    employees.erase(it);
                    --count;
                    return; 
                }
            }
            std::cout << "Not Found!\n";
        }
};



class Director : public Employee {
    public:
        Manager* m;

        Director(int a, std::string n, std::string s, int sal) : Employee(a, n, s, sal), m(nullptr) {}

        void hireManager(Manager* newManager) {
            if (m == nullptr) {
                m = newManager;
                std::cout << "Manager " << newManager->name << " hired.\n";
            } else {
                std::cout << "We already have a manager.\n";
            }
        }

        void fireManager() {
            if (m != nullptr) {
                std::cout << "Manager " << m->name << " fired.\n";
                m = nullptr;
            } else {
                std::cout << "We don't have a manager.\n";
            }
        }
};


int main() {

    Employee emp1(30, "John", "Doe", 5000);
    Employee emp2(25, "Jane", "Smith", 4800);
    Employee emp3(28, "Alice", "Johnson", 5200);

    Manager mgr(40, "Michael", "Scott", 10000);

    mgr.hireEmployee(emp1);
    mgr.hireEmployee(emp2);

    std::cout << "Employees: " << mgr.count << "\n";

    mgr.fireEmployee("Jane");
    
    std::cout << "Employees: " << mgr.count << "\n";

    mgr.fireEmployee("Bob");

    Director dir(50, "Angela", "Martin", 20000);

    dir.hireManager(&mgr);

    Manager mgr2(35, "Thomas", "Schrute", 9500);
    
    dir.hireManager(&mgr2);

    dir.fireManager();

    dir.hireManager(&mgr2);

    return 0;
}