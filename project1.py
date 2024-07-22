from datetime import datetime

class Calculator:

    def __init__(self, options):
        self.options = options
        self.max_width = len(max(self.options, key=len))

    def print_options(self):
        for option in self.options:
            padding = " " * (self.max_width - len(option))
            print(f"║ {option}{padding} ║")

    def draw_frame(self):
        print(f"{' ' * (int(self.max_width/2 - 2))}HESAPLAYICI")
        top_bottom = "═" * (self.max_width + 2)
        print(f"╔{top_bottom}╗")
        print(f"║ {' ' * self.max_width} ║")
        self.print_options()
        print(f"║ {' ' * self.max_width} ║")
        print(f"╚{top_bottom}╝")

    def get_selection(self):
        while True:
            try:
                selection = int(input("Bir seçenek seçin: "))
                if selection == 0:
                    print("Ana menüye dönülüyor...")
                    return None
                elif selection > len(self.options) - 1:
                    print("Geçersiz seçenek!")
                else:
                    print(self.options[selection - 1], "seçildi.")
                    return selection
            except ValueError:
                print("Lütfen bir sayı girin.")

    def perform_calculation(self, operation):
        try:
            if operation == 1:
                num1 = float(input("İlk sayıyı girin: "))
                op = input('Yapmak istediğiniz işlemi girin (+, -, *, /): ')
                num2 = float(input("İkinci sayıyı girin: "))
                if op == '+':
                    result = num1 + num2
                    print(f"Sonuç: {result}")
                elif op == '-':
                    result = num1 - num2
                    print(f"Sonuç: {result}")
                elif op == '*':
                    result = num1 * num2
                    print(f"Sonuç: {result}")
                elif op == '/':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Sonuç: {result}")
                    else:
                        result = "Hata: Sıfıra bölme hatası!"
                else:
                    print("Geçersiz işlem!")
            elif operation == 2:
                edge = float(input('Karenin bir kenar uzunluğunu girin: '))
                perimeter = edge * 4
                area = edge**2
                print(f"Karenin Çevresi: {perimeter} \nKarenin Alanı: {area}")
            elif operation == 3:
                base = float(input("Üçgenin taban uzunluğunu girin: "))
                edge1 = float(input("Üçgenin bir kenar uzunluğunu girin: "))
                edge2 = float(input("Üçgenin diğer kenar uzunluğunu girin"))
                height = float(input("Üçgenin yüksekliğini girin: "))
                area = 0.5 * base * height
                perimeter = base + edge1 + edge2
                print(f"Üçgenin Alanı: {area} \nÜçgenin Çevresi {perimeter}")
            elif operation == 4:
                radius = float(input("Dairenin yarıçapını girin: "))
                pi = 3.14
                area = pi * radius**2
                perimeter = 2 * pi * radius
                print(
                    f"Dairenin Alanı: {area} \nDairenin Çevresi: {perimeter}")
            elif operation == 5:
                user_year = int(input("Doğum yılınızı girin: "))
                current_year = datetime.now().year
                age = current_year - user_year
                print(f"Yaşınız: {age} ")
            elif operation == 6:
                first_grade = float(input("İlk sınav notunuzu girin: "))
                second_grade = float(input("İkinci sınav notunuzu girin: "))
                performance_grade = float(input("Performans notunuzu girin: "))
                avarage_grade = (first_grade + second_grade +
                                 performance_grade) / 3
                print(f"Ortalama notunuz: {avarage_grade}")
            elif operation == 7:
                kg = float(input(f"Kilonuzu girin (kg): "))
                m = float(input(f"Boyunuzu girin (m): "))
                bmi = kg / (m**2)
                print(f"Vücut kitle indeksiniz: {bmi}")
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")

    def run(self):
        while True:
            self.draw_frame()
            selection = self.get_selection()
            if selection is None:
                break
            elif 1 <= selection <= len(self.options):
                self.perform_calculation(selection)


def run():
    options = [
        "1-Basit Hesap Makinesi",
        "2-Karenin Çevresi ve Alanı",
        "3-Üçgenin Çevresi ve Alanı",
        "4-Dairenin Çevresi ve Alanı",
        "5-Yaş Hesaplama",
        "6-Ortalama Hesaplayıcı",
        "7-BMI -Vücut Kitle İndeksi- Hesaplayıcı",
        "0-Ana Menü",
    ]
    calculator = Calculator(options)
    calculator.run()


if __name__ == '__main__':
    run()
