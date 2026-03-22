# Family Tree Management System

This project is a solution to the **Glynac Data Engineer Coding Challenge**.  
It models a royal family tree and supports operations to add children and fetch relationships.

---

## Features

- Add a child to a family through the mother
- Add a spouse to a family through a person
- Retrieve relationships (currently supports: Siblings,Maternal-Aunt,Maternal-Uncle,Paternal-Aunt,Paternal-Uncle)
- Command-based input from file
- Clean modular design using OOP principles

---

## Project Structure
Glynac_Data_Engineering_Coding_Challenge/
│
├── models/
│ └── person.py
│
├── services/
│ ├── family_service.py
│ └── relationship_service.py
│
├── utils/
│ └── file_processor.py
│
├── main.py
└── input.txt


---

## Design Approach

### 1. Data Modeling
- Each person is represented using a `Person` class
- Relationships are maintained using:
  - `mother`
  - `father`
  - `children`
  - `spouse`

### 2. Storage
- A global dictionary (`family`) is used for **O(1) lookup**

### 3. Separation of Concerns
- `models/` → Data structure
- `services/` → Business logic
- `utils/` → Input processing
- `main.py` → Entry point

---

##  How to Run

### Step 1: Navigate to project folder
cd Glynac_Data_Engineering_Coding_Challenge

### Step 2: Run the program
python main.py input.txt


---

##  Input Format

Commands are read from a text file:
ADD_CHILD Flora Jasmine Female
GET_RELATIONSHIP Ginny Siblings
ADD_SPOUSE Bill Ely Female



---

## 📤 Output Format
PERSON_NOT_FOUND
Bill Charlie Percy Ronald
SPOUSE_ADDITION_SUCCEEDED

---

## ⚠️ Assumptions

- Children can only be added via the **mother**
- Names are unique identifiers
- Gender values are either `"Male"` or `"Female"`
- If a person is not found → `PERSON_NOT_FOUND`
- If no relationship exists → `NONE`

---

## 🧹 Improvements (Future Work)

- Support more relationships
- Can Add Spouse to a person and add it to family
- Convert to class-based service architecture
---

## 🧑‍💻 Author

Vinayak Ganesh

---

## ✅ Summary

This solution focuses on:
- Clean OOP design
- Readability and maintainability
- Efficient data structures
- Extensible architecture