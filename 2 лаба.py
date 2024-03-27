class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Queue: " + str(self.items)

    def __repr__(self):
        return f"Queue({self.items})"


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Stack: " + str(self.items)

    def __repr__(self):
        return f"Stack({self.items})"


class ServoMotor:
    def __init__(self, angle, speed):
        self.angle = angle
        self.speed = speed

    def __str__(self):
        return f"Servo Motor (Angle: {self.angle}, Speed: {self.speed})"

    def __repr__(self):
        return f"ServoMotor(angle={self.angle}, speed={self.speed})"


class SynchronousServoMotor(ServoMotor):
    def __init__(self, angle, speed, linear_speed):
        super().__init__(angle, speed)
        self.linear_speed = linear_speed

    def __str__(self):
        return f"Synchronous Servo Motor (Angle: {self.angle}, Speed: {self.speed}, Linear Speed: {self.linear_speed})"

    def __repr__(self):
        return f"SynchronousServoMotor(angle={self.angle}, speed={self.speed}, linear_speed={self.linear_speed})"


class ManipulatorJoint:
    def __init__(self):
        self.position = 0

    def __str__(self):
        return f"Joint Position: {self.position}"

    def __repr__(self):
        return f"ManipulatorJoint(position={self.position})"


class SixAxisManipulator:
    def __init__(self):
        self.joints = [ManipulatorJoint() for _ in range(6)]

    def move_joint(self, joint_index, position):
        if 0 <= joint_index < len(self.joints):
            self.joints[joint_index].position += position

    def __str__(self):
        return "Six-Axis Manipulator with joints at positions: " + \
               ", ".join(str(joint.position) for joint in self.joints)

    def __repr__(self):
        return f"SixAxisManipulator(joints={self.joints})"


# Создание и использование структур данных

# Создаем очередь
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue)

# Создаем стек
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)

# Создаем сервоприводы
servo = ServoMotor(1500, 10)
print(servo)

sync_servo = SynchronousServoMotor(1500, 10, 230)
print(sync_servo)

# Создаем манипулятор и двигаем его суставы
manipulator = SixAxisManipulator()
manipulator.move_joint(2, 30)  # Двигаем третий сустав на 30 градусов
print(manipulator)




