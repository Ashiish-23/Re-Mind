# Re-Mind

# Kivy Lab - Task Management Applications

A collection of task management applications built with Kivy and KivyMD, featuring modern Material Design UI components and persistent data storage.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Applications](#applications)
  - [Basic To-Do App](#basic-to-do-app)
  - [RE-MIND Task Manager](#re-mind-task-manager)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Technical Details](#technical-details)
- [License](#license)

## 🎯 Overview

This project contains two task management applications built with KivyMD:

1. **Basic To-Do App** (`main1.py`) - A simple to-do list application with real-time clock display
2. **RE-MIND Task Manager** (`RE-MIND/main.py`) - A feature-rich task manager with persistent storage, date picking, and task completion tracking

Both applications showcase different approaches to building GUI applications with KivyMD, demonstrating various UI components and data management techniques.

## ✨ Features

### Basic To-Do App
- ✅ Create tasks with title, description, and due date
- 🕐 Real-time clock display
- 📝 Scrollable task list using RecycleView for efficient rendering
- 🎨 Material Design UI with customizable theme (Blueviolet palette)
- 📅 Date picker integration

### RE-MIND Task Manager
- ✅ Create, edit, and delete tasks
- 📅 Interactive date picker with formatted date display
- ☑️ Mark tasks as complete/incomplete with checkboxes
- 💾 Persistent data storage using JSON
- 🔄 Automatic task loading on app startup
- 🎨 Modern Material Design UI with Orange theme
- 🗑️ Task deletion with visual feedback
- 📝 Two-line task display with task name and date

## 🚀 Applications

### Basic To-Do App

A straightforward to-do list application demonstrating basic KivyMD concepts.

**Files:**
- `main1.py` - Main application logic
- `Lab.kv` - User interface layout file

**Running:**
```bash
python main1.py
```

### RE-MIND Task Manager

A full-featured task management application with persistent storage and advanced UI components.

**Files:**
- `RE-MIND/main.py` - Main application logic
- `RE-MIND/remind.kv` - User interface layout file
- `RE-MIND/taskmanager.py` - Task persistence layer
- `RE-MIND/task.json` - JSON data storage file

**Running:**
```bash
cd RE-MIND
python main.py
```

## 📦 Requirements

- **Python:** 3.9.2 or higher (compatible with Python 3.7+)
- **Operating System:** Windows, macOS, Linux, Android, iOS

## 🔧 Installation

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd kivy-lab
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install kivy kivymd
```

Or install from a requirements file (if available):

```bash
pip install -r requirements.txt
```

**Note:** For Kivy installation on different platforms, refer to the [official Kivy installation guide](https://kivy.org/doc/stable/gettingstarted/installation.html).

### Step 3: Verify Installation

Ensure all dependencies are installed correctly:

```bash
python -c "import kivy; import kivymd; print('Installation successful!')"
```

## 📖 Usage

### Basic To-Do App

1. Run the application:
   ```bash
   python main1.py
   ```

2. **Adding a Task:**
   - Enter a title in the "Title" field
   - Enter a description in the "Description" field
   - Select a due date using the date picker
   - The task will be automatically added to the list

3. **Viewing Tasks:**
   - Scroll through the task list to view all tasks
   - Tasks display title, description, and formatted due date
   - The current time is displayed in the top-right corner

### RE-MIND Task Manager

1. Navigate to the RE-MIND directory and run the application:
   ```bash
   cd RE-MIND
   python main.py
   ```

2. **Adding a Task:**
   - Click the floating action button (plus icon) at the bottom
   - Enter your task in the dialog box
   - Click the calendar icon to select a due date
   - Click "SAVE" to add the task or "CANCEL" to discard

3. **Managing Tasks:**
   - **Mark as Complete:** Click the checkbox next to a task
   - **Delete Task:** Click the trash icon on the right side of a task
   - **View Tasks:** All tasks are displayed in a scrollable list

4. **Data Persistence:**
   - All tasks are automatically saved to `task.json`
   - Tasks are loaded automatically when you restart the application
   - Completed tasks are marked with strikethrough text

## 📁 Project Structure

```
kivy-lab/
├── main1.py                 # Basic To-Do App main file
├── Lab.kv                   # Basic To-Do App UI layout
├── RE-MIND/
│   ├── main.py              # RE-MIND Task Manager main file
│   ├── remind.kv            # RE-MIND UI layout
│   ├── taskmanager.py       # Task persistence layer (JSON operations)
│   ├── task.json            # Task data storage (JSON format)
│   ├── PT_Sans/             # Custom font files
│   │   ├── PTSans-Regular.ttf
│   │   ├── PTSans-Bold.ttf
│   │   ├── PTSans-Italic.ttf
│   │   ├── PTSans-BoldItalic.ttf
│   │   └── OFL.txt          # Font license (SIL Open Font License)
│   └── __pycache__/         # Python cache files
├── .vscode/
│   └── settings.json        # VS Code configuration
└── README.md                # This file
```

## 📚 Dependencies

### Core Dependencies

- **Kivy** - Open-source Python framework for rapid development of applications with innovative user interfaces
- **KivyMD** - Material Design components library for Kivy

### Standard Library Modules Used

- `datetime` - Date and time handling
- `json` - JSON file operations for data persistence
- `kivy.clock` - Clock and scheduling functionality
- `kivy.properties` - Reactive properties system

### KivyMD Components Used

- `MDApp` - Base application class
- `MDDialog` - Dialog boxes
- `MDBoxLayout` - Layout containers
- `MDDatePicker` - Date selection widget
- `MDTextField` - Text input fields
- `MDList` - List containers
- `MDCheckbox` - Checkbox widgets
- `MDFloatingActionButton` - Floating action buttons
- `MDToolbar` - App bar/toolbar
- `MDLabel` - Text labels
- `RecycleView` - Efficient list rendering

## 🔍 Technical Details

### Data Storage

The RE-MIND application uses JSON for data persistence:

- **Storage File:** `RE-MIND/task.json`
- **Data Format:**
  ```json
  [
    {
      "id": 0,
      "task": "Task description",
      "date": "Monday 01 January 2024",
      "complete state": false
    }
  ]
  ```

### Task Manager Module

The `taskmanager.py` module provides the following functions:

- `list_store()` - Check if tasks exist in storage
- `load_tasks()` - Load all tasks from JSON file
- `add_task(task, date)` - Add a new task
- `pop_task(index)` - Delete a task by index
- `get_tasks()` - Get the most recent task
- `task_complete(task_id)` - Mark task as complete
- `task_incomplete(task_id)` - Mark task as incomplete

### UI Architecture

Both applications follow the Model-View-Controller (MVC) pattern:

- **Model:** Task data structures (`ToDoItem` class, JSON storage)
- **View:** KV language files (`.kv`) defining UI layout
- **Controller:** Python application classes handling logic and user interactions

## 🎨 Customization

### Changing Themes

**Basic To-Do App:**
Edit the theme in `main1.py`:
```python
self.theme_cls.primary_palette = "Blueviolet"  # Change to any KivyMD palette
```

**RE-MIND:**
Edit the theme in `RE-MIND/main.py`:
```python
self.theme_cls.primary_palette = "Orange"  # Change to any KivyMD palette
```

Available palette options: `"Red"`, `"Pink"`, `"Purple"`, `"DeepPurple"`, `"Indigo"`, `"Blue"`, `"LightBlue"`, `"Cyan"`, `"Teal"`, `"Green"`, `"LightGreen"`, `"Lime"`, `"Yellow"`, `"Amber"`, `"Orange"`, `"DeepOrange"`, `"Brown"`, `"Grey"`, `"BlueGrey"`

### Font Customization

The RE-MIND app includes PT Sans fonts in the `RE-MIND/PT_Sans/` directory. To use these fonts, configure them in your KV file or Python code.

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors:**
   - Ensure Kivy and KivyMD are installed: `pip install kivy kivymd`
   - Check Python version compatibility (Python 3.7+)

2. **KV File Not Loading:**
   - Ensure `.kv` files are in the same directory as the Python file
   - Check file names match exactly (case-sensitive)

3. **JSON File Errors:**
   - Ensure `task.json` exists in the `RE-MIND/` directory
   - If corrupted, delete `task.json` and restart the app (it will create a new one)

4. **Display Issues:**
   - Update Kivy/KivyMD to the latest versions
   - Check graphics drivers if running on Linux

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

### Code License

The code in this project is provided as-is for educational and personal use.

### Font License

The PT Sans fonts included in `RE-MIND/PT_Sans/` are licensed under the [SIL Open Font License (OFL)](RE-MIND/PT_Sans/OFL.txt). Please refer to the OFL.txt file for license details.

## 📝 Notes

- The Basic To-Do App (`main1.py`) stores tasks in memory only (data is lost on app close)
- The RE-MIND Task Manager persists data to JSON, so tasks are saved between sessions
- Both applications are desktop-focused but can be adapted for mobile platforms
- The RecycleView in the Basic To-Do App provides efficient rendering for large task lists

## 🔗 Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [KivyMD Documentation](https://kivymd.readthedocs.io/)
- [KivyMD GitHub](https://github.com/kivymd/KivyMD)
- [KivyMD Material Design Components](https://kivymd.readthedocs.io/en/latest/components/)

---

**Author:** [Your Name]  
**Version:** 1.0.0  
**Last Updated:** 2024

