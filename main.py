import csv
import sys

if len(sys.argv) != 2:
    raise SystemExit("Укажи путь к таблице: py -3.12 main.py examples/stock.csv")

shortages = []

try:
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as file:
        rows = csv.reader(file, strict=True)
        if next(rows, None) != ["product", "stock", "minimum"]:
            raise ValueError("В первой строке должно быть: product,stock,minimum")

        for row in rows:
            if not row:
                continue

            if len(row) != 3:
                raise ValueError(f"Строка {rows.line_num}: ожидаются три колонки.")

            product, stock_text, minimum_text = row
            try:
                stock = int(stock_text)
                minimum = int(minimum_text)
            except ValueError:
                raise ValueError(
                    f"Строка {rows.line_num}: остаток и минимум должны быть целыми числами."
                ) from None

            if not product.strip() or stock < 0 or minimum < 0:
                raise ValueError(f"Строка {rows.line_num}: проверь название и числа.")

            if stock < minimum:
                shortages.append((product, stock, minimum, minimum - stock))

except (OSError, ValueError, csv.Error) as error:
    raise SystemExit(f"Не удалось прочитать таблицу: {error}") from None

print("ОТЧЁТ ПО ОСТАТКАМ")
if not shortages:
    print("Все остатки в норме")
else:
    print(f"Позиций ниже минимума: {len(shortages)}")
    width = max(5, max(len(product) for product, *_ in shortages))
    print(f"{'Товар':<{width}}  {'Остаток':>7}  {'Минимум':>7}  {'Добавить':>8}")
    for product, stock, minimum, missing in shortages:
        print(f"{product:<{width}}  {stock:>7}  {minimum:>7}  {missing:>8}")