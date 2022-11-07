import zad1, zad2

df = zad1.DecisionSystem('iris.txt', 'iris-type.txt')
print(df.get_all_objects()[0].values)
print(df.get_attr_name())
print(df.get_attr_type(1))
print(df.get_all_object_float([0, 2], [3, 4]))
