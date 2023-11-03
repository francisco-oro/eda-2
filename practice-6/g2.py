class Vertice:
    def __init__ (self,n):
        self.nombre = n
        self.vecinos = list()
        self.distancia = 0
        self.color = 'white'
        self.pred = -1

    def agregarVecino (self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    vertices = {}

    def agregarVertice (self,vertice):
        if isinstance (vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False
        
    def agregarArista (self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False
    
    def bfs (self,vert):
        vert.distancia = 0
        vert.color = 'gris'
        vert.pred = -1
        
        q = list()
        q.append(vert.nombre)
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gris'
                    node_v.distancia = node_u.distancia+1
                    node_v.pred = node_u.nombre
                    q.append(v)
            self.vertices[u].color = 'black'

    def imprimeGrafo(self):
        print("- GRAFO G2 -")
        for key in sorted(list(self.vertices.keys())):
            print("\nVertice "+key+" Sus vecinos son "+ str(self.vertices[key].vecinos))
            print("Vertice "+key+" El predecesor es "+ str(self.vertices[key].pred))
            print("La distancia de A a "+key+" es: "+ str(self.vertices[key].distancia))

class Controladora:
    def main (self):
        #Se crea un objeto 'g' de la clase Grafo:
        g = Grafo()
        #Se crea un objeto 'a' de la clase Vertice:
        a = Vertice('A')
        #Se agrega el vertice al grafo:
        g.agregarVertice(a)

        for i in range(ord('A'),ord('M')):
            g.agregarVertice(Vertice(chr(i)))

        edges = ['AB','AD','AE','AL', 'BC','BF','BK','CK', 'CG','CD', 'DL', 'DH', 
                 'EF', 'EI', 'FJ', 'GK', 'GH', 'HL', 'IJ', 'IL', 'JK', 'KL' ]
        for edge in edges:                                                  
            g.agregarArista(edge[:1],edge[1:])

        for i in range(ord('A'),ord('M')):
            g.bfs(Vertice(chr(i)))

        g.imprimeGrafo()

obj = Controladora()
obj.main()                                                                                                  