<код>=<class Block:
    def __init__(self, name):
        self.name = name

    def link(self, other):
        return f"{self.name} -> {other.name}"

# Core elements
core = Block("Core")
ai = Block("AI")
curator = Block("Curator")
platform = Block("Platform")

# System blocks
inputs = Block("Inputs")
outputs = Block("Outputs")

# Connections
links = [
    inputs.link(ai),
    ai.link(curator),
    curator.link(core),
    core.link(platform),
    platform.link(outputs),
]

for l in links:
    print(l)>
