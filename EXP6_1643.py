def cocomo_basic(kloc, project_type):
    cocomo_params = {
        "organic": (3.2, 2.3, 2.5, 0.38),
        "semi-detached": (3.0, 1.2, 2.5, 0.35),
        "embedded": (3.8, 1.20, 2.5, 0.52)
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
kloc = 12
project_type = "organic"

result = cocomo_basic(kloc, project_type)
print(result)