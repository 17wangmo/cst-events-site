from build_site import upcoming, render


EVENTS = [
    {
        "title": "Hackathon",
        "date": "2027-03-01",
        "venue": "Lab 4"
    },
    {
        "title": "Orientation",
        "date": "2027-02-14",
        "venue": "Auditorium"
    },
    {
        "title": "Old AGM",
        "date": "2025-11-02",
        "venue": "Room 12"
    },
]


def test_past_events_are_dropped():
    result = upcoming(EVENTS, "2026-01-01")
    assert len(result) == 2


def test_events_come_out_in_date_order():
    result = upcoming(EVENTS, "2026-01-01")
    assert [e["title"] for e in result] == [
        "Orientation",
        "Hackathon"
    ]


def test_an_event_today_still_counts_as_upcoming():
    result = upcoming(EVENTS, "2027-03-01")
    assert [e["title"] for e in result] == ["Hackathon"]


def test_render_mentions_every_event_given_to_it():
    html = render(EVENTS)

    for event in EVENTS:
        assert event["title"] in html