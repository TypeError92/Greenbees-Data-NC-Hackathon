from models.level_models import fetch_level


def get_level(level_id):
    level_id, layout, start, finish, optimal_solution = fetch_level(level_id)
    level = {
        'level_id': level_id,
        'layout': layout,
        'start': start,
        'finish': finish,
        'optimal_solution': optimal_solution,
    }

    return level
