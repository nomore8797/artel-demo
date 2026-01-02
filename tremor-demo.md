# Mini Demo: Equilibrium Handling Tremors

**Цель:** показать наглядно, как модули платформы реагируют на резкий поток задач и как работает Equilibrium.

```python
class Block:
    def __init__(self, name):
        self.name = name
        self.buffer = []

    def receive(self, tasks):
        self.buffer.extend(tasks)

    def process(self):
        if not self.buffer:
            return f"{self.name}: idle"
        task = self.buffer.pop(0)
        return f"{self.name} processed {task}"

# Инициализация модулей
inputs = Block("Inputs")
ai = Block("AI")
curator = Block("Curator")
core = Block("Core")
platform = Block("Platform")
outputs = Block("Outputs")

# Equilibrium: перераспределение задач
def equilibrium_cycle(tasks):
    inputs.receive(tasks)
    ai.receive(inputs.buffer[:len(inputs.buffer)//2])
    curator.receive(inputs.buffer[len(inputs.buffer)//2:])
    inputs.buffer.clear()
    core.receive(ai.buffer + curator.buffer)
    ai.buffer.clear()
    curator.buffer.clear()
    platform.receive(core.buffer[:len(core.buffer)//2])
    outputs.receive(core.buffer[len(core.buffer)//2:])
    core.buffer.clear()
    for b in [inputs, ai, curator, core, platform, outputs]:
        print(b.process())

# Симуляция тряски: резкий поток из 6 задач
tasks = [f"Task{i}" for i in range(1,7)]
equilibrium_cycle(tasks)
```

**Что демонстрирует код:**  
- Inputs получает все задачи → перегрузка.  
- AI и Curator перераспределяют нагрузку.  
- Core получает оптимизированный поток.  
- Platform и Outputs получают задачи постепенно.  
- На выходе система остаётся стабильной — тряска сглажена.
