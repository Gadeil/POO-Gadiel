from tkinter import messagebox

class logic:
    def __init__(self):
        pass 

    def roman2int(self, romval):
        if romval == "VX" or romval == "IIII" or romval == "VVVV" or romval == "XXXX" or romval == "LLLL" or romval == "CCCC" or romval == "DDDD" or romval == "MMMM" or romval == "VV" :
            messagebox.showinfo("resultado", "no es un numero romano")
        else:
            romanos = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            total = 0
            prev = 0
            for letra in romval[::-1]:
                valor = romanos[letra]
                total += valor if valor >= prev else -valor
                prev = valor
            messagebox.showinfo("resultado", str(total))
            
    def intToRoman(self, num):
        if num >= 50:
            messagebox.showinfo("resultado", "fuera de rango")
        else:
            m = ["", "M", "MM", "MMM"]
            c = ["", "C", "CC", "CCC", "CD", "D",
                "DC", "DCC", "DCCC", "CM "]
            x = ["", "X", "XX", "XXX", "XL", "L",
                "LX", "LXX", "LXXX", "XC"]
            i = ["", "I", "II", "III", "IV", "V",
                "VI", "VII", "VIII", "IX"]

            miles = m[num // 1000]
            cientos = c[(num % 1000) // 100]
            decenas = x[(num % 100) // 10]
            unidad = i[num % 10]
        
            respuesta = (miles + cientos +decenas + unidad)
        
            messagebox.showinfo("resultado", str(respuesta))
