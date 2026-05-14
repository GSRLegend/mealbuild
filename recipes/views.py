from django.shortcuts import render

# Create your views here.
recipes = [
    {
        'id': 1, 'name': 'Breakfast Sourdough Sandwich', 'description': 'A sourdough sandwich with steamed egg over avacodo with hot sauce and black pepper sprinkled on.',
        'steps': {'1': 'Bring a pan to medium heat', '2': 'Spray pan with cooking oil', '3': 'Put sourdough slices into toaster set to preferred toast', '4': 'Once pan is hot, crack egg into pan', '5': 'Pour a little bit of water into pan and place a cover over the pan', '6': 'Once sourdough is toasted, carve out avacodo and spread it onto one slice of bread', '7': 'Take egg out of pan and lay it over the avacodo', '8': 'Sprinkle hot sauce and pepper over egg', '9': 'Put other slice on top', },
        'macros': {'fat': '36.2g', 'protein': '18g', 'carb': '54.5g', 'cholesterol': '186mg', 'sodium': '595mg', },
        'vitamins': {'alpha_carotene': '49.3μg', 'beta_carotene': '149μg', 'choline': '182mg', 'folate': '267.3μg', 'lycopene': '1μg', 'niacin': '6.1mg', 'pantothenic_acid': '4.4mg', 'retinol': '80μg', 'riboflavin': '0.8mg', 'vitamin_A_IU': '606iu', 'vitamin_A': '96.4μg', 'vitamin_B12': '0.4μg', 'vitamin_B6': '1.2mg', 'vitamin_C': '24mg', 'vitamin_D_iu': '41iu', 'vitamin_D': '1μg', 'vitamin_D2': '', 'vitamin_D3': '1μg', 'vitamin_E': '5.2mg', 'vitamin_K': '52.7μg', },
        'minerals': {'caffeine': '0mg', 'copper': '0.6mg', 'flouride': '17μg', 'magnesium': '95.2mg', 'manganese': '1.7mg', 'phosphorus': '282mg', 'selenium': '34.3μg', 'theobromine': '0mg', 'zinc': '3.1mg', 'potassium': '1211mg', 'calcium': '113.4mg', 'iron': '6mg', },
        'sugars': {'sugar': '4.3g', 'sucrose': '0.1g', 'glucose': '1.5g', 'fructose': '0.5g', 'lactose': '0g', 'maltose': '2g', 'galactose': '0.2g', 'starch': '28.2g', },
        'fats': {'saturated_fats': '6.4g', 'monounsaturated_fats': '22.2g', 'polyunsaturated_fats': '6.1g', 'trans_fats': '0g', },
        'fatty_acids': {'omega_3': '0.3g', 'omega_6': '2g', 'ala': '0.2g', 'dha': '0g', 'epa': '0g', 'dpa': '0g', },
        'amino_acids': {'alanine': '0.8g', 'arginine': '0.8g', 'aspartic_acid': '1.9g', 'cystine': '0.4g', "glutamic_acid": '4.1g', 'glycine': '0.6g', 'histidine': '0.4g', 'hydroxyproline': '', 'isoleucine': '0.7g', 'leucine': '1.7g', 'lysine': '1g', 'methionine': '0.4g', 'phenylalanine': '0.8g', 'proline': '1.6g', 'serine': '1g', 'threonine': '0.6g', 'tryptophan': '0.3g', 'tyrosine': '0.4g', 'valine': '0.9g', },
        'serving_size': '1 sandwich',
        'calories': '585',
        'source': '',
    },
]
def index(request):
    template_data = {}
    template_data['title'] = 'Recipes'
    template_data['recipes'] = recipes
    return render(request, 'recipes/index.html', {'template_data': template_data})
def show(request, id):
    recipe = recipes[id - 1]
    template_data = {}
    template_data['title'] = recipe['name']
    template_data['recipe'] = recipe
    return render(request, 'recipes/show.html', {'template_data': template_data})