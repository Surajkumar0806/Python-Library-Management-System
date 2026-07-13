# 📚 Library Management System (Python OOP)

A terminal-based **Library Management System** developed in Python to practice **Object-Oriented Programming (OOP)**, clean project architecture, JSON-based data persistence, and modular software design.

This project was built from the ground up as a learning project with a strong focus on writing maintainable, reusable, and well-structured code rather than simply implementing features.

---

## 🚀 Features

### 📖 Book Management

* Add new books
* Search books by Book ID
* Display all books
* Borrow books
* Return books
* Automatic update of available copies
* Prevent borrowing when no copies are available

### 👤 Member Management

* Add new members
* Search members by Member ID
* Display all members
* Borrow books for members
* Return books from members
* Prevent duplicate borrowing
* Borrow limit validation

### 💾 Data Persistence

* Save books to JSON
* Save members to JSON
* Automatically load saved data when the application starts

### ✅ Input Validation

* Prevent empty text input
* Validate positive integer inputs
* Handle invalid user input gracefully
* Prevent application crashes caused by invalid data

---

# 🏗️ Project Structure

```text
Library-Management-System/
│
├── book.py
├── library.py
├── member.py
├── member_library.py
├── menu.py
├── member_menu.py
├── validation.py
├── storage.py
├── main.py
├── books.json
├── members.json
└── README.md
```

The project follows a modular structure where each file has a single responsibility.

---

# 🧠 OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Instance Methods
* Class Methods (`@classmethod`)
* Dunder Methods (`__str__`)
* Object Composition
* Encapsulation
* Separation of Concerns
* Modular Programming

---

# 📂 Technologies Used

* Python 3
* JSON
* Object-Oriented Programming
* File Handling
* Exception Handling

---

# ▶️ How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd Library-Management-System
```

3. Run the application.

```bash
python main.py
```

---

# 📸 Screenshots

Include screenshots demonstrating:

* Main Menu
* Add Book
* Display Books
* Add Member
* Display Members
* Borrow Book
* Return Book

---

# 🎯 Learning Outcomes

This project was developed to strengthen practical Python programming skills while applying Object-Oriented Programming concepts to a real-world application.

Key learning outcomes include:

* Designing multiple collaborating classes
* Organizing a project into reusable modules
* Applying clean architecture principles
* Implementing JSON serialization and persistence
* Building reusable validation functions
* Managing object relationships across multiple classes
* Refactoring code for maintainability

---

# 🔮 Future Improvements

Potential enhancements include:

* Automatic Book ID generation
* Due dates and renewals
* Borrow history
* Fine calculation
* SQL database integration
* Django REST backend
* React frontend
* Authentication and user roles

---

# 👨‍💻 Author

Developed by **Surajkumar Kottal** as part of a hands-on Python and Object-Oriented Programming learning journey.
