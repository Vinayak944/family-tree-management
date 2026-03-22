from services.family_service import build_family
from utils.file_processor import process_commands
import sys

if __name__ == "__main__":
    build_family()
    process_commands(sys.argv[1])