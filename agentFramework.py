import random

class Agent():
    def __init__(self, environment, agents):
        self.environment = environment
        self.store = 0
        self._x = random.randint(0, len(environment))
        self._y = random.randint(0, len(environment))
        self.agents = agents
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def setx(self, value):
        self._x = value
    def sety(self, value):
        self._y = value
    x = property(getx, setx, "I'm the 'x' property.")
    y = property(gety, sety, "I'm the 'y' property.")
    pass

    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % len(self.environment)
        else:
            self._x = (self._x - 1) % len(self.environment)

        if random.random() < 0.5:
            self._y = (self._y + 1) % len(self.environment)
        else:
            self._y = (self._y - 1) % len(self.environment)
    pass

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] - 10
            #self.environment[self.y][self.x] -= 10
            self.store += 10
        if self.store >= 100:
            self.store = 0
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            #self.environment[self.y][self.x] += 100
    pass

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))
    pass
    
    def disease(self, infect):
        self.infection=0
        time_infected=0
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= infect and random.random()<0.5:
                self.infection=1 
                agent.infection=0
            if dist <= infect and agent.disease==1:
                self.infection=1
        while time_infected<5:
            self.store=0
            #self.environment[self._y][self._x]=+self.store
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + self.store
            time_infected=time_infected+1
    pass

    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
        