from services.family_service import add_child,add_spouse
from services.relationship_service import get_relationship

def process_commands(file_path):
    with open(file_path) as f:
        for line in f:
            parts = line.strip().split()

            if not parts:
                continue

            if parts[0] == "ADD_CHILD":
                print(add_child(parts[1], parts[2], parts[3]))
            elif parts[0] == "ADD_SPOUSE":
                print(add_spouse(parts[1],parts[2],parts[3]))            
            elif parts[0] == "GET_RELATIONSHIP":
                print(get_relationship(parts[1], parts[2]))
