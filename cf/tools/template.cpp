#include <iostream>
#include <vector>

using namespace std;

class Person {
    public:
        int height;
        int weight;
        Person(int height, int weight) {
            this->height = height;
            this->weight = weight;
        }

};

bool student_cmp(Person* p1, Person* p2) {
    if (p1->height == p2->height) {
        return p1->weight < p2->weight;
    }
    return p1->height < p2->height;
}

int main() {
    vector<Person*> v;
    v.push_back(new Person(1, 2));
    v.push_back(new Person(3, 2));
    v.push_back(new Person(2, 3));
    v.push_back(new Person(2, 2));

    sort(v.begin(), v.end(), student_cmp);

    for (auto p: v) {
        cout << "Height: " << p->height << ", Weight: " << p->weight << "\n";
    }

    return 0;
}
