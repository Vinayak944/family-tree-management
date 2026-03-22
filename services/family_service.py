from models.person import Person

family ={}

def build_family():
    king = Person("King Arthur", "Male")
    queen = Person("Queen Margaret", "Female")
    
    king.spouse = queen
    queen.spouse = king

    family[king.name] = king
    family[queen.name] = queen

    children_data = [
        ("Bill","Male"),
        ("Charlie","Male"),
        ("Percy", "Male"),
        ("Ronald","Male"),
        ("Ginny","Female")
    ]
    for name,gender in children_data:
        child = Person(name,gender)

        child.mother = queen
        child.father = king

        queen.children.append(child)
        king.children.append(child)
        
        family[name] = child
    
def find_person(name):
    return family.get(name)

def add_child(mother_name,child_name,gender):
    mother = find_person(mother_name)

    if not mother:
        return "PERSON_NOT_FOUND"
    
    if mother.gender != "Female":
        return "CHILD_ADDITION_FAILED"
    
    child = Person(child_name,gender)

    child.mother = mother
    child.father = mother.spouse
    
    mother.children.append(child)

    if mother.spouse:
        mother.spouse.children.append(child)

    family[child.name] = child

    return "CHILD_ADDITION_SUCCEEDED"

def add_spouse(person_name,spouse_name,gender):
    person = find_person(person_name)

    if not person:
        return "PERSON_NOT_FOUND"
    if person.spouse:
        return "SPOUSE_ALREADY_EXISTS"
    
    spouse = Person(spouse_name,gender)

    person.spouse = spouse
    spouse.spouse = person

    family[spouse_name] = spouse

    return "SPOUSE_ADDITION_SUCCEEDED"
