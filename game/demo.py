# demo.py
import json

def load_story(path="story.json"):
    with open(path, "r") as f:
        return json.load(f)["nodes"]

def build_node_map(nodes):
    return {n["id"]: n for n in nodes}

def play(node_map, start_id="checkpoint_0"):
    current = node_map[start_id]
    history = []

    while True:
        print("\n" + current["text"] + "\n")
        if not current.get("choices"):
            # No choices = an ending
            print("=== End of story ===")
            break

        # list choices
        for i, choice in enumerate(current["choices"], 1):
            print(f"  {i}. {choice['text']}")
        # get user input
        sel = input("\nChoose an option: ").strip()
        if not sel.isdigit() or not (1 <= int(sel) <= len(current["choices"])):
            print("Invalid choice. Try again.")
            continue

        idx = int(sel) - 1
        history.append((current["id"], current["choices"][idx]["target"]))
        next_id = current["choices"][idx]["target"]
        current = node_map[next_id]

    # optional: print path taken
    print("\nYour path:")
    for src, tgt in history:
        print(f"  {src} → {tgt}")

if __name__ == "__main__":
    nodes = load_story()
    node_map = build_node_map(nodes)
    play(node_map)
