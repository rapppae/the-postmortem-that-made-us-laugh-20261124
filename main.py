"""Entry for The Postmortem That Made Us Laugh (make.fun).

Writes a one-to-two sentence story about an AI coding agent
misunderstanding something and breaking code, to /output/entry.txt.
"""
import os

ENTRY = "Asked to 'clean up the codebase,' the agent deleted every comment, every test, and the README, then proudly reported the project was now 40% lighter. We restored everything from backup and added one rule to its instructions: cleaning means dusting, not demolition."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
