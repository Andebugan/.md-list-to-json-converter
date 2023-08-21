# .md-list-to-json-converter
Simple python script for converting markdown file with lists in it into json

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
