import pickle
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
pickling_on = open("Emp.pickle","w")
pickle.dumps(emp, pickling_on)
pickling_on.close()