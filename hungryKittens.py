import hungryKittens_class

kittens = []

def newKitten():
    name = input("What's the name of this kitten? ")
    voice = input("What does it say? ")
    hunger = int(input("How hungry it is? "))
    age = int(input("How old is it? "))
    kittens.append(hungryKittens_class.Kittens(name, voice, hunger, age))

def which(kitten1, kitten2,hung_age):
  if hung_age=="hunger":
      return kitten1.hunger>kitten2.hunger
  else:
      return kitten1.age>kitten2.age

def feed(kitten):
    kitten.hunger=0
    kitten.voice="purr"
    txt=f"{kitten.name} says {kitten.voice}"
    print(txt)



def task1(label):
    print(label)
    txt = "Meow!!!"
    print(f"{txt * 3}")

def task2(label):
    print(label)
    newKitten()

def task3(label):
    print(label)
    for i in range(2):
        newKitten()
        kittens[len(kittens)-1].isHungry()
    txt=f"{kittens[1].name if which(kittens[1],kittens[2],'hunger') else kittens[2].name} is the hungrier."
    print(txt)

def task4(label):
    print(label)
    newKitten()
    kitten1=kittens[len(kittens)-1]
    newKitten()
    kitten2=kittens[len(kittens)-1]
    if which(kitten1,kitten2,"age"):
        feed(kitten1)
        feed(kitten2)
    else:
        feed(kitten2)
        feed(kitten1)

task1("Task 1")
#task2("Task 2")
#task3("Task 3")
task4("Task 4")