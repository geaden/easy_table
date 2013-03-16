Easy rST table
==============

It's a script of generating rst-structrured tables.

Create rst tables with ease.

**Example**
===========

Source table:
_____________

:stable:
id code name
1 2 test
2 3 py
3 4 sub
:etable:

Result table:
_____________

+----+------+------+
| id | code | name |
+====+======+======+
|  1 |    2 | test |
+----+------+------+
|  2 |    3 |   py |
+----+------+------+
|  3 |    4 |  sub |
+----+------+------+


Constraints
===========

Table in your source should be marked with tags :stable: - beginning of table,
:etable: - end of table without spaces after start tag and before end tag.

I found it useful for generating sceleton of table.

It leaves rest content of the file. Just rewrites section marked with `:stable:` and `:etable:`

But remember you use it on your own risk, as I have no warranty that your data won't be corrupted after
processing.

TODO
====

- Support multiple tables in file
- Support cells containing whitespases
- Support type. Currently only Grid type is supported

