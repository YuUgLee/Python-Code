import pandas as pd
import openpyxl
from openpyxl import load_workbook
# Select excel workbook
wb = load_workbook(filename='Inventory.xlsx')
sheet = wb.active

df = pd.read_excel('Inventory.xlsx')
df = pd.DataFrame(df, columns = ["Name","Location","Part Number","Quantity","Decryption","Note"])