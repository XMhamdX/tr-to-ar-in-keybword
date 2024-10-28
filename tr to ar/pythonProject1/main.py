import keyboard
from pynput import keyboard as kb
import time
import sys
from threading import Thread

# قاموس تحويل الحروف التركية إلى العربية (لوحة مفاتيح 101)
turkish_to_arabic = {
    # الصف العلوي
    'q': 'ض',
    'w': 'ص',
    'e': 'ث',
    'r': 'ق',
    't': 'ف',
    'y': 'غ',
    'u': 'ع',
    'ı': 'ه',
    'o': 'خ',
    'p': 'ح',
    'ğ': 'چ',
    'ü': 'د',

    # الصف الأوسط
    'a': 'ش',
    's': 'س',
    'd': 'ي',
    'f': 'ب',
    'g': 'ل',
    'h': 'ا',
    'j': 'ت',
    'k': 'ن',
    'l': 'م',
    'ş': 'ك',
    'i': 'ط',

    # الصف السفلي
    'z': 'ئ',
    'x': 'ء',
    'c': 'ؤ',
    'v': 'ر',
    'b': 'لا',
    'n': 'ى',
    'm': 'ة',
    'ö': 'و',
    'ç': 'ز',
    '.': 'ظ'
}


class KeyboardConverter:
    def __init__(self):
        self.active = False
        self.controller = kb.Controller()
        self.last_key = None

    def toggle_conversion(self):
        self.active = not self.active
        print(f"التحويل {'مفعل' if self.active else 'معطل'}")

    def on_press(self, key):
        try:
            if not self.active:
                return True

            # تجاهل مفتاح التحكم
            if key == kb.Key.ctrl:
                return True

            # تحويل الحرف إذا كان موجوداً في القاموس
            char = key.char.lower() if hasattr(key, 'char') else None
            if char in turkish_to_arabic:
                # حذف الحرف الأصلي
                keyboard.press('backspace')
                keyboard.release('backspace')
                # كتابة الحرف العربي
                self.controller.type(turkish_to_arabic[char])

        except AttributeError:
            pass
        return True


def main():
    converter = KeyboardConverter()

    # تسجيل اختصار Ctrl+K للتبديل
    keyboard.add_hotkey('ctrl+k', converter.toggle_conversion)

    # بدء مراقبة لوحة المفاتيح
    with kb.Listener(on_press=converter.on_press) as listener:
        print("البرنامج يعمل. اضغط Ctrl+K للتبديل بين وضعي التحويل")
        listener.join()


if __name__ == "__main__":
    main()