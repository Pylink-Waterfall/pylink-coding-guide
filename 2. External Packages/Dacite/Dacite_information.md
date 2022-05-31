# Dacite
## Turning dictionaries into dataclasses
### Overview
* With the standard “dataclass” module in python it is easy to convert a dataclass object into a dictionary using the dataclass.to_dict() method
* It is however not possible to automatically populate a dataclass object from a dictionary (useful when reading config YAMLs etc.)
* This is where dacite, and its dacite.from_dict() method comes in
* With dacite you can load data from your dictionary into a dataclass with one line of code, including complex, nested structures!
* [konradhalas/dacite: Simple creation of data classes from dictionaries. (github.com)](https://github.com/konradhalas/dacite)

