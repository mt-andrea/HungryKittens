class Kitten:
    def __init__(self, name,voice,hunger,age):
        self.name=name
        self.voice=voice
        self.hunger=hunger
        self.age=age
    def isHungry(self):
        txt=f"{self.name} \n{(self.voice+' ')*self.hunger}"
        print(txt)
