import requestsender as rs
import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, Canvas, ClearBuffers, ClearColor
import main as mn
class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__()
        #self.canvas = Canvas()
            
        """
        self.cols = 2

        self.add_widget(Label(text = "Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text = "Password:"))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.join = Button(text="Join")
        self.add_widget(self.join)
        self.join.bind(on_press = self.connect)

    def connect(self, instance):
        """"""Function that is called one the button is clicked
        
        Arguments:
            instance {[type]} -- [Instance of that object]
        """"""
        
        if(self.username.text =="wael" and self.password.text =="0000"):
            print("hello world")
            my_app.screen_manager.current = "create"
        else :
            print(" No way !")
        """


class CreateProduct(GridLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.cols = 4

        self.add_widget(Label(text = "name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text = "description:"))
        self.description = TextInput(multiline=True)
        self.add_widget(self.description)

        self.add_widget(Label(text = "price:"))
        self.price = TextInput(multiline=False)
        self.add_widget(self.price)

        self.add_widget(Label(text = "quantity:"))
        self.qty = TextInput(multiline=False)
        self.add_widget(self.qty)

        self.addbutton = Button(text="Add")
        self.add_widget(self.addbutton)
        self.addbutton.bind(on_press = self.create_prod)

        self.deletebutton = Button(text="delete")
        self.add_widget(self.deletebutton)
        self.deletebutton.bind(on_press = self.delete_prod)

    def create_prod(self,instance):
        """Function that push the new data in the DB
        
        Arguments:
            name {[str]} -- [name of the product]
            description {[str]} -- [description of the product]
            price {[int]} -- [price of the product]
            qty {[int]} -- [quantity of the product]
        """
        rs.post_request(self.name.text,self.description.text,self.price.text,self.qty.text, "")
    
    def delete_prod(self, instance):
        """Function that delete a product with specific id

        Arguments:
        instance {[type]} -- [description]
        """
        #rs.delete_request(self.)
        my_app.screen_manager.current = "delete"
        #return 0

class DeleteProduct:
    def build(self):
        return mn.RV()

class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen (name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.create_product = CreateProduct()
        screen = Screen (name="create")
        screen.add_widget(self.create_product)
        self.screen_manager.add_widget(screen)

        self.delete_product = mn.RV() #DeleteProduct()
        screen = Screen (name="delete")
        screen.add_widget(self.delete_product)
        self.screen_manager.add_widget(screen)


        return self.screen_manager

if __name__ == "__main__":
    my_app = EpicApp()
    my_app.run()