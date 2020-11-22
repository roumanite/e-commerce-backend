from product.models import Category

# Men's Wear
mens_wear = Category.objects.create(name="Men's Wear")

mens_jeans = Category.objects.create(name="Jeans", parent=mens_wear)
Category.objects.create(name="Skinny Fit", parent=mens_jeans)
Category.objects.create(name="Slim Fit", parent=mens_jeans)
Category.objects.create(name="Regular Fit", parent=mens_jeans)

Category.objects.create(name="Pants", parent=mens_wear)

# Women's Apparel
womens_apparel = Category.objects.create(name="Women's Apparel")

dresses = Category.objects.create(name="Dresses", parent=womens_apparel)
Category.objects.create(name="Mini Dresses", parent=dresses)
Category.objects.create(name="Party Dresses", parent=dresses)

skirts = Category.objects.create(name="Mini Skirts", parent=womens_apparel)
Category.objects.create(name="Mini Skirts", parent=skirts)
Category.objects.create(name="Maxi Skirts", parent=skirts)
Category.objects.create(name="Midi Skirts", parent=skirts)

modest_wear = Category.objects.create(name="Modest Wear", parent=womens_apparel)
Category.objects.create(name="Cheongsam", parent=modest_wear)
Category.objects.create(name="Jubah", parent=modest_wear)
Category.objects.create(name="Sari", parent=modest_wear)
Category.objects.create(name="Hijab", parent=modest_wear)
Category.objects.create(name="Sarong & Kain Batik", parent=modest_wear)
Category.objects.create(name="Muslimah Pants", parent=modest_wear)
Category.objects.create(name="Muslimah Skirts", parent=modest_wear)
Category.objects.create(name="Telekung", parent=modest_wear)
Category.objects.create(name="Muslimah Blouse", parent=modest_wear)

occasion_wear = Category.objects.create(name="Occasion wear", parent=womens_apparel)
Category.objects.create(name="Prom", parent=occasion_wear)
Category.objects.create(name="Wedding", parent=occasion_wear)
Category.objects.create(name="Cosplay & costumes", parent=occasion_wear)

# Beauty & Personal Care
bp_care = Category.objects.create(name="Beauty & Personal Care")

skincare = Category.objects.create(name="Skincare", parent=bp_care)
Category.objects.create(name="Cleanser", parent=skincare)
Category.objects.create(name="Mask", parent=skincare)
Category.objects.create(name="Moisturizer", parent=skincare)
Category.objects.create(name="Exfoliators & Scrubs", parent=skincare)

makeup = Category.objects.create(name="Makeup", parent=bp_care)
Category.objects.create(name="Blusher", parent=makeup)
Category.objects.create(name="Contour & Highlight", parent=makeup)
Category.objects.create(name="Eye", parent=makeup)
Category.objects.create(name="Foundation", parent=makeup)

# Hobbies & Books
hobbies_books = Category.objects.create(name="Hobbies & Books")

kits = Category.objects.create(name="Figures & Model Kits", parent=hobbies_books)
Category.objects.create(name="Manga & Anime Figures", parent=kits)
Category.objects.create(name="Action Figures", parent=kits)
Category.objects.create(name="DIY Figure, Model Kits & Accessories", parent=kits)
Category.objects.create(name="Vehicle Models & Diecast", parent=kits)

books = Category.objects.create(name="Books", parent=hobbies_books)
Category.objects.create(name="Religious Books", parent=books)
Category.objects.create(name="Chinese Books", parent=books)
Category.objects.create(name="Cooking", parent=books)
Category.objects.create(name="Magazines", parent=books)
