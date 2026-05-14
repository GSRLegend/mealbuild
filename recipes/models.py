from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    serving_size = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='recipe_images/',
        blank=True,
        null=True
    )
    source = models.URLField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  
    def __str__(self):
        return str(self.id) + ' - ' + self.name

class RecipeSteps(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='steps'
    )
    step_number = models.PositiveIntegerField()
    instruction = models.TextField()
    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"{self.recipe.name} - Step {self.step_number}"

class Ingredient:
    name = models.CharField(
        max_lenght=100,
        unique=True
    )

    #Macros per 100g
    #-------------------------------------
    calories = models.FloatField(default=0)
    fat = models.FloatField(default=0)                  #g
    protein = models.FloatField(default=0)              #g
    carbohydrates = models.FloatField(default=0)        #g
    cholesterol = models.FloatField(default=0)          #mg
    sodium = models.FloatField(default=0)               #mg

    #Vitamins per 100g
    #-------------------------------------
    alpha_carotene = models.FloatField(default=0)       #μg
    beta_carotene = models.FloatField(default=0)        #μg
    choline = models.FloatField(default=0)              #mg
    folate = models.FloatField(default=0)               #μg
    lycopene = models.FloatField(default=0)             #μg
    niacin = models.FloatField(default=0)               #mg
    pantothenic_acid = models.FloatField(default=0)     #mg
    retinol = models.FloatField(default=0)              #μg
    riboflavin = models.FloatField(default=0)           #mg
    vitamin_A_IU = models.FloatField(default=0)         #IU
    vitamin_A = models.FloatField(default=0)            #μg
    vitamin_B12 = models.FloatField(default=0)          #μg
    vitamin_B6 = models.FloatField(default=0)           #mg
    vitamin_C = models.FloatField(default=0)            #mg
    vitamin_D_IU = models.FloatField(default=0)         #IU
    vitamin_D = models.FloatField(default=0)            #μg
    vitamin_D2 = models.FloatField(default=0)           #μg
    vitamin_D3 = models.FloatField(default=0)           #μg
    vitamin_E = models.FloatField(default=0)            #mg
    vitamin_K = models.FloatField(default=0)            #μg

    #Minerals per 100g
    #-------------------------------------
    caffeine = models.FloatField(default=0)             #mg
    copper = models.FloatField(default=0)               #mg
    flouride = models.FloatField(default=0)             #μg
    magnesium = models.FloatField(default=0)            #mg
    manganese = models.FloatField(default=0)            #mg
    phosphorus = models.FloatField(default=0)           #mg
    selenium = models.FloatField(default=0)             #μg
    theobromine = models.FloatField(default=0)          #mg
    zinc = models.FloatField(default=0)                 #mg
    potassium = models.FloatField(default=0)            #mg
    calcium = models.FloatField(default=0)              #mg
    iron = models.FloatField(default=0)                 #mg

    #Sugars per 100g
    #-------------------------------------
    sugar = models.FloatField(default=0)                #g
    sucrose = models.FloatField(default=0)              #g
    glucose = models.FloatField(default=0)              #g
    fructose = models.FloatField(default=0)             #g
    lactose = models.FloatField(default=0)              #g
    maltose = models.FloatField(default=0)              #g
    galactose = models.FloatField(default=0)            #g
    starch = models.FloatField(default=0)               #g

    #Fats per 100g
    #-------------------------------------
    saturated_fats = models.FloatField(default=0)       #g
    monosaturated_fats = models.FloatField(default=0)   #g
    polyunsaturated_fats = models.FloatField(default=0) #g
    trans_fats = models.FloatField(default=0)           #g

    #Fatty Acids per 100g
    #-------------------------------------
    omega_3 = models.FloatField(default=0)              #g  
    omega_6 = models.FloatField(default=0)              #g
    ALA = models.FloatField(default=0)                  #g
    DHA = models.FloatField(default=0)                  #g
    EPA = models.FloatField(default=0)                  #g
    DPA = models.FloatField(default=0)                  #g

    #Amino Acids per 100g
    #-------------------------------------
    alanine = models.FloatField(default=0)              #g
    arginine = models.FloatField(default=0)             #g
    aspartic_acid = models.FloatField(default=0)        #g
    cystine = models.FloatField(default=0)              #g
    glutamic_acid = models.FloatField(default=0)        #g
    glycine = models.FloatField(default=0)              #g
    histidine = models.FloatField(default=0)            #g
    hydroxyproline = models.FloatField(default=0)       #g
    isoleucine = models.FloatField(default=0)           #g
    leucine = models.FloatField(default=0)              #g
    lysine = models.FloatField(default=0)               #g
    methionine = models.FloatField(default=0)           #g
    phenylalanine = models.FloatField(default=0)        #g
    proline = models.FloatField(default=0)              #g
    serine = models.FloatField(default=0)               #g
    threonine = models.FloatField(default=0)            #g
    tryptophan = models.FloatField(default=0)           #g
    tyrosine = models.FloatField(default=0)             #g
    valine = models.FloatField(default=0)               #g

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    amount = models.CharField(
        max_length=20,
        default='g'
    )
    class Meta:
        unique_together = ['recipe', 'ingredient']
    
    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name}"
    
class Nutrition(models.Model):
    recipe = models.OneToOneField(
        Recipe,
        on_delete=models.CASCADE,
        related_name='nutrition'
    )
    
    #Macros per serving
    #-------------------------------------
    calories = models.FloatField(default=0)
    fat = models.FloatField(default=0)                  #g
    protein = models.FloatField(default=0)              #g
    carbohydrates = models.FloatField(default=0)        #g
    cholesterol = models.FloatField(default=0)          #mg
    sodium = models.FloatField(default=0)               #mg

    #Vitamins per serving
    #-------------------------------------
    alpha_carotene = models.FloatField(default=0)       #μg
    beta_carotene = models.FloatField(default=0)        #μg
    choline = models.FloatField(default=0)              #mg
    folate = models.FloatField(default=0)               #μg
    lycopene = models.FloatField(default=0)             #μg
    niacin = models.FloatField(default=0)               #mg
    pantothenic_acid = models.FloatField(default=0)     #mg
    retinol = models.FloatField(default=0)              #μg
    riboflavin = models.FloatField(default=0)           #mg
    vitamin_A_IU = models.FloatField(default=0)         #IU
    vitamin_A = models.FloatField(default=0)            #μg
    vitamin_B12 = models.FloatField(default=0)          #μg
    vitamin_B6 = models.FloatField(default=0)           #mg
    vitamin_C = models.FloatField(default=0)            #mg
    vitamin_D_IU = models.FloatField(default=0)         #IU
    vitamin_D = models.FloatField(default=0)            #μg
    vitamin_D2 = models.FloatField(default=0)           #μg
    vitamin_D3 = models.FloatField(default=0)           #μg
    vitamin_E = models.FloatField(default=0)            #mg
    vitamin_K = models.FloatField(default=0)            #μg

    #Minerals per serving
    #-------------------------------------
    caffeine = models.FloatField(default=0)             #mg
    copper = models.FloatField(default=0)               #mg
    flouride = models.FloatField(default=0)             #μg
    magnesium = models.FloatField(default=0)            #mg
    manganese = models.FloatField(default=0)            #mg
    phosphorus = models.FloatField(default=0)           #mg
    selenium = models.FloatField(default=0)             #μg
    theobromine = models.FloatField(default=0)          #mg
    zinc = models.FloatField(default=0)                 #mg
    potassium = models.FloatField(default=0)            #mg
    calcium = models.FloatField(default=0)              #mg
    iron = models.FloatField(default=0)                 #mg

    #Sugars per serving
    #-------------------------------------
    sugar = models.FloatField(default=0)                #g
    sucrose = models.FloatField(default=0)              #g
    glucose = models.FloatField(default=0)              #g
    fructose = models.FloatField(default=0)             #g
    lactose = models.FloatField(default=0)              #g
    maltose = models.FloatField(default=0)              #g
    galactose = models.FloatField(default=0)            #g
    starch = models.FloatField(default=0)               #g

    #Fats per serving
    #-------------------------------------
    saturated_fats = models.FloatField(default=0)       #g
    monosaturated_fats = models.FloatField(default=0)   #g
    polyunsaturated_fats = models.FloatField(default=0) #g
    trans_fats = models.FloatField(default=0)           #g

    #Fatty Acids per serving
    #-------------------------------------
    omega_3 = models.FloatField(default=0)              #g  
    omega_6 = models.FloatField(default=0)              #g
    ALA = models.FloatField(default=0)                  #g
    DHA = models.FloatField(default=0)                  #g
    EPA = models.FloatField(default=0)                  #g
    DPA = models.FloatField(default=0)                  #g

    #Amino Acids per serving
    #-------------------------------------
    alanine = models.FloatField(default=0)              #g
    arginine = models.FloatField(default=0)             #g
    aspartic_acid = models.FloatField(default=0)        #g
    cystine = models.FloatField(default=0)              #g
    glutamic_acid = models.FloatField(default=0)        #g
    glycine = models.FloatField(default=0)              #g
    histidine = models.FloatField(default=0)            #g
    hydroxyproline = models.FloatField(default=0)       #g
    isoleucine = models.FloatField(default=0)           #g
    leucine = models.FloatField(default=0)              #g
    lysine = models.FloatField(default=0)               #g
    methionine = models.FloatField(default=0)           #g
    phenylalanine = models.FloatField(default=0)        #g
    proline = models.FloatField(default=0)              #g
    serine = models.FloatField(default=0)               #g
    threonine = models.FloatField(default=0)            #g
    tryptophan = models.FloatField(default=0)           #g
    tyrosine = models.FloatField(default=0)             #g
    valine = models.FloatField(default=0)               #g

    def __str__(self):
        return f"{self.recipe.name} Nutrition"