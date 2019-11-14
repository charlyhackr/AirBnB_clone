<p align="center">
  <img src="https://github.com/jvcortes/AirBnB_clone/blob/master/airbnb.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>

---

Clone website of AirBnB, as a required project of the Holberton School Foundations curriculum.

As of today, this repository contains the command line feature, used for administration purposes.

### The command interpreter

The command interpreter is currently capable of:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

#### Installation
```
git clone https://github.com/danyramirezg/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Usage
This interpreter has basic console commands such as help, quit, EOF, create, show, destroy, update, all and count.

### Command Snytax and Usage:

Command | Syntax | Output
------- | ------ | ------
help | `help [option]` | Displays all available commands
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id
count | `count [class_name]` or `[class_name].count()`| Counts all the instances with class name specified


### Files
File Name | Description
--- | ---
`models/base_model.py` | Base Class with public instance attributes and methods
`models/amenity.py` | An Amenity class that inherits from BaseModel
`models/city.py` | A City class that inherits from BaseModel
`models/place.py` | A Place class that inherits from BaseModel
`models/review.py` | A Review class that inherits from BaseModel
`models/state.py` | A State class that inherits from BaseModel
`models/user.py` | A User class that inherits from BaseModel
`models/engine/file_storage.py` | A class that serializes instances to a JSON file and deserializes JSON file to instances
`tests/test_models/` | Unittests for BaseModel, User, amenity, city, place, review, and state
`tests/test_models/test_engine/` | Unittest for file storage

### Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Authors
* Javier Cortés | [GitHub](https://github.com/jvcortes) |
* Carlos Alvarez | [GitHub](https://github.com/charlyhackr) |
