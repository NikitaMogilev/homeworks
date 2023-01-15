class Country:
    def __init__(self, population):
        self.population = population

    def setPopulation(self, population):
        self.population = population
        return print(f'введенное население страны {self.population}')

    @property
    def getPopulation(self):
        return print(f'население страны {self.population}')


class Russia(Country):
    pass


class Canada(Country):
    pass


class Germany(Country):
    pass


russia_population = Russia(15000000)
russia_population.getPopulation
russia_population.setPopulation(500000)
russia_population.getPopulation
russia_population.setPopulation(500077700)
russia_population.getPopulation
