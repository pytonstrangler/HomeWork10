import json


def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


print(load_candidates())


def get_all():
    return load_candidates()


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_by_skill(skill_name):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            result.append(candidate)
    return result
