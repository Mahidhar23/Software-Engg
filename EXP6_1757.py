def cocomo_basic(kloc, project_type):
    cocomo_params = {
        "organic": (2.4, 1.05, 2.5, 0.38),
        "semi-detached": (3.0, 1.12, 2.5, 0.35),
        "embedded": (3.6, 1.20, 2.5, 0.32)
    }

    if project_type.lower() not in cocomo_params:
        return "Invalid project type! Choose from: organic, semi-detached, embedded."


    a, b, c, d = cocomo_params[project_type.lower()]


    effort = a * (kloc ** b)
    time = c * (effort ** d)

    avg_team_size = effort / time

    return {
        "Effort (Person-Months)": round(effort, 2),
        "Time (Months)": round(time, 2),
        "Team Size (Avg Developers)": round(avg_team_size, 2)
    }

# Example
kloc = 10
project_type = "organic"

result = cocomo_basic(kloc, project_type)
print(result)