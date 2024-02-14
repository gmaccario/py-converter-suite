# Py Converter Suite

The purpose of this Converter is to read a text file that contains thousands of words (one per line), and create an output file that contains all the words wrapped into INSERT statements.

## Input file (snippet):
aaaaaaaa\
bbbbbbbb\
cccccccc\
dddddddd

## Output file (snippet):
INSERT INTO your-tablename (your-columnname) VALUES ("cccccccc");\
INSERT INTO your-tablename (your-columnname) VALUES ("aaaaaaaa");\
INSERT INTO your-tablename (your-columnname) VALUES ("dddddddd");\
INSERT INTO your-tablename (your-columnname) VALUES ("bbbbbbbb");
