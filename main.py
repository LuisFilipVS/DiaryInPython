from PyQt5 import QtCore, QtGui, QtWidgets
import Agenda as ag
import InterfaceMainPage
import InterfaceCreate
import InterfaceSearch
import InterfaceUpdate
import InterfaceUpdate2
import InterfaceDelete

ContadorDeCadastros = 0
key = ""

def main():
    '''Metodo principal onde será executado todas as interfaces gráficas do projeto e onde será
    definido todas as funções que realizarão a chamada da interfaces da janela.
    
    retorno:
    None
    '''
    #ChamarInterfaceMenuPrincipal(InterfaceMainPage)
    
    UiCreate = InterfaceCreate
    UiSearch = InterfaceSearch
    UiUpdate1 = InterfaceUpdate
    UiUpdate2 = InterfaceUpdate2
    UiDelete = InterfaceDelete
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InterfaceMainPage.Ui_MainWindow()
    ui.setupUi(MainWindow)


    DadosAgenda = []

    def carregarDados(endereco):
        try:
            arquivo  = open(endereco, 'r')
            
            dados = arquivo.read().split("\n")

            
            

            global ContadorDeCadastros
            ContadorDeCadastros = int(dados[0])
        
            dados.pop(0)
            if len(dados) > 0:
                if dados[-1] == "" :
                    dados.pop(-1)


            
            print("Carregando dados")
            for i in dados:
                dadosSeparados = i.split('&')
                
                DadosAgenda.append(ag.Agenda(int(dadosSeparados[0]), dadosSeparados[1], dadosSeparados[2], dadosSeparados[3]))
            
            arquivo.close()

            pass
        except:
            print("Erro ao carregar dados salvos")
            
        pass

    carregarDados('./OutputContatos.txt')

    def ChamarMainWindow():
        '''Este método irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
        traduzido de formato Ui para formato Py.
        
        Neste caso será executado a tela inicial(Menu) do prejeto da Agenda
        
        retorno: None'''

        ui.setupUi(MainWindow)
        MainWindow.show()

        def salvarDados(dados, endereco):
            arquivo = open(endereco, 'w')
            strSalvamento = ""
            global ContadorDeCadastros

            strSalvamento += str(ContadorDeCadastros) + "\n"


            for i in DadosAgenda:
                strSalvamento += str(i.getId()) + "&" + str(i.getNome()) + "&" + str(i.getEmail()) + "&" + str(i.getTelefone()) + "\n"

            arquivo.write(strSalvamento)
            arquivo.close()



            print("Dados Salvos com sucesso")

            pass

        #Events

        ui.pushButton.clicked.connect(lambda: ChamarInterfaceCreate())

        ui.pushButton_2.clicked.connect(lambda: ChamarInterfaceSearch())

        ui.pushButton_3.clicked.connect(lambda: ChamarInterfaceUpdate())

        ui.pushButton_4.clicked.connect(lambda: ChamarInterfaceDelete())

        ui.pushButton_5.clicked.connect(lambda: salvarDados(DadosAgenda,'./OutputContatos.txt'))

        #sys.exit(app.exec_())

        pass
    

    def ChamarInterfaceCreate():
        '''Este método irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
        traduzido de formato Ui para formato Py.
        
        Neste caso será executado a tela de cadastos de um novo contato da agenda
        
        Retono:
        None'''
        #import sys
        #app = QtWidgets.QApplication(sys.argv)
        #Dialog = QtWidgets.QDialog()
        #ui = UiCreate.Ui_Dialog()
        ui = UiCreate.Ui_MainWindow()
        
        ui.setupUi(MainWindow)
        MainWindow.show()

        def AdicionarDados(Nome, Email, Telefone):
            '''Nome: Str ; Email: Str; Telefone: Str
            Esta função recebe 3 argumentos refente aos dados de cadastros de um contato
            no qual será salvo em uma estrutura de dados Dicionário, onde a chave é o nome do contato
            
            Retorno: None'''
            global ContadorDeCadastros
            ContadorDeCadastros += 1
            #DadosAgenda[Nome] = [ContadorDeCadastros, Email,Telefone]
            Contato = ag.Agenda(ContadorDeCadastros,Nome,Email,Telefone)
            DadosAgenda.append(Contato)
            pass

        def ObterDados():
            '''None : None
            Esta é uma função auxiliar usada para caputar os dados em String dos formulários da página
            de cadastro de contato para a agenda

            Retorno None
            '''

            nome = ui.lineEdit.text()
            Telefone = ui.lineEdit_2.text()
            Email = ui.lineEdit_3.text()
            print(nome  + Telefone + Email)

            AdicionarDados(nome,Telefone,Email)
            print("Teste --ObterDados-- Executado com Sucesso")
            
        #Events
        ui.pushButton.clicked.connect(lambda: ObterDados())

        ui.pushButton_2.clicked.connect(lambda: ChamarMainWindow())

        pass

    def ChamarInterfaceSearch():
        '''Este método irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
        traduzido de formato Ui para formato Py.
        
        Neste caso será executado a tela de consulta de contatos na agenda'''
        ui = UiSearch.Ui_MainWindow()
        ui.setupUi(MainWindow)

        def AdicionarDadosNaTabela(DadosAgenda):
            '''DadosAgenda : Dicionário
            Esta é uma função auxiliar usada para adicionar todos os registros encontrados no dicionário
            e para adicioná-los no Widget de tabela da interface de consulta de registros da agenda.

            Retorno None
            '''
            
            print(DadosAgenda)
            count = 0
            for i in DadosAgenda:
                ui.tableWidget.setRowCount(count + 1)
                ItemNome = QtWidgets.QTableWidgetItem(i.getNome())
                ItemID = QtWidgets.QTableWidgetItem(str(i.getId()))
                ItemEmail = QtWidgets.QTableWidgetItem(i.getEmail())
                ItemTelefone = QtWidgets.QTableWidgetItem(i.getTelefone())
                ui.tableWidget.setItem(count,0,ItemID)
                ui.tableWidget.setItem(count,1,ItemNome)
                ui.tableWidget.setItem(count,2,ItemEmail)
                ui.tableWidget.setItem(count,3,ItemTelefone)

                count += 1
            pass

        AdicionarDadosNaTabela(DadosAgenda)

        MainWindow.show()

        #Events

        ui.pushButton_2.clicked.connect(lambda: ChamarMainWindow())
        pass

    def ChamarInterfaceUpdate():
        '''Este mdo irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
        traduzido de formato Ui para formato Py.
        
        Neste caso será executado a tela para alterar contato da agenda
        
        Retorno: 
        None'''
        ui = UiUpdate1.Ui_MainWindow()
        ui.setupUi(MainWindow)

        def AdicionarDadosNaTabela(DadosAgenda):
            '''DadosAgenda : Dicionário
            Esta é uma função auxiliar usada para adicionar todos os registros encontrados no dicionário
            e para adicioná-los no Widget de tabela da interface de consulta de registros da agenda.

            Retorno None
            '''
            print(DadosAgenda)
            count = 0
            for i in DadosAgenda:
                   
                ui.tableWidget.setRowCount(count + 1)
                ItemNome = QtWidgets.QTableWidgetItem(i.getNome())
                ItemID = QtWidgets.QTableWidgetItem(str(i.getId()))
                ItemEmail = QtWidgets.QTableWidgetItem(i.getEmail())
                ItemTelefone = QtWidgets.QTableWidgetItem(i.getTelefone())
                ui.tableWidget.setItem(count,0,ItemID)
                ui.tableWidget.setItem(count,1,ItemNome)
                ui.tableWidget.setItem(count,2,ItemEmail)
                ui.tableWidget.setItem(count,3,ItemTelefone)

                count += 1

        AdicionarDadosNaTabela(DadosAgenda)


        def ChamarInterfaceUpdate2(id):
            '''Este método irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
            traduzido de formato Ui para formato Py.
        
            Neste caso será executado a tela auxiliar para alterar contato da agenda
            Retorno: None
            '''
            print(id)
            ui = UiUpdate2.Ui_MainWindow()
            ui.setupUi(MainWindow)

            IndexCount = 0
            for item in DadosAgenda:
                if str(item.getId()) == str(id):
                    global key
                    key = item
                    break
                IndexCount += 1
            
            #print(key)
            ui.label_9.setText(key.getNome())
            ui.label_10.setText(key.getEmail())
            ui.label_11.setText(key.getTelefone())
            ui.label_12.setText(str(key.getId()))

            def AlterarDados(id, key):
                '''id : Int ; key : Str

                Esta é uma função auxiliar usada para alterar um registro da base de contato.
                A função recebe um numero identificador "ID", e nome do registro, fundamental para
                realizar o processo de exclusão.
 
                Retorno None'''

                NovoNome = ui.lineEdit.text()
                NovoTelefone = ui.lineEdit_2.text()
                NovoEmail = ui.lineEdit_3.text()
                CountIndex = 0
                for i in DadosAgenda:
                    if(i.getId() == key.getId()):
                        DadosAgenda.pop(CountIndex)
                        break
                    CountIndex += 1
                    
                
                DadosAgenda.append(ag.Agenda(id, NovoNome, NovoEmail, NovoTelefone))
                print("Dados Alterados com Sucesso!")
                ChamarInterfaceUpdate()
                
                pass
            #Events

            ui.pushButton_2.clicked.connect(lambda: ChamarInterfaceUpdate())

            ui.pushButton.clicked.connect(lambda: AlterarDados(id, key))

            pass

        

        #Events
        ui.pushButton.clicked.connect(lambda: ChamarInterfaceUpdate2(ui.lineEdit.text()))

        ui.pushButton_2.clicked.connect(lambda: ChamarMainWindow())
        pass
    
    def ChamarInterfaceDelete():
        '''Este método irá criar uma interface gráfica com os elementos oriundos de um arquivo Python
        traduzido de formato Ui para formato Py.
        
        Neste caso será executado a tela de exclusão de um registro de cadastro na agenda'''
        ui = UiDelete.Ui_MainWindow()
        ui.setupUi(MainWindow)
    
        def AdicionarDadosNaTabela(DadosAgenda):
            '''DadosAgenda : Dicionário
            Esta é uma função auxiliar usada para adicionar todos os registros encontrados no dicionário
            e para adicioná-los no Widget de tabela da interface de consulta de registros da agenda.

            Retorno None
            '''
            print(DadosAgenda)
            count = 0
            for i in DadosAgenda:
                ui.tableWidget.setRowCount(count + 1)
                ItemNome = QtWidgets.QTableWidgetItem(i.getNome())
                ItemID = QtWidgets.QTableWidgetItem(str(i.getId()))
                ItemEmail = QtWidgets.QTableWidgetItem(i.getEmail())
                ItemTelefone = QtWidgets.QTableWidgetItem(i.getTelefone())
                ui.tableWidget.setItem(count,0,ItemID)
                ui.tableWidget.setItem(count,1,ItemNome)
                ui.tableWidget.setItem(count,2,ItemEmail)
                ui.tableWidget.setItem(count,3,ItemTelefone)

                count += 1
            pass

        AdicionarDadosNaTabela(DadosAgenda)

        def ApagarRegistro(id):
            '''id : Int

            Esta é uma função auxiliar usada para apagar um registro da base de contato.
            A função recebe um numero identificador "ID" no qual será usado para idenficar qual
            é o cadastro no qual será realizado a exclusão
 
            Retorno None
            '''
            IndexCount = 0
            for item in DadosAgenda:
                if str(item.getId()) == str(id):
                    global key
                    key = item
                    DadosAgenda.pop(IndexCount)
                    break
                IndexCount += 1
            
            #DadosAgenda.pop(key)
            ui.tableWidget.clear()
            ui.tableWidget.update()
            print("Dados Apagados com Sucesso")
            AdicionarDadosNaTabela(DadosAgenda)
            pass
        MainWindow.show()

        #Events
        ui.pushButton_2.clicked.connect(lambda: ChamarMainWindow())

        ui.pushButton.clicked.connect(lambda: ApagarRegistro(ui.lineEdit.text()))
        pass
    
    #Events
    ui.pushButton.clicked.connect(lambda: ChamarInterfaceCreate())

    ui.pushButton_2.clicked.connect(lambda: ChamarInterfaceSearch())

    ui.pushButton_3.clicked.connect(lambda: ChamarInterfaceUpdate())

    ui.pushButton_4.clicked.connect(lambda: ChamarInterfaceDelete())
                                  
    #MainWindow.show()
    ChamarMainWindow()
    sys.exit(app.exec_())
    
main()

        