# 📚 Console Library Management System

A Python-based console application for managing library operations, including book management, member tracking, and librarian controls. This system provides an efficient way to handle library resources through a command-line interface.

## 🌟 Key Features

### Book Management

- 📖 Add and remove books with details (title, author, copies)
- 🔍 Track available copies
- 📊 Display book information and inventory
- 🔄 Update book status and availability

### User Management

- 👥 Dual user roles (Librarian and Member)
- 🆔 Automatic unique ID generation
- 📧 Email-based user verification
- 📚 Track member borrowing history

### System Features

- 💾 Persistent data storage using pickle
- 🔐 Simple login system
- ⚡ Efficient data handling
- 🛡️ Error handling and validation

## 🛠️ Technical Requirements

- Python 3.x
- Operating System: Windows/Linux/MacOS
- Minimum Storage: 50MB
- RAM: 256MB or higher

## 📂 Project Structure

```
library_management_system/
├── baseclass.py     # Base Person class implementation
├── book.py         # Book class and inventory management
├── database.py     # Data persistence using pickle
├── librarian.py    # Librarian functionalities
├── login.py        # Authentication system
├── main.py         # Application entry point
├── member.py       # Member management
├── utils.py        # Utility functions
└── db/            # Data storage
    ├── books.txt
    ├── employees.txt
    └── members.txt
```

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/console_library_management_system.git
```

2. Navigate to project directory

```bash
cd console_library_management_system
```

## 💻 Usage

1. Start the application:

```bash
python main.py
```

2. Select your role:

   - Press 1 for Librarian
   - Press 2 for Member

3. Enter required information:
   - Name
   - Email

## 🗃️ Class Structure

### Person (Base Class)

- Properties:
  - name: str
  - email: str
- Methods:
  - **init**(name, email)
  - **str**()

### Book

- Properties:
  - title: str
  - author: str
  - copies: int
- Methods:
  - **init**(title, author, copies)
  - **str**()
  - **eq**(other)

### Member (extends Person)

- Additional Properties:
  - member_id: str
  - borrowed_books: list
- Methods:
  - borrow_book(book)
  - return_book(book)

### Librarian (extends Person)

- Additional Properties:
  - employee_id: str
- Methods:
  - add_book(book)
  - remove_book(book)

## 📝 Data Storage

The system uses three text files for data persistence:

- `books.txt`: Book inventory
- `members.txt`: Member records
- `employees.txt`: Employee data

All data is serialized using Python's pickle module.

## 🔒 Error Handling

- File not found exceptions
- Duplicate entry prevention
- Input validation
- User authentication checks

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit changes

```bash
git commit -m 'Add NewFeature'
```

4. Push to branch

```bash
git push origin feature/NewFeature
```

5. Create Pull Request

## 🐛 Bug Reporting

Submit bug reports through GitHub issues including:

- Bug description
- Steps to reproduce
- Expected vs actual behavior
- Python version
- Operating system

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

[Your Name](https://github.com/yourusername)

## 📞 Support

For support:

- Create an issue on GitHub
- Email: your.email@example.com

## 🔄 Version History

- v1.0.0
  - Initial release
  - Basic CRUD operations
  - User authentication
  - Data persistence

## 🙏 Acknowledgments

- Python standard library
- Open source community
- Object-oriented programming principles

---
