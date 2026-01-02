# Tremor Visual Demo (Визуализация тряски)

**Цель:** показать, как каждый модуль реагирует на резкий поток задач и как Equilibrium сглаживает тряску.

```python
class Block:
    def __init__(self, name):
        self.name = name
        self.buffer = []

    def receive(self, tasks):
        self.buffer.extend(tasks)

    def status(self):
        return f"{self.name} buffer: {len(self.buffer)} tasks"

# Инициализация модулей
inputs = Block("Inputs")
ai = Block("AI")
curator = Block("Curator")
core = Block("Core")
platform = Block("Platform")
outputs = Block("Outputs")

def show_buffers():
    for b in [inputs, ai, curator, core, platform, outputs]:
        print(b.status())
    print("-" * 40)

def equilibrium_cycle(tasks):
    print("=== Incoming tasks ===")
    inputs.receive(tasks)
    show_buffers()
    
    half = len(inputs.buffer)//2
    ai.receive(inputs.buffer[:half])
    curator.receive(inputs.buffer[half:])
    inputs.buffer.clear()
    print("=== After AI & Curator redistribute ===")
    show_buffers()
    
    core.receive(ai.buffer + curator.buffer)
    ai.buffer.clear()
    curator.buffer.clear()
    print("=== After Core receives tasks ===")
    show_buffers()
    
    half_core = len(core.buffer)//2
    platform.receive(core.buffer[:half_core])
    outputs.receive(core.buffer[half_core:])
    core.buffer.clear()
    print("=== Final distribution to Platform & Outputs ===")
    show_buffers()

# Симуляция тряски: 8 входящих задач
tasks = [f"Task{i}" for i in range(1,9)]
equilibrium_cycle(tasks)
```

**Что видно:**  
- Перегрузка Inputs  
- Перераспределение AI & Curator  
- Сглаживание в Core  
- Финальное распределение Platform & Outputs
