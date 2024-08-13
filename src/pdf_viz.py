import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

file_name = "Redrex - Fatura (2)"
path = os.path.abspath(f"src/files/pdf/redrex/{file_name}.pdf")

tables = camelot.read_pdf(path,
                          flavor='stream',
                          table_areas= ['70, 560,498,279'],
                          columns= ['70, 105, 160, 230, 285, 340, 380, 446'],
                          strip_text=".\n",
                          pages="1-end",
                          password="161"
                          )
print(tables[0].parsing_report)

# camelot.plot(tables[0], kind="contour")

# plt.show()

print(tables[0].df)
print("Waiting for work")