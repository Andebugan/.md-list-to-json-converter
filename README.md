# .md-list-to-json-converter
Simple python code for converting markdown lists to json dictionary

Converts this:
```
- a
  - 1
  - 2
    - 3
  - 4
- b  
  - a
  - b
    - c
  - d
```
into this:
```
{
  "a": {
    "1": {},
    "2": {
      "3": {}
    },
    "4": {}
  },
  "b": {
    "a": {},
    "b": {
      "c": {}
    },
    "d": {}
  }
}
```
