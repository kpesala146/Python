"Python Lists"
"Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type."

"The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator."


list=["test", 2333, "hello"];
print(list);
print(list[2]);
list.append("add value");
print(list);
list.append("Sub Value");
print(list);
list.remove(list[3]);
print(list);