#include <iostream>
using namespace std;

int RDVALUE_ = 1;
#define RAND RD()

int RD(void) {
    int A;
    RDVALUE_ = (RDVALUE_ + (int)(&A)) * 1103515245 + 12345;
    return RDVALUE_ / 31;
}

struct PQ_el {
    void* data;
    int priority;
};


struct Priority_Queue {
    PQ_el* elements;
    int capacity;
    int size;
    int (*pr_func)(void*);
};


Priority_Queue* init(int capacity, int (*priorityFunction)(void*)) {
    Priority_Queue* queue = (Priority_Queue*)malloc(sizeof(Priority_Queue));
    queue->elements = (PQ_el*)malloc(capacity * sizeof(PQ_el));
    queue->capacity = capacity;
    queue->size = 0;
    queue->pr_func = priorityFunction;
    return queue;
}


void del(Priority_Queue* queue) {
    free(queue->elements);
    free(queue);
}


void push(Priority_Queue* queue, void* data) {
    if (queue->size == queue->capacity) {
        printf("Queue is full\n");
        return;
    }

    PQ_el element = { data, queue->pr_func(data) };
    int i;

    for (i = queue->size - 1; i >= 0; i--) {
        if (element.priority > queue->elements[i].priority) {
            queue->elements[i + 1] = queue->elements[i];
        }

        else break;
    }
    queue->elements[i + 1] = element;
    queue->size++;
}


void* pop(Priority_Queue* queue) {
    if (queue->size == 0) {
        printf("Queue is empty\n");
        return NULL;
    }

    void* data = queue->elements[0].data;
    int i;

    for (i = 1; i < queue->size; i++) queue->elements[i - 1] = queue->elements[i];

    queue->size--;
    return data;
}


int priority1(void* data) {
    int value = *((int*)data);
    return (value % 2 == 0) ? 1 : 0;
}


int priority2(void *data) {
    int value = *((int*) data);
    return -value;
}

int priority3(void* data) {
    int value = *((int*)data);

    if (value % 2 != 0) return value;
    else return value + 1e9;
}


int main() {

    int N; cin >> N;
    Priority_Queue* queue = init(N, &priority3);

    for (int i = 0; i < N; i++) {
        int* a = new int; *a = abs(RAND) / 100;
        push(queue, a);
    }

    for (int i = 0; i < N; i++) {
        cout << *(int*)pop(queue) << "\n";
    }

    del(queue);
}
