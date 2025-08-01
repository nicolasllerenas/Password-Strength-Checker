import re
import tkinter as tk
from tkinter import ttk, messagebox
import sys

class PasswordStrengthChecker:
    def __init__(self):
        self.criteria = {
            'length': r'.{8,}',  # Mínimo 8 caracteres
            'uppercase': r'[A-Z]',  # Al menos una mayúscula
            'lowercase': r'[a-z]',  # Al menos una minúscula
            'numbers': r'\d',  # Al menos un número
            'special_chars': r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]',  # Caracteres especiales
            'no_spaces': r'^\S*$',  # Sin espacios
            'no_common_patterns': r'^(?!.*(?:123|abc|qwe|password|admin|user|test|123456|qwerty)).*$'  # Sin patrones comunes
        }
    
    def check_password_strength(self, password):
        """
        Verifica la fortaleza de una contraseña usando expresiones regulares
        """
        if not password:
            return "Vacía", 0, []
        
        score = 0
        feedback = []
        
        # Verificar longitud mínima
        if re.search(self.criteria['length'], password):
            score += 2
            feedback.append("✓ Longitud adecuada (8+ caracteres)")
        else:
            feedback.append("✗ Muy corta (mínimo 8 caracteres)")
        
        # Verificar mayúsculas
        if re.search(self.criteria['uppercase'], password):
            score += 1
            feedback.append("✓ Contiene mayúsculas")
        else:
            feedback.append("✗ Sin mayúsculas")
        
        # Verificar minúsculas
        if re.search(self.criteria['lowercase'], password):
            score += 1
            feedback.append("✓ Contiene minúsculas")
        else:
            feedback.append("✗ Sin minúsculas")
        
        # Verificar números
        if re.search(self.criteria['numbers'], password):
            score += 1
            feedback.append("✓ Contiene números")
        else:
            feedback.append("✗ Sin números")
        
        # Verificar caracteres especiales
        if re.search(self.criteria['special_chars'], password):
            score += 2
            feedback.append("✓ Contiene caracteres especiales")
        else:
            feedback.append("✗ Sin caracteres especiales")
        
        # Verificar que no tenga espacios
        if re.search(self.criteria['no_spaces'], password):
            score += 1
            feedback.append("✓ Sin espacios")
        else:
            feedback.append("✗ Contiene espacios")
        
        # Verificar que no tenga patrones comunes
        if re.search(self.criteria['no_common_patterns'], password, re.IGNORECASE):
            score += 1
            feedback.append("✓ Sin patrones comunes")
        else:
            feedback.append("✗ Contiene patrones comunes")
        
        # Determinar fortaleza basada en el puntaje
        if score >= 7:
            strength = "Muy Fuerte"
        elif score >= 5:
            strength = "Fuerte"
        elif score >= 3:
            strength = "Media"
        elif score >= 1:
            strength = "Débil"
        else:
            strength = "Muy Débil"
        
        return strength, score, feedback

class PasswordGUI:
    def __init__(self):
        self.checker = PasswordStrengthChecker()
        self.root = tk.Tk()
        self.root.title("Verificador de Fortaleza de Contraseñas")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Título
        title_label = tk.Label(
            self.root,
            text="🔐 Verificador de Fortaleza de Contraseñas",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Etiqueta de entrada
        input_label = tk.Label(
            main_frame,
            text="Ingresa tu contraseña:",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#34495e'
        )
        input_label.pack(pady=(0, 5))
        
        # Campo de entrada de contraseña
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            main_frame,
            textvariable=self.password_var,
            font=("Arial", 12),
            show="*",
            width=30
        )
        self.password_entry.pack(pady=(0, 10))
        self.password_entry.bind('<KeyRelease>', self.on_password_change)
        
        # Botón para mostrar/ocultar contraseña
        self.show_password_var = tk.BooleanVar()
        show_password_cb = tk.Checkbutton(
            main_frame,
            text="Mostrar contraseña",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            bg='#f0f0f0',
            font=("Arial", 10)
        )
        show_password_cb.pack(pady=(0, 15))
        
        # Frame para resultados
        results_frame = tk.Frame(main_frame, bg='#f0f0f0')
        results_frame.pack(fill='both', expand=True)
        
        # Etiqueta de fortaleza
        self.strength_label = tk.Label(
            results_frame,
            text="Fortaleza: -",
            font=("Arial", 14, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.strength_label.pack(pady=(0, 10))
        
        # Puntaje
        self.score_label = tk.Label(
            results_frame,
            text="Puntaje: 0/8",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.score_label.pack(pady=(0, 15))
        
        # Lista de feedback
        self.feedback_frame = tk.Frame(results_frame, bg='#f0f0f0')
        self.feedback_frame.pack(fill='both', expand=True)
        
        # Scrollbar para feedback
        self.feedback_canvas = tk.Canvas(self.feedback_frame, bg='#f0f0f0', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.feedback_frame, orient="vertical", command=self.feedback_canvas.yview)
        self.scrollable_frame = tk.Frame(self.feedback_canvas, bg='#f0f0f0')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.feedback_canvas.configure(scrollregion=self.feedback_canvas.bbox("all"))
        )
        
        self.feedback_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.feedback_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.feedback_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Botón de verificar
        verify_button = tk.Button(
            main_frame,
            text="Verificar Contraseña",
            command=self.verify_password,
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        verify_button.pack(pady=20)
        
        # Configurar el foco
        self.password_entry.focus()
    
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def on_password_change(self, event=None):
        # Verificar automáticamente mientras el usuario escribe
        self.verify_password()
    
    def verify_password(self):
        password = self.password_var.get()
        strength, score, feedback = self.checker.check_password_strength(password)
        
        # Actualizar etiqueta de fortaleza con color
        strength_colors = {
            "Muy Fuerte": "#27ae60",
            "Fuerte": "#2ecc71", 
            "Media": "#f39c12",
            "Débil": "#e67e22",
            "Muy Débil": "#e74c3c"
        }
        
        self.strength_label.config(
            text=f"Fortaleza: {strength}",
            fg=strength_colors.get(strength, "#2c3e50")
        )
        
        # Actualizar puntaje
        self.score_label.config(text=f"Puntaje: {score}/8")
        
        # Limpiar feedback anterior
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Mostrar nuevo feedback
        for item in feedback:
            color = "#27ae60" if item.startswith("✓") else "#e74c3c"
            label = tk.Label(
                self.scrollable_frame,
                text=item,
                font=("Arial", 10),
                bg='#f0f0f0',
                fg=color,
                anchor='w'
            )
            label.pack(pady=1, padx=5, fill='x')
        
        # Ajustar scroll
        self.feedback_canvas.update_idletasks()
        self.feedback_canvas.configure(scrollregion=self.feedback_canvas.bbox("all"))
    
    def run(self):
        self.root.mainloop()

def command_line_interface():
    """
    Interfaz de línea de comandos para verificar contraseñas
    """
    checker = PasswordStrengthChecker()
    
    print("🔐 Verificador de Fortaleza de Contraseñas")
    print("=" * 50)
    print("Criterios de evaluación:")
    print("• Longitud mínima: 8 caracteres")
    print("• Mayúsculas y minúsculas")
    print("• Números")
    print("• Caracteres especiales")
    print("• Sin espacios")
    print("• Sin patrones comunes")
    print("=" * 50)
    
    while True:
        try:
            password = input("\nIngresa una contraseña (o 'quit' para salir): ")
            
            if password.lower() in ['quit', 'exit', 'salir']:
                print("¡Hasta luego!")
                break
            
            strength, score, feedback = checker.check_password_strength(password)
            
            print(f"\n📊 Resultados:")
            print(f"Fortaleza: {strength}")
            print(f"Puntaje: {score}/8")
            print("\n📋 Detalles:")
            
            for item in feedback:
                print(f"  {item}")
            
            print("\n" + "=" * 50)
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except EOFError:
            print("\n\n¡Hasta luego!")
            break

def main():
    """
    Función principal que determina si usar GUI o CLI
    """
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Modo línea de comandos
        command_line_interface()
    else:
        # Modo GUI (por defecto)
        try:
            app = PasswordGUI()
            app.run()
        except tk.TclError:
            print("Error: No se puede iniciar la interfaz gráfica.")
            print("Usando modo línea de comandos...")
            command_line_interface()

if __name__ == "__main__":
    main()
