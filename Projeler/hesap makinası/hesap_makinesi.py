import tkinter as tk

class HesapMakinasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinası")

        # Text widget oluşturma
        self.text = tk.Text(self.root, height=2, width=30, font=("Helvetica", 16))
        self.text.pack(pady=10)

        # Hesapla butonu
        self.hesap_button = tk.Button(self.root, text="Hesapla", command=self.calculate)
        self.hesap_button.pack(pady=5)

        # Sonucu göstermek için etiket
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            # Text widget'ından veriyi al
            expression = self.text.get("1.0", tk.END).strip()
            # İfadeyi değerlendirme
            result = eval(expression)
            # Sonucu gösterme
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            # Hata durumunda mesaj gösterme
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HesapMakinasi(root)
    root.mainloop()
