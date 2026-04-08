import matplotlib.pyplot as plt

class Block:
    def __init__(self, name):
        self.name = name
        self.buffer = []

    def receive(self, tasks):
        self.buffer.extend(tasks)

    def size(self):
        return len(self.buffer)

# Инициализация модулей
inputs = Block("Inputs")
ai = Block("AI")
curator = Block("Curator")
core = Block("Core")
platform = Block("Platform")
outputs = Block("Outputs")
blocks = [inputs, ai, curator, core, platform, outputs]

def show_graph(step_label="Step"):
    names = [b.name for b in blocks]
    sizes = [b.size() for b in blocks]
    plt.bar(names, sizes, color='skyblue')
    plt.ylim(0, max(10, max(sizes)+2))
    plt.title(f"Buffer sizes — {step_label}")
    plt.ylabel("Number of tasks")
    plt.show(block=False)
    plt.pause(0.8)
    plt.clf()

def equilibrium_cycle(tasks):
    # Step 1: Inputs
    inputs.receive(tasks)
    show_graph("Incoming tasks")
    
    # Step 2: AI & Curator перераспределяют
    half = len(inputs.buffer)//2
    ai.receive(inputs.buffer[:half])
    curator.receive(inputs.buffer[half:])
    inputs.buffer.clear()
    show_graph("After AI & Curator redistribute")
    
    # Step 3: Core получает поток
    core.receive(ai.buffer + curator.buffer)
    ai.buffer.clear()
    curator.buffer.clear()
    show_graph("After Core receives tasks")
    
    # Step 4: Platform & Outputs распределение
    half_core = len(core.buffer)//2
    platform.receive(core.buffer[:half_core])
    outputs.receive(core.buffer[half_core:])
    core.buffer.clear()
    show_graph("Final distribution to Platform & Outputs")

# --- Меню сценариев ---
def run_scenario():
    while True:
        print("\nВыберите сценарий тряски:")
        print("1 — Базовый сценарий (8 задач)")
        print("2 — Групповой всплеск (3 группы по 5 задач)")
        print("3 — Постепенный поток с пиками")
        print("0 — Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "0":
            print("Выход из симуляции.")
            break
        elif choice == "1":
            tasks = [f"Task{i}" for i in range(1, 9)]
            equilibrium_cycle(tasks)
        elif choice == "2":
            tasks = [f"Task{i}" for i in range(1, 16)]
            equilibrium_cycle(tasks)
        elif choice == "3":
            print("Введите количество задач по очереди, 0 чтобы закончить:")
            while True:
                try:
                    n = int(input("Количество задач: "))
                    if n == 0:
                        break
                    tasks = [f"Task{i}" for i in range(1, n+1)]
                    equilibrium_cycle(tasks)
                except ValueError:
                    print("Введите число.")
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск меню
run_scenario()
plt.close()
