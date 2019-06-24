
# classes,objects,instances
# classes should have functions

class Nigella:
    pass
table1 = Nigella()
table1.comp = 'hp'
table1.mouse = 'dell'
table1.envelope = 'khaki'

table2 = Nigella()
table2.comp = 'dell'
table2.phone = 'Nokia'
table2.book = 'counter book'

table3 = Nigella()
table3.bottle = 'soda'
table3.phone = 'tecno'
table3.book = 'exercise book'

print(table2.comp)

table4 = Nigella()
table4.bag = (input('what brand'))
table4.cables = (input('what type'))
table4.chairs = (input('what color'))

print(table4.chairs)