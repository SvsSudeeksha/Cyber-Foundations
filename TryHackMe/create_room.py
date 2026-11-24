from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def create_room_template():
  print("--- Cyber-Foundations Room Note Generator ---")
  room_name = input("Enter room name (e.g., 3-Networking-Basics): ").strip()
  if not room_name:
    print("[!] Room name cannot be empty.")
    return

  # Preserve exact casing, replace spaces with hyphens, and avoid double .md
  clean_name = room_name.replace(" ", "-")
  if not clean_name.endswith(".md"):
    clean_name = f"{clean_name}.md"
  filename = clean_name

  display_title = Path(filename).stem.replace("-", " ").title()

  # Choose category folder matching your structure
  print("\nSelect Category Folder:")
  print("1. 01-Fundamentals")
  print("2. 02-Web-Security")
  print("3. 03-Linux-PrivEsc")
  print("4. 04-Defensive-Ops")
  print("5. 05-Network-Analysis")
  print("6. 06-CTF-Walkthroughs")

  choice = input("Enter choice (1-6): ").strip()
  folder_map = {
      "1": "01-Fundamentals",
      "2": "02-Web-Security",
      "3": "03-Linux-PrivEsc",
      "4": "04-Defensive-Ops",
      "5": "05-Network-Analysis",
      "6": "06-CTF-Walkthroughs",
  }

  sub_folder = folder_map.get(choice, "")
  target_dir = BASE_DIR / sub_folder if sub_folder else BASE_DIR
  filepath = target_dir / filename

  today_str = date.today().strftime("%Y-%m-%d")
  category_label = sub_folder if sub_folder else BASE_DIR.name

  # Pre-filled Markdown Template Content
  template_content = f"""# {display_title} - TryHackMe Write-Up

**Date Completed:** {today_str}  
**Category:** {category_label}  
**Room Link:** [Insert TryHackMe URL]

---

## 1. Key Concepts Learned
- **[Concept 1]:** Brief explanation in your own words.
- **[Concept 2]:** Explain the underlying mechanism or syntax.

---

## 2. Tools & Syntax Reference
| Tool / Command | Flag / Payload | Purpose / Explanation |
| :--- | :--- | :--- |
| `nmap` | `-sV -sC` | Scans services and runs default scripts. |

---

## 3. Practical Steps & Execution
1. **Reconnaissance:**
  - Ran port scans / directory enumeration.
2. **Exploitation / Task Completion:**
  - Steps taken to solve the room objectives.

---

## 4. Key Takeaways & Defense
- How to patch, mitigate, or defend against this issue.
"""

  if filepath.exists():
    print(f"\n[!] File already exists at: {filepath}")
    return

  target_dir.mkdir(parents=True, exist_ok=True)
  filepath.write_text(template_content, encoding="utf-8")

  print(f"\n[+] Successfully created template at: {filepath}")


if __name__ == "__main__":
  create_room_template()