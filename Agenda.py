
class Agenda:
    '''Nome: String ; Email: String ; Telefone: String ; id: int
    Criação da classe que irá receber os dados de cadastro de um contato da agenda, e irá devolver
    um objeto usado na interface.'''
    
    Nome,email,telefone,id = None,None,None,None

    def __init__(self,id,Nome,email,telefone):
        self.nome = Nome
        self.email = email
        self.telefone = telefone
        self.id = id

    def getNome(self):
        '''
        Função que vai devolver o nome cadastrado no objeto

        retorno:
        Nome: String
        '''
        return self.nome
    
    def getEmail(self):
        '''
        Função que vai devolver o email cadastrado no objeto

        retorno:
        Email: String
        '''
        return self.email
    
    def getTelefone(self):
        '''
        Função que vai devolver o telefone cadastrado no objeto

        retorno:
        Telefone: String
        '''
        return self.telefone
    
    def getId(self):
        '''
        Função que vai devolver o id cadastrado no objeto

        retorno:
        ID: int
        '''
        return self.id
    
    def setNome(self, newNome):
        '''
        Função que vai receber uma string e vai cadastrar o novo nome no objeto

        retorno:
        None
        '''
        self.nome = newNome

    def setEmail(self, newEmail):
        '''
        Função que vai receber uma string e vai cadastrar o novo email no objeto

        retorno:
        None
        '''
        self.email = newEmail

    def setTelefone(self, newTelefone):
        '''
        Função que vai receber uma string e vai cadastrar o novo telefone no objeto

        retorno:
        None
        '''
        self.telefone = newTelefone
    




