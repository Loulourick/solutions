def month_calendar(start_weekday, days):
    a = []
    b = []
    for _ in range(start_weekday):
        b.append("  ")
    for day in range(1, days + 1):
        b.append(f"{day:2}")
        if len(b) == 7:
            a.append(" ".join(b))
            b = []
    if b:
        a.append(" ".join(b))
    return "\n".join(a)

print((month_calendar(6, 31)))