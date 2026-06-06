class project:
    def __init__(self,use,dur):
        self.name="Python"
        self.use=use
        self.dur=dur 
        self.tools=[]
        self.lang=None
        print("welcome to the project")

        ob1=project("coding", 4)
        ob2=project("programming", 6)
        print(ob1.name)
        print(ob1.use,ob1.dur)
        print(ob2.use,ob2.dur)
        ob1.tools="vs code"
        print(ob1.tools)
        ob2.tools="jupyter"
        print(ob2.tools)
        ob1.lang="C"
        ob2.lang="C++"
        print(ob1.lang)
        print(ob2.lang)