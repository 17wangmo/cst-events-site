import json
from datetime import date
from pathlib import Path


def load_events(path):
    data = json.loads(Path(path).read_text())
    return data["events"]


def upcoming(events, today):
    future = [e for e in events if e["date"] >= today]
    return sorted(future, key=lambda e: e["date"])


def render(events):
    items = "\n".join(
        f'''
        <div class="event-card">
            <div class="event-date">{e["date"]}</div>
            <div class="event-info">
                <h2>{e["title"]}</h2>
                <p>📍 {e["venue"]}</p>
            </div>
        </div>
        '''
        for e in events
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>ACM Club at CST - Events</title>

    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #f0f4ff, #e8f5f0);
            color: #1f2937;
            min-height: 100vh;
        }}

        header {{
            background: linear-gradient(135deg, #172554, #1e40af);
            color: white;
            padding: 50px 20px;
            text-align: center;
        }}

        header h1 {{
            font-size: 42px;
            margin-bottom: 12px;
        }}

        header p {{
            font-size: 18px;
            opacity: 0.9;
        }}

        .container {{
            width: 90%;
            max-width: 900px;
            margin: 40px auto;
        }}

        .section-title {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .section-title h2 {{
            font-size: 30px;
            color: #172554;
        }}

        .section-title p {{
            margin-top: 8px;
            color: #6b7280;
        }}

        .events {{
            display: grid;
            gap: 20px;
        }}

        .event-card {{
            background: white;
            border-radius: 16px;
            padding: 22px;
            display: flex;
            align-items: center;
            gap: 25px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            border-left: 6px solid #2563eb;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .event-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.13);
        }}

        .event-date {{
            background: #eff6ff;
            color: #1d4ed8;
            padding: 12px 16px;
            border-radius: 10px;
            font-weight: bold;
            min-width: 125px;
            text-align: center;
        }}

        .event-info h2 {{
            color: #111827;
            margin-bottom: 8px;
            font-size: 22px;
        }}

        .event-info p {{
            color: #6b7280;
            font-size: 16px;
        }}

        footer {{
            text-align: center;
            padding: 30px;
            color: #6b7280;
            font-size: 14px;
        }}

        @media (max-width: 600px) {{
            header h1 {{
                font-size: 30px;
            }}

            .event-card {{
                flex-direction: column;
                align-items: flex-start;
                gap: 15px;
            }}

            .event-date {{
                width: 100%;
            }}
        }}
    </style>
</head>

<body>

<header>
    <h1>ACM Club at CST</h1>
    <p>Events & Activities</p>
</header>

<main class="container">

    <div class="section-title">
        <h2>Upcoming Events</h2>
        <p>Stay updated with the latest ACM Club activities at CST.</p>
    </div>

    <div class="events">
        {items}
    </div>

</main>

<footer>
    ACM Club at CST &bull; College of Science and Technology
</footer>

</body>
</html>
'''


def main():
    events = upcoming(
        load_events("events.json"),
        date.today().isoformat()
    )

    Path("dist").mkdir(exist_ok=True)

    Path("dist/index.html").write_text(
        render(events),
        encoding="utf-8"
    )

    print(f"wrote dist/index.html with {len(events)} events")


if __name__ == "__main__":
    main()