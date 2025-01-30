class Person:
    def __init__(self, name, surname, phone=None):
        self.name=name
        self.surname=surname
        self.phone=phone
    def scheda_personale(self):
        return f"""
        Nome: {self.name}
        Cognome: {self.surname}
        Telefono: {self.phone}
        """
    
class Business:
    def __init__(self, name, surname=None, phone=None):
        self.name=name
        self.phone=phone
        self.surname=surname
    def scheda_personale(self):
        return f"""
        Nome: {self.name}
        Telefono: {self.phone}
        """

class Directory:
    def __init__(self):
        self.directory=[]
    def add(self, persona, *args):
        self.directory.append(persona)
    def query(self, name=None):
        return [el for el in self.directory if el.name==name]
    def find(self, surname=None):
        return [el for el in self.directory if hasattr(el, 'surname') and el.surname == surname]
    def __len__(self):
        return len(self.directory)
    
directory = Directory()
directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
print("Dopo aver aggiunto Margaret Hamilton", directory)
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
print("Dopo aver aggiunto Vedrai", directory)
directory.add(Person(name="Linda", surname="Hamilton"))
print("Dopo aver aggiunto Linda Hamilton", directory)
print(len(directory))
assert len(directory) == 3

assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
print("Dopo aver cercato Vedrai", directory.query(name="Vedrai"))
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
print("Dopo aver cercato Margaret", directory.query(name="Margaret"))
assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
print("Dopo aver cercato Hamilton", directory.find("Hamilton"))
assert [el.name for el in directory.find("333")] == ["Vedrai"]
print("Dopo aver cercato 333", directory.find("333"))