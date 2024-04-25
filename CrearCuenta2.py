from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

Builder.load_string('''
<CasillaTexto>:
    foreground_color: 0, 0, 0, 1  # Color del texto
    cursor_color: 0, 0, 0, 1   # Color del cursor
    padding: [20, (self.height - self.line_height) / 2]  # Espacio en el borde
    font_size: '11sp'  # Tamaño de la fuente
    font_name: "Inter.ttc"  # Fuente de la letra
    border_color: (0.945, 0.761, 0.639, 1)
    
<EnlaceLabel>:
    size_hint: None, None
    size: self.texture_size
    color: (0, 0, 0, 1)
    font_name: "Inter.ttc"  # Fuente de la letra
    font_size: '10sp'

<EnlaceIniciaSesionLabel>:
    size_hint: None, None
    size: self.texture_size
    color: (0.6588, 0.4314, 0.2706, 1)
    font_name: "Inter.ttc"  # Fuente de la letra
    markup: True
    pos_hint: {'x': 0.011111, 'y': 0}
    font_size: '10sp'
''')

class CasillaTexto(TextInput):
    pass

class EnlaceLabel(Label):
    pass

class EnlaceIniciaSesionLabel(Label):
    pass

class CrearCuentaApp(App):
    def build(self):
        self.usuarios = []  # Lista para almacenar usuarios registrados
        layout = RelativeLayout()

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (360, 640)

        background = Image(source='Huellas.jpg')
        layout.add_widget(background)

        title_label = Label(
            text="¡Regístrate y deja a tus mascotas \nen las mejores manos!",
            bold=True,  # Aplica negrilla al texto
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.650},
            color=(0.6588, 0.4314, 0.2706, 1),
            valign='middle',
            line_height=1.5,
            font_size='20sp',
        )

        self.name_input = CasillaTexto(
            hint_text='Nombre Completo',
            hint_text_color=(0, 0, 0, 1),  # Color del texto del hint
            size_hint=(0.8, None),
            height=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            foreground_color=(0, 0, 0, 1),  # Color del texto
            background_color=(0.945, 0.761, 0.639, 1))  # Color del borde igual al color de fondo

        self.email_input = CasillaTexto(
            hint_text='Email',
            hint_text_color=(0, 0, 0, 1),  # Color del texto del hint
            foreground_color=(0, 0, 0, 1),  # Color del texto
            background_color=(0.945, 0.761, 0.639, 1),  # Color del borde igual al color de fondo
            size_hint=(0.8, None),
            height=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.45})

        self.password_input = CasillaTexto(
            hint_text='Contraseña',
            hint_text_color=(0, 0, 0, 1),  # Color del texto del hint
            password=True,
            size_hint=(0.8, None),
            height=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            foreground_color=(0, 0, 0, 1),  # Color del texto
            background_color=(0.945, 0.761, 0.639, 1))  # Color del borde igual al color de fondo

        register_button = Button(
            text="Crear Cuenta",
            size_hint=(0.8, None),
            height=40,
            font_size= '11sp',  # Tamaño de la fuente
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            background_color=(0.6627, 0.4314, 0.2706, 1),
            background_normal='')

        register_button.bind(on_press=self.registrar_usuario)

        layout.add_widget(title_label)
        layout.add_widget(self.name_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(register_button)

        # Añadir enlace para iniciar sesión
        enlace_layout = RelativeLayout(size_hint=(None, None), size=(327, 29), pos_hint={'center_x': 0.65, 'center_y': 0.15})
        enlace_label = EnlaceLabel(text="¿Ya tienes una cuenta? ", pos_hint={'x': 0.05, 'y': 0})
        enlace_inicia_sesion_label = EnlaceIniciaSesionLabel(text="[ref=iniciar_sesion]Inicia sesión[/ref]", pos_hint={'x': 0.4, 'y': 0})


        enlace_inicia_sesion_label.bind(on_ref_press=self.ir_a_iniciar_sesion)  # Asociar evento de clic al enlace

        enlace_layout.add_widget(enlace_label)
        enlace_layout.add_widget(enlace_inicia_sesion_label)
        
        layout.add_widget(enlace_layout)

        # Botón de la flecha
        flecha_button = Button(
            text="←",
            size_hint=(None, None),  # Establece size_hint como una tupla
            size=(30, 32),  # Tamaño fijo del botón
            pos_hint={'x': 17/360, 'top': 1 - 34/640},  # Coordenadas proporcionales para que sea responsive
            background_color=(0, 0, 0, 0),  # Fondo transparente
            background_normal='',  # Sin fondo normal
            background_down='',  # Sin fondo cuando presionado
            color=(0.6588, 0.4314, 0.2706, 1),  # Color del texto
            font_size='20sp',  # Tamaño de fuente
            bold=True,  # Negrilla
            font_name= 'Inter.ttc',  # Fuente de la letra
            markup=True)

        flecha_button.bind(on_press=self.ir_a_inicio)  # Vincular evento de clic al botón de la flecha
        
        layout.add_widget(flecha_button)

        return layout

    def registrar_usuario(self, instance):
        nombre = self.name_input.text
        correo = self.email_input.text
        contraseña = self.password_input.text

        # Validar el correo electrónico
        if '@' in correo and '.' in correo:
            # Si el correo parece válido, continuar con el registro
            self.usuarios.append({'nombre': nombre, 'correo': correo, 'contraseña': contraseña})
            print("Nombre Completo:", nombre)
            print("Email:", correo)
            print("Contraseña:", contraseña)
            self.name_input.text = ''
            self.email_input.text = ''
            self.password_input.text = ''
        else:
            # Si el correo no parece válido, mostrar un mensaje de error
            print("El correo electrónico no es válido. Por favor, ingrese un correo válido.")

    def ir_a_iniciar_sesion(self, instance, value):
        # Aquí puedes escribir el código para navegar a la pantalla de inicio de sesión
        print("Ir a la pantalla de inicio de sesión")
        
    def ir_a_inicio(self, instance):
        # Aquí puedes escribir el código para navegar a la pantalla de inicio
        print("Ir a la pantalla de inicio")

if __name__ == '__main__':
    CrearCuentaApp().run()


