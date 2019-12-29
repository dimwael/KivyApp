from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.button import Button

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    label1_text: 'label 1 text'
    label2_text: 'label 2 text'
    label3_text: 'label 3 text'
    label4_text: 'label 4 text'
    label5_text: 'label 5 text'
    label6_text: 'label 6 text'
    pos: self.pos
    size: self.size
    Label:
        id: id_label1
        text: root.label1_text
    Label:
        id: id_label2
        text: root.label2_text
    Label:
        id: id_label3
        text: root.label3_text
    Label:
        id: id_label4
        text: root.label4_text
    Label:
        id: id_label5
        text: root.label5_text
    Label:
        id: id_label6
        text: root.label6_text

<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')

items = [{'SP1': 'Artikelnummer', 'SP2': 'Name', 'SP3': 'Groesse'},
         {'SP1': '510001', 'SP2': 'Big Pump', 'SP3': '1.50 L'},
         {'SP1': '523001', 'SP2': 'Leonie Still', 'SP3': '1.50 L'},
         {'SP1': '641301', 'SP2': 'Cola Mix', 'SP3': '1.50 L'}
         ]
items3 = [
  {
    "description": "Tenaris",
    "id": 3,
    "name": "TS.BA",
    "price": 1200.0,
    "qty": 50
  },
  {
    "description": "something to watch",
    "id": 4,
    "name": "tv",
    "price": 1500.0,
    "qty": 50
  },
  {
    "description": "something to watch",
    "id": 5,
    "name": "tv",
    "price": 1500.0,
    "qty": 50
  },
  {
    "description": "something to watch",
    "id": 6,
    "name": "tv",
    "price": 1500.0,
    "qty": 50
  },
  {
    "description": "something to watch",
    "id": 7,
    "name": "tv",
    "price": 1500.0,
    "qty": 50
  },
  {
    "description": "something to watch",
    "id": 8,
    "name": "tv",
    "price": 1500.0,
    "qty": 50
  },
  {
    "description": "dsqdq",
    "id": 9,
    "name": "ezaea",
    "price": 21.0,
    "qty": 2
  }
]
items_1 = {'apple', 'banana', 'pear', 'pineapple'}
items_2 = {'dog', 'cat', 'rat', 'bat'}


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    

    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 6    

    

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        #self.index = str(index)
        """
        self.label1_text = str(index)
        self.label2_text = data['id']['text']
        self.label3_text = data['name']['text']
        self.label4_text = data['description']['text']
        self.label5_text = data['price']['text']
        self.label6_text = data['quantity']['text']
        self.ids['id_label3'].text = data['id']['text']  # As an alternate method of assignment
        """
        self.index = index
        #self.label1_text = str(index)
        self.label1_text = str(index)
        self.label2_text = data['SP1']['text']
        self.label3_text = data['SP2']['text']
        self.label4_text = data['SP3']['text']
        self.label5_text = data['SP4']['text']
        self.label6_text = data['SP5']['text']

        #self.ids['id_label3'].text = data['SP2']['text']  # As an alternate method of assignment
        self.addbutton = Button(text="Delete")
        self.add_widget(self.addbutton)
        self.addbutton.bind(on_press = self.delete_prod)
        
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)
        
        

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        #if is_selected:
        #    print("selection changed to {0}".format(rv.data[index]))
        #else:
        #    print("selection removed for {0}".format(rv.data[index]))

    def delete_prod(self,rv):
        if True:
            print(self.index)
        else:
            print("selection removed for {0}".format(rv.data[index]))

        

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        #self.data = [{'SP1': {'text': str(x['SP1'])}, 'SP2': {'text':str(x['SP2'])}} for x in items]
        self.data = [{'SP1': {'text': str(x['id'])}, 'SP2': {'text':str(x['description'])} , 'SP3': {'text':str(x['name'])}, 'SP4': {'text':str(x['price'])}, 'SP5': {'text':str(x['qty'])} } for x in items3]

class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()







