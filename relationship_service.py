from services.family_service import find_person


def get_siblings(name):
    person = find_person(name)

    if not person or not person.mother:
        return []
    
    return[
        child.name
        for child in person.mother.children
        if child.name != person.name
    ]

def get_siblings_by_gender(parent, gender):
    siblings = get_siblings(parent.name)
    
    return [
        s
        for s in siblings
        if find_person(s).gender == gender
    ]

def get_paternal_uncle(name):
    person = find_person(name)

    if not person or not person.father:
        return []
    
    return get_siblings_by_gender(person.father, "Male")

def get_paternal_aunt(name):
    person = find_person(name)

    if not person or not person.father:
        return []
    
    return get_siblings_by_gender(person.father, "Female")

def get_maternal_uncle(name):
    person = find_person(name)

    if not person or not person.mother:
        return []
    
    return get_siblings_by_gender(person.father, "Male")

def get_maternal_aunt(name):
    person = find_person(name)

    if not person or not person.mother:
        return []
    
    return get_siblings_by_gender(person.father, "Female")


def get_relationship(name,relation):
    person = find_person(name)

    if not person:
        return "PERSON_NOT_FOUND"
    
    if relation == "Siblings":
        result = get_siblings(name)
    elif relation == "Paternal-Uncle":
        result = get_paternal_uncle(name)
    elif relation == "Paternal-Aunt":
        result = get_paternal_aunt(name)
    elif relation == "Maternal-Uncle":
        result = get_maternal_uncle(name)
    elif relation == "Maternal-Aunt":
        result = get_maternal_aunt(name)
    else:
        result = []
    return " ".join(result) if result else "NONE"
