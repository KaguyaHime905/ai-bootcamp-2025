class City:
    """A city"""
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop or 0  # Se pop non è specificato, assume 0


class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []  # Lista per contenere le città

    def add(self, city):
        self.cities.append(city)

    @property
    def pop(self):
        return sum(city.pop for city in self.cities)  # Somma la popolazione di tutte le città


class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []  # Lista per contenere le regioni

    def add(self, region):
        self.regions.append(region)

    @property
    def pop(self):
        return sum(region.pop for region in self.regions)  # Somma la popolazione di tutte le regioni

    @property
    def most_populuous_city(self):
        all_cities = [city for region in self.regions for city in region.cities]
        return max(all_cities, key=lambda city: city.pop) if all_cities else None