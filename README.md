#artel-demo
Research demonstrator: minimal architecture prototype
git clone https://github.com/<username>/artel-demo.git
cd artel-demo
echo "<class Block:
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
    print(l)>" > artel_mini.py
git add artel_mini.py
git commit -m "Add minimal architectural prototype"
git push
