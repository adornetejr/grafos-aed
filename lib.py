class Vertice():
    def __init__(self, id):
        self.id = id
        self.estimativa = 999999
        self.input = 0
        self.output = 0
        self.visitado = False
        self.predecessor = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setInput(self, inp):
        self.input = inp

    def setOutput(self, out):
        self.output = out

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa

    def __str__(self):
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
            self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso

    def __lt__(self, v):
        return self.estimativa < v.estimativa

    def __eq__(self, v):
        return self.estimativa == v.estimativa

    def __eq__(self, v):
        return self.id == v.id

    def __gt__(self, v):
        return self.estimativa > v.estimativa

class Aresta():
	def __init__(self,origem,destino,peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso
				
	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino
	
	def setPeso(self,peso):
		self.peso = peso
		
	def	getPeso(self):
		return self.peso
		
	def setOrigem(self,vertice):
		self.origem = vertice
		
	def setDestino(self,vertice):
		self.destino = vertice
	
	def __str__(self):
		return "A(%s----%i---->%s)" % (self.origem.getId(),self.peso,self.destino.getId())

class Grafo:
    def __init__(self, direcionado=True):
        self.vertices = []
        self.arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novoVertice(self, identificador):
        self.vertices.append(Vertice(identificador))

    def buscaVertice(self, identificador):  # Método recebe um int
        for i in self.vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def novaAresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.buscaVertice(origem)
        destino_aux = self.buscaVertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

 def buscaAresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

   def matrixAdjacencia(self):
        destino_Aux = self.buscaVertice(destino)
        if len(destino_Aux.predecessor) == 0:
            print("Não há caminho")
        else:
            print(destino)
            self.imprime_Grafo(origem, destino)

   def imprimeGrafocomDestino(self, origem, destino):
        destino_Aux = self.buscaVertice(destino)
        if len(destino_Aux.predecessor) == 0:
            print("Não há caminho")
        else:
            print(destino)
            self.imprimeGrafo(origem, destino)

    def imprimeGrafo(self, origem, destino):
        if origem == destino:
            print("Fim")
        else:
            destino_Aux = self.buscaVertice(destino)
            if len(destino_Aux.predecessor) == 0:
                print("Não há caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprimeGrafo(origem, destino_Aux.predecessor[0])

    def estaVazio(self):
        if len(self.vertices) == 0:
            return True
        else:
            return False

    def buscaAdjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.arestas)):
            origem = self.arestas[i].getOrigem()
            destino = self.arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None

    def depthFirstSearch(self):
        self.tempo = 0
        for v in self.vertices:
            v.setVisitado(False)
            v.input = 0
            v.output = 0
        for v in self.vertices:
            if not v.getVisitado():
                self.visita(v)

    def visita(self, u):
        print("Visitando o vertice: %s" % u.getId())
        u.setVisitado(True)
        self.tempo += 1
        u.setImput(self.tempo)
        v = self.buscaAdjacente(u)  # retorna apenas não visitado ou nulo
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.buscaAdjacente(u)

        self.tempo += 1
        u.setOutput(self.tempo)
        print("Voltando para: ", u.predecessor)

    def inicializaFonte(self, fonte):  # Função usado no BFS e Dijkstra Método recebe um Objeto
        for v in self.vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte.setVisitado(True)
        fonte.setEstimativa(0)

    def breadthFirstSearch(self, identificador):
        fonte = self.buscaVertice(identificador)
        if fonte is None:
            return "Vertce Nulo"
        self.inicializaFonte(fonte)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.buscaAdjacente(u)  # retorna adjacente não visitado
            if v is None:
                lista.pop(0)  # retiro o vertice sem adjacentes

            else:
                self.tempo += 1
                v.setImput(self.tempo)
                v.predecessor.append(u.getId())
                v.setVisitado(True)
                lista.append(v)

            u.setVisitado(True)

    def relaxaVertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())  # guarda apenas o id

    def dijkstra(self, origem):
        fonte = self.buscaVertice(origem)
        if fonte is None:
            return "Vértice Nulo"

        self.inicializaFonte(fonte)
        lista = []
        resposta = []  # conjunto resposta
        for i in self.vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.buscaAdjacente(u)
            if v is None:
                for i in self.vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(
                        False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                self.tempo += 1
                u.setImput(self.tempo)  # apenas mostra a ordem de visitação do grafo
                resposta.append(lista[0])
                lista.pop(0)  # retiro vertice sem adjacente da lista

            else:
                w = self.buscaAresta(u, v)
                if w is not None:
                    self.relaxaVertice(u, v, w)

        print("Estimativas: ")
        for i in resposta:
            print(i)  # imprimo as respostas
    
    def bellManFord2(self,origem):
        acc = 0
        fonte = self.buscaVertice(origem)
        self.inicializaFonte(fonte)
        for i in range(1,len(self.vertices)-1):
            for w in self.arestas:
                u = w.getOrigem()
                v = w.getDestino()
                if u.getEstimativa()+w.getPeso() < v.getEstimativa():
                    v.predecessor= [u.getId()]
                    v.setEstimativa(u.getEstimativa()+w.getPeso())

        for w in self.arestas:
            u = w.getOrigem()
            v = w.getDestino()
            if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                acc=acc+1
        if acc>0:
            return True
        else:
            return False
    
    def bellmanFord(self, origem):
        fonte = self.buscaVertice(origem)
        self.inicializaFonte(fonte)
        for i in range(1,len(self.vertices)-1):
            for w in self.arestas:
                u = w.getOrigem()
                v = w.getDestino()
                #self.relaxaVertice(u, v, w)
                if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                    print(u.getEstimativa(),w.getPeso(), v.getEstimativa())
                    v.setEstimativa(u.getEstimativa() + w.getPeso())
                    v.predecessor=u.getId()  # guarda apenas o id

        for w in self.arestas:
            u = w.getOrigem()
            v = w.getDestino()
            if u.getEstimativa() + w.getPeso()<v.getEstimativa() :
                return False  # Não existe ciclo negativo
            else:
                return True  # Exixte ciclo negatio

    def minimumSpanningTree(self, origem):  # Prim
        fonte = self.buscaVertice(origem)
        if fonte is None:
            return "Vertice Nulo"

        self.inicializaFonte(fonte)
        lista = []
        for i in self.vertices:
            lista.append(i)
        lista.sort()
        while len(lista) != 0:
            # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.buscaAdjacente(u)

            if v is None:
                for i in lista:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(
                        False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                    # retiro vertice sem adjacente
                lista.sort()
                self.tempo += 1
                u.setImput(self.tempo)
                lista.remove(u)
            else:
                w = self.buscaAresta(u, v)
                if lista.count(v) > 0:
                    if v.getEstimativa() > w.getPeso():
                        v.predecessor = [u.getId()]
                        v.setEstimativa(w.getPeso())

        for u in self.vertices:
            if len(u.predecessor) > 0:
                print(u.predecessor, "------", u.getId())
        self.vertices.sort(key=lambda u: u.input, reverse=False)
        for i in self.vertices:
            print(i)

    def grafoCiclico(self):
        if (len(self.arestas) > len(self.vertices) - 1):
            print("Grafo Cíclico por Nº Aresta : %i > Nº Vértices: %i" % (
            len(self.arestas), len(self.vertices)))
        else:
            print("Grafo Acíclico")

    def grafoTransposto(self):  # w(u,v) passa a ser w(v,u)
        for i in range(len(self.arestas)):
            origem = self.arestas[0].getOrigem()
            destino = self.arestas[0].getDestino()
            self.arestas.pop(0)
            self.arestas.append(Aresta(destino, origem, 0))

    def strongComponentAlgorithm(self):
        print("Busca em Profundidade")
        self.depthFirstSearch()
        self.vertices.sort(key=lambda u: u.output, reverse=True)  # ordena a lista em ralação a vertice.output
        for w in self.arestas:
            print(w)
        self.grafoTransposto()
        print("Grafo Transposto:")
        for w in self.arestas:
            print(w)
        for i in self.vertices:
            i.input = 0
            i.output = 0
            i.setVisitado(False)
        print("\nComponetes fortemente Conexos\n")
        for i in self.vertices:
            if not i.getVisitado():
                self.visita(i)

    def criaEuleriano(self):
        pass

    def grafoEuleriano(self):
        for u in self.vertices:
            if self.grau(u) % 2 is not 0:
                return False
        return True

    def grau(self, u):
        grau = 0
        for w in self.arestas:
            if u == w.getOrigem():
                grau += 1
        return grau

    def ponto(self, u):
        for v in self.vertices:
            v.setVisitado(False)

        u.setVisitado(True)
        self.visita(self.buscaAdjacente(u))
        for v in self.vertices:
            if v.getVisitado() == False:
                return True

    def articulation(self):
        art = []
        for u in self.vertices:
            if self.ponto(u):
                art.append(u.getId())
        print("Pontos de Articulação", art)