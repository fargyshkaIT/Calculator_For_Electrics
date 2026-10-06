import math
import webview

class Api:
    def py_calc_ohm(self, mode: str, v1_raw: str, v2_raw: str) -> dict:
        try:
            v1 = float(v1_raw)
            v2 = float(v2_raw)

            if math.isnan(v1) or math.isnan(v2) or v2 == 0:
                return {"status": "error", "text": "Ошибка: Проверьте числа"}

            if mode == 'I':
                return {"status": "ok", "text": f"Ток (I) = {v1 / v2:.2f} А"}
            else:
                return {"status": "ok", "text": f"Мощность (P) = {v1 * v2:.2f} Вт"}
        except (ValueError, TypeError, ZeroDivisionError):
            return {"status": "error", "text": "Ошибка: Введите корректные числа"}

    def py_calc_wire(self, p_raw: str, mat: str) -> dict:
        try:
            p = float(p_raw)
            if math.isnan(p) or p <= 0:
                return {"status": "error", "text": "Укажите верную мощность"}

            current = (p * 1000.0) / 220.0

            if mat == "Медь":
                sections = [(1.5, 19), (2.5, 27), (4, 38), (6, 46), (10, 70)]
            else:
                sections = [(2.5, 20), (4, 28), (6, 36), (10, 50)]

            selected = "Нужен кабель > 10 мм²"
            for sect, max_i in sections:
                if current <= max_i:
                    selected = f"Сечение: {sect} мм² (до {max_i} А)"
                    break

            return {"status": "ok", "text": f"Ток: {current:.1f} А\n{selected}"}
        except (ValueError, TypeError):
            return {"status": "error", "text": "Ошибка данных: Введите число"}

api = Api()

window = webview.create_window(
    title='Профессиональный калькулятор электрика',
    url='index.html',
    js_api=api,
    width=1920,
    height=1080,
    resizable=True
)

webview.start()
