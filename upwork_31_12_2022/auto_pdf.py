# %% Setting up dataframe
import pandas as pd
from fpdf import FPDF

# Read file as a dataframe
quality_game_inputs = pd.read_csv("C:/Users/erwin/OneDrive/Desktop/Upwork/quality_game_inputs.csv")

# Convert string values within items as a list
# To be used to parse for images
quality_game_inputs['items'] = quality_game_inputs['items'].str.replace(" ", "")
quality_game_inputs['items'] = quality_game_inputs['items'].str.split(',')

# concat 'qg_item_' to items
def rename_item(lst_of_item):
    result = list(map(lambda x: "qg_item_" + x + ".jpeg", lst_of_item))
    return result

quality_game_inputs['images'] = quality_game_inputs['items'].map(lambda x: rename_item(x))


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', '', 14)

image_filepath = 'C:/Users/erwin/OneDrive/Desktop/Upwork/item_pictures/items/'

def get_images(lst_of_pics):
    for pic in enumerate(lst_of_pics):
        pic = image_filepath + pic[1]
        pdf.image(pic)

for index, row in quality_game_inputs.iterrows():
    pdf.write(5, f"Round Number: {row['round']}\n")
    pdf.write(5, f"Respondent ID: {row['respondent_id']}\n")
    pdf.write(5, f"Delivery Number: {row['delivery_number']}\n")
    pdf.write(5, f"Number of Items to be delivered: {row['n_items_to_deliver']}\n")
    pdf.write(5, f"Items: \n")
    get_images(row['images'])
    pdf.add_page()

pdf.output("example_pdf.pdf", "F")
