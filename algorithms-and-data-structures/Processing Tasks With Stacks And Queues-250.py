## 3. Processing Applications ##

import pandas
applications = pandas.read_csv("applications.csv")
from datetime import datetime

def process_application(application):
    birth_date = datetime.strptime(application["birthdate"], "%Y-%m-%d %H:%M:%S")
    delta = (birth_date - datetime.now()).total_seconds()
    delta /= (3600 * 24 * 365.25)
    if delta < 18:
        return False
    state = application["address"].split(" ")[-2]
    if state != "CA":
        return False
    return True

application_status = list(applications.apply(process_application, axis=1))

## 5. Stacks ##

import threading
import math
import time

def process_application(application):
    time.sleep(.001)
    birth_date = datetime.strptime(application["birthdate"], "%Y-%m-%d %H:%M:%S")
    delta = (birth_date - datetime.now()).total_seconds()
    delta /= (3600 * 24 * 365.25)
    if delta < 18:
        return False
    state = application["address"].split(" ")[-2]
    if state != "CA":
        return False
    return True
wait_times = []
stack = []
task_numbers = []

def add_tasks():
    for index, row in applications.iterrows():
        stack.insert(0,(index + 1, row))
        task_numbers.append(index + 1)
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            if task_number == task_numbers[-1]:
                wait_times.append(600)
            else:
                wait_times.append((24 - math.ceil(task_number / 300)) * 3600)
                
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / len(wait_times)
print(average_wait_time)

## 6. Implementing A Stack ##

class Stack():
    pass
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.insert(0, value)
    
    def pop(self):
        return self.items.pop(0)
    
    def count(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

## 7. Time Spent In Stacks ##

import matplotlib.pyplot as plt

stack = []

def add_tasks():
    for index, row in applications.iterrows():
        stack.insert(0,(index + 1, row))
        # Insert code here.
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            # Insert code here.

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / 2400
print(average_wait_time)
queue_times = []
wait_times = []
stack = []

def add_tasks():
    for index, row in applications.iterrows():
        stack.insert(0,(index + 1, row))
        queue_times.append(0)
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            wait_times.append(queue_times[task_number - 1] * 20 + 600)
            for i in range(len(queue_times)):
                queue_times[i] += 1

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / 2400
print(average_wait_time)

plt.hist(wait_times)

## 9. Waiting Time With Queues ##

import threading
import math
import time

def process_application(application):
    time.sleep(.001)
    birth_date = datetime.strptime(application["birthdate"], "%Y-%m-%d %H:%M:%S")
    delta = (birth_date - datetime.now()).total_seconds()
    delta /= (3600 * 24 * 365.25)
    if delta < 18:
        return False
    state = application["address"].split(" ")[-2]
    if state != "CA":
        return False
    return True
wait_times = []
queue = []

def add_tasks():
    for index, row in applications.iterrows():
        queue.append((index + 1, row))
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(queue) == 0:
            time.sleep(1)
        else:
            task_number, application = queue.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            wait_times.append((24 - math.ceil(task_number / 300)) * 3600)
                
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / 2400
print(average_wait_time)

## 10. Implementing a Queue ##

class Queue():
    pass
class Queue():
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop(0)
    
    def count(self):
        return len(self.items)

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()

## 11. Time Spent In Queues ##

queue = []

def add_tasks():
    for index, row in applications.iterrows():
        queue.append((index + 1, row))
        # Insert code here.
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(queue) == 0:
            time.sleep(1)
        else:
            task_number, application = queue.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            # Insert code here.
                
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / 2400
print(average_wait_time)
queue_times = []
wait_times = []
queue = []

def add_tasks():
    for index, row in applications.iterrows():
        queue.append((index + 1, row))
        queue_times.append(0)
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(queue) == 0:
            time.sleep(1)
        else:
            task_number, application = queue.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            wait_times.append(queue_times[task_number - 1] * 20 + 600)
            for i in range(len(queue_times)):
                queue_times[i] += 1

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / 2400
print(average_wait_time)

plt.hist(wait_times)

## 12. Profiling Stacks As Elements Are Added ##

queue_times = []
wait_times = [0] * 2400
stack = []

def add_tasks():
    for index, row in applications.iterrows():
        stack.insert(0,(index + 1, row))
        queue_times.append(0)
        time.sleep(.001)
        
def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            # Insert code here.
            for i in range(len(queue_times)):
                queue_times[i] += 1
                
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()
queue_times = []
wait_times = [0] * 2400
stack = []

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            task_index = task_number - 1
            wait_times[task_index] = (queue_times[task_index] * 20 + 600)
            for i in range(len(queue_times)):
                queue_times[i] += 1

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

plt.bar(range(2400), wait_times)

## 13. Profiling Queues As Elements Are Added ##

queue_times = []
wait_times = [0] * 2400
queue = []

def add_tasks():
    for index, row in applications.iterrows():
        queue.append((index + 1, row))
        queue_times.append(0)
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(queue) == 0:
            time.sleep(1)
        else:
            task_number, application = queue.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            # Insert code here.
            for i in range(len(queue_times)):
                queue_times[i] += 1

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()
queue_times = []
wait_times = [0] * 2400
queue = []

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(queue) == 0:
            time.sleep(1)
        else:
            task_number, application = queue.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            task_index = task_number - 1
            wait_times[task_index] = (queue_times[task_index] * 20 + 600)
            for i in range(len(queue_times)):
                queue_times[i] += 1

t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

plt.bar(range(2400), wait_times)