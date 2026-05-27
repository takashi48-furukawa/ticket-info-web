import json
from jinja2 import Environment, FileSystemLoader

def generate_page():
    # 1. JSON を読み込む
    with open("data/tickets.json", "r", encoding="utf-8") as f:
        events = json.load(f)

    # 2. templates フォルダからテンプレートを読み込む
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")

    # 3. HTML を生成
    html = template.render(events=events)

    # 4. output/index.html に書き出す
    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_page()

