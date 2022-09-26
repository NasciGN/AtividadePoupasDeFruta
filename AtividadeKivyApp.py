import kivy

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


kivy.require('2.1.0')
class TelaPrincipal(GridLayout):
    litros = ObjectProperty(None)
    maracuja = ObjectProperty(None)
    caju = ObjectProperty(None)
    goiaba = ObjectProperty(None)
    adAcucar = ObjectProperty(None)
    adGelo = ObjectProperty(None)
    mensagens = ObjectProperty(None)
        
    def VerificarEscolhas(self):
        self.mensagens.text = ''
        porcaoAgua=0
        porcaoSuco=0
        quantia=None
        litrosEdit=None
        sabor=None
        try:
            float(self.ids.litros.text)
            quantia=float(self.ids.litros.text)
            litrosEdit=quantia
            if self.adAcucar.active & self.adGelo.active:
                litrosEdit=(quantia-(quantia*0.02)) - (quantia*0.05)
            elif self.adAcucar.active:
                litrosEdit=quantia-(quantia*0.02)
            elif self.adGelo.active:    
                litrosEdit=quantia-(quantia*0.05)
            
            if self.maracuja.active:
                porcaoSuco=quantia*0.4
                porcaoAgua=litrosEdit*0.6
            elif self.caju.active:
                porcaoSuco=quantia*0.8
                porcaoAgua=litrosEdit*0.2
            elif self.goiaba.active:
                porcaoSuco=quantia*0.5
                porcaoAgua=litrosEdit*0.5
            poupas=[self.maracuja, self.caju, self.goiaba]
            for s in poupas:
                if s.active:
                        self.mensagens.text += f'Poupa escolhida: {s.text}' + '\n'
                        sabor=s.text
        except (TypeError, ValueError):
            lbErroNoFloat=Label(text='Por favor, verifique se o valor inserido está correto!')
            popup = Popup(title='Error 460', content=lbErroNoFloat, auto_dismiss=True)
            popup.size_hint=(0.75, 0.4)
            popup.open()
        
        if sabor==None or litrosEdit==None:
            self.mensagens.text=''
            lbErroEmp=Label(text='Verifique se você preencheu as opções que são requisitadas')
            popup = Popup(title='Error 489', content=lbErroEmp, auto_dismiss=True)
            popup.size_hint=(0.75, 0.4)
            popup.open()
        else:
            self.mensagens.text += f'Para preparar o suco de {sabor} adicione {round(porcaoSuco, 1)} litros de poupa ao liquidificador' + '\n'
            self.mensagens.text += f'Apos isso adicione mais {round(porcaoAgua, 2)} litros de água.'

        
        

class AtividadeKivyApp(App):
    def build(self):
        kivy.config.Config.set('graphics', 'resizable',  False)
        tela=TelaPrincipal()
        tela.size=200, 210
        return tela

if __name__== "__main__":
    AtividadeKivyApp().run()

