# Age-specific recommendations for symptoms
# This module provides tailored recommendations based on patient age and symptoms

def get_age_category(age):
    """Categorize age into appropriate groups"""
    if age is None:
        return 'adult'
    try:
        age_val = int(age)
        if age_val < 5:
            return 'infant'  # 0-4 years
        elif age_val < 12:
            return 'child'   # 5-11 years
        elif age_val < 18:
            return 'teen'    # 12-17 years
        elif age_val < 60:
            return 'adult'   # 18-59 years
        else:
            return 'elderly' # 60+ years
    except:
        return 'adult'


AGE_SPECIFIC_SYMPTOMS = {
    'fever': {
        'infant': {
            'medicines': ['Paracetamol syrup 125mg/5ml — 5ml every 4-6 hours (pediatrician approval)', 'Cool sponging every 15 mins if >38.5°C'],
            'medicine_timing': 'Only under doctor supervision; max 4 doses/day',
            'diet': ['Breast milk (if nursing)', 'Warm water', 'Diluted fruit juice', 'Soft mashed fruits'],
            'drinks': ['Breast milk only', 'Boiled water (cooled)', 'ORS solution (every 30 mins)', 'Diluted apple juice'],
            'lifestyle': ['Cool room', 'Loose cotton clothes', 'Sponge bath with lukewarm water', 'Frequent monitoring'],
            'advice': 'Fever in infants needs careful monitoring. Keep hydrated, avoid medications without doctor approval.'
        },
        'child': {
            'medicines': ['Paracetamol syrup 250mg/5ml — 10ml every 6 hours', 'OR Nimesulide suspension 50mg/5ml — 5ml every 8 hours', 'Cool water sponging if fever >38.5°C'],
            'medicine_timing': 'Every 6-8 hours; max 4 doses/day; with food',
            'diet': ['Soft rice with dal', 'Mashed potato with ghee', 'Banana', 'Papaya', 'Egg curry (mild)', 'Avoid fried/spicy'],
            'drinks': ['Warm water with honey', 'Fresh juice (diluted 50%)', 'Milk with turmeric', 'ORS solution', 'Coconut water'],
            'lifestyle': ['Rest 2-3 hours daily', 'Loose cotton clothes', 'Cool room', 'Light indoor games when better'],
            'advice': 'Monitor temperature closely, keep well hydrated. Give age-appropriate medicines only.'
        },
        'teen': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 6 hours', 'OR Dolo 500mg — 1-2 tablets every 6 hours', 'Nimesulide 100mg — 1 tablet every 8 hours if fever >101°F'],
            'medicine_timing': 'Every 6-8 hours with food; max 3g/day',
            'diet': ['Khichdi', 'Moong dal soup', 'Chicken broth', 'Soft fruits', 'Boiled rice with curd', 'Avoid oily/spicy'],
            'drinks': ['Warm water with honey + lemon', 'Ginger-turmeric tea', 'Coconut water', 'ORS solution', 'Milk with turmeric'],
            'lifestyle': ['Complete bed rest', 'Cold compress on forehead', 'Cotton clothes', 'Room ventilation'],
            'advice': 'Stay hydrated, rest well. Monitor for any complications.'
        },
        'adult': {
            'medicines': ['Paracetamol 500mg — 1-2 tablets every 6 hours', 'OR Dolo 500mg — 1-2 tablets every 6 hours with food', 'Nimesulide 100mg — 1 tablet every 8 hours if fever >101°F'],
            'medicine_timing': 'Every 6 hours after meals; max 3g/day',
            'diet': ['Khichdi', 'Moong dal soup', 'Chicken broth', 'Boiled rice with curd', 'Soft fruits', 'Avoid street food/fried'],
            'drinks': ['Warm water with honey + lemon', 'Ginger-turmeric tea', 'Coconut water', 'ORS solution', 'Milk with turmeric'],
            'lifestyle': ['Complete bed rest', 'Cold compress every 2 hours', 'Cotton clothes', 'Sponge bath if >103°F'],
            'advice': 'Monitor temperature closely, keep hydrated, avoid NSAIDs until dengue excluded.'
        },
        'elderly': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 6 hours (lower dose)', 'NO NSAIDs — use paracetamol only'],
            'medicine_timing': 'Every 6-8 hours with food; max 2g/day; check BP meds interaction',
            'diet': ['Soft khichdi', 'Warm dal', 'Mild chicken broth', 'Soft rice with dal', 'Mashed vegetables', 'Avoid hard/fried'],
            'drinks': ['Warm water with honey + lemon', 'Herbal tea (gentle)', 'Milk with turmeric (if tolerated)', 'ORS solution', 'Coconut water (limited)'],
            'lifestyle': ['Complete bed rest for 3-5 days', 'BP/pulse monitoring', 'Gentle room temperature', 'Avoid sudden movements'],
            'advice': 'Elderly more susceptible to complications. Monitor closely, maintain hydration, avoid NSAIDs.'
        }
    },
    'headache': {
        'infant': {
            'medicines': ['Paracetamol syrup — 5ml (consult pediatrician)', 'NO adult medicines'],
            'medicine_timing': 'Only with doctor approval',
            'diet': ['Breast milk', 'Warm mashed food', 'Soft diet'],
            'drinks': ['Breast milk or warm water'],
            'lifestyle': ['Dark, quiet room', 'Gentle rocking', 'Comfortable position'],
            'advice': 'Crying may indicate headache. Ensure hydration and comfort.'
        },
        'child': {
            'medicines': ['Paracetamol syrup 250mg/5ml — 10ml every 6 hours', 'Cool water compress on forehead'],
            'medicine_timing': 'Every 6 hours; max 4 doses/day',
            'diet': ['Plain rice', 'Toast', 'Soft fruits', 'Banana', 'Mild dal', 'Avoid chocolates/spicy'],
            'drinks': ['Warm water with honey', 'Fresh juice (diluted)', 'Milk with honey', 'Coconut water'],
            'lifestyle': ['Rest in dark room', 'Ice pack on forehead (10 mins)', 'Sleep 8-10 hours', 'Avoid stress/noise'],
            'advice': 'Rest in cool room, hydration is key. Simple headaches usually resolve with rest.'
        },
        'teen': {
            'medicines': ['Aspirin 500mg — 1 tablet every 6 hours', 'Paracetamol 500mg — 1 tablet every 6 hours', 'Take with food'],
            'medicine_timing': 'Every 6 hours; max 6 tablets/day; with food',
            'diet': ['Plain rice', 'Toast', 'Eggs', 'Yogurt', 'Soft fruits', 'Avoid tea/coffee/chocolate'],
            'drinks': ['Ginger-lemon water', 'Tulsi tea', 'Milk with turmeric', 'Coconut water', 'Plain water (3-4L daily)'],
            'lifestyle': ['Rest in dark room', 'Ice pack (15-20 mins)', 'Neck massage with warm oil', 'Deep breathing', 'Sleep 8 hours'],
            'advice': 'Headache often from stress or dehydration. Rest in dark room, stay hydrated.'
        },
        'adult': {
            'medicines': ['Aspirin 500mg — 1 tablet every 6 hours', 'Ibuprofen 400mg — 1-2 tablets every 6 hours', 'Sumatriptan 50mg for migraine (prescription)'],
            'medicine_timing': 'Every 6 hours with food; max 6 tablets/day',
            'diet': ['Plain rice', 'Toast', 'Eggs', 'Yogurt', 'Soft fruits', 'Avoid tea/coffee/chocolate/cheese'],
            'drinks': ['Ginger-lemon water', 'Tulsi tea', 'Milk with turmeric', 'Coconut water', 'Plain water (3-4L daily)'],
            'lifestyle': ['Rest in dark room', 'Ice pack (15-20 mins)', 'Neck massage', 'Deep breathing', 'Sleep 7-8 hours'],
            'advice': 'Headache often from dehydration or stress. Rest in dark room, stay hydrated.'
        },
        'elderly': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 8 hours (lower dose)', 'NO NSAIDs — increases stroke risk', 'Check BP immediately'],
            'medicine_timing': 'Every 8 hours with food; max 2g/day; no other pain meds',
            'diet': ['Soft rice', 'Mild dal', 'Vegetables (cooked)', 'Soft fruits', 'Avoid hard/fried'],
            'drinks': ['Warm water with honey (limited)', 'Mild tea (no caffeine)', 'Milk (if tolerated)', 'Water (2-3L daily)'],
            'lifestyle': ['Rest in cool room', 'Gentle position', 'Avoid sudden movements', 'Regular BP monitoring', 'Sleep 7-8 hours'],
            'advice': 'Headache in elderly often related to BP or medications. Monitor closely, avoid sudden movements.'
        }
    },
    'cough': {
        'infant': {
            'medicines': ['Honey — 1 tsp (for infants >1 year only)', 'Vicks VapoRub on chest (limited)', 'Doctor approval essential'],
            'medicine_timing': 'Consult pediatrician',
            'diet': ['Breast milk', 'Warm water', 'Mashed fruits', 'Soft diet'],
            'drinks': ['Breast milk', 'Warm water', 'Diluted juice'],
            'lifestyle': ['Humidifier in room', 'Elevate head', 'Warm room', 'Frequent monitoring'],
            'advice': 'Cough in infants needs monitoring. NO cough syrups without doctor approval.'
        },
        'child': {
            'medicines': ['Benadryl cough syrup — 5ml every 6 hours', 'Honey — 1 tsp 2-3 times daily (natural)', 'Avoid adult syrups'],
            'medicine_timing': 'Every 6 hours after meals',
            'diet': ['Light chicken soup', 'Khichdi', 'Soft vegetables', 'Banana', 'Papaya', 'Avoid dairy (increases mucus)'],
            'drinks': ['Warm water with honey', 'Ginger tea', 'Warm milk (limited)', 'Herbal tea with honey'],
            'lifestyle': ['Head elevated 2-3 pillows', 'Humidifier', 'Avoid dusty areas', 'Gargle salt water', 'Sleep well'],
            'advice': 'Stay hydrated, elevate head. Avoid smoke and pollution.'
        },
        'teen': {
            'medicines': ['Benadryl cough syrup — 2 tsp every 6 hours', 'Ascoril syrup — 2 tsp every 6 hours', 'Strepsils lozenges 1 every 4 hours'],
            'medicine_timing': 'Every 6 hours after meals',
            'diet': ['Chicken soup with garlic', 'Khichdi', 'Turmeric rice', 'Soft vegetables', 'Banana', 'Papaya', 'Almonds soaked'],
            'drinks': ['Warm turmeric milk 2-3x daily', 'Ginger tea with basil', 'Warm lemon water + honey', 'Herbal tea'],
            'lifestyle': ['Head elevated 3-4 pillows', 'Humidifier daily', 'Avoid pollution/smoke', 'Gargle salt water 2-3x daily', 'Vitamin C foods'],
            'advice': 'Stay hydrated, avoid air pollution. Elevate head while sleeping.'
        },
        'adult': {
            'medicines': ['Benadryl cough syrup — 2 tsp every 6 hours', 'Ascoril syrup — 2 tsp every 6 hours', 'Honey — 1 tsp mixed in warm water'],
            'medicine_timing': 'Every 6 hours after meals; complete course even if better',
            'diet': ['Chicken soup with garlic/ginger', 'Khichdi', 'Turmeric rice', 'Soft vegetables', 'Banana', 'Papaya', 'Almonds soaked'],
            'drinks': ['Warm turmeric milk (Haldi doodh) 2-3x daily', 'Ginger tea with 5-6 basil leaves', 'Warm lemon water + honey', 'Herbal tea with black pepper'],
            'lifestyle': ['Sleep head elevated 3-4 pillows', 'Humidifier or steam daily', 'Avoid dusty/smoky areas', 'Gargle salt water 2-3x daily', 'Vitamin C foods'],
            'advice': 'Stay hydrated, avoid pollution and smoke. Elevate head while sleeping.'
        },
        'elderly': {
            'medicines': ['Benadryl cough syrup — 1-2 tsp every 6 hours (lower dose)', 'Honey — 1 tsp (natural, safe)', 'NO excessive syrups — consult doctor'],
            'medicine_timing': 'Every 6-8 hours; gentle formulations only',
            'diet': ['Warm chicken broth', 'Soft rice', 'Dal', 'Steamed vegetables', 'Soft fruits', 'Avoid hard/cold'],
            'drinks': ['Warm turmeric milk (limited)', 'Gentle ginger tea (low ginger)', 'Warm lemon water + honey (limited)', 'Water (2-3L daily)'],
            'lifestyle': ['Head elevated 4-5 pillows', 'Humidifier (if tolerated)', 'Avoid sudden temperature changes', 'Gentle activity', 'Frequent monitoring'],
            'advice': 'Cough in elderly needs close monitoring. May indicate serious conditions.'
        }
    },
    'cold': {
        'infant': {
            'medicines': ['Saline nasal drops (only)', 'NO decongestants', 'Doctor approval essential'],
            'medicine_timing': 'As needed under supervision',
            'diet': ['Breast milk', 'Warm water', 'Soft mashed food'],
            'drinks': ['Breast milk/formula', 'Warm water only'],
            'lifestyle': ['Warm room', 'Humidifier', 'Elevate head', 'Frequent monitoring'],
            'advice': 'Common in infants. Maintain hydration, consult doctor if worsens.'
        },
        'child': {
            'medicines': ['Aspirin 300mg — 1 tablet every 6 hours (if fever)', 'Nasacort nasal spray — 1 spray per nostril, 2x daily', 'Throat lozenges — Strepsils'],
            'medicine_timing': 'Aspirin with food; nasal spray at night',
            'diet': ['Vegetable soup', 'Chicken rice soup', 'Soft bread', 'Eggs', 'Dal', 'Fresh fruits', 'Avoid cold/hard'],
            'drinks': ['Hot water with lemon + honey', 'Herbal tea with tulsi', 'Warm milk with turmeric', 'Fruit juice (diluted)', 'Warm water'],
            'lifestyle': ['Sleep 8-9 hours', 'Avoid AC/cold', 'Wash hands frequently', 'Separate towel', 'Salt water gargling 2x'],
            'advice': 'Common viral, mostly self-limiting. Focus on hydration and comfort.'
        },
        'teen': {
            'medicines': ['Aspirin 500mg — 1 tablet every 6 hours', 'Cetirizine 10mg — 1 tablet at night', 'Nasacort nasal spray — 1-2 sprays, 2x daily'],
            'medicine_timing': 'Aspirin with food; nasal spray at night; antihistamine at bedtime',
            'diet': ['Vegetable soup with garlic/ginger', 'Chicken rice soup', 'Soft bread', 'Boiled eggs', 'Dal', 'Fresh fruits', 'Avoid cheese/butter'],
            'drinks': ['Hot water with fresh lemon + honey + ginger', 'Herbal tea with tulsi', 'Warm milk with turmeric', 'Water (3-4L daily)'],
            'lifestyle': ['Sleep 8-9 hours daily', 'Avoid AC/cold', 'Wash hands frequently', 'Use separate towel', 'Gargle salt water 2-3x daily'],
            'advice': 'Common viral; mostly self-limiting in 7-10 days. Stay hydrated, rest.'
        },
        'adult': {
            'medicines': ['Aspirin 500mg — 1 tablet every 6 hours', 'Cetirizine 10mg (Allergyless) — 1 tablet at night', 'Nasacort nasal spray — 1-2 sprays, 2-3x daily'],
            'medicine_timing': 'Aspirin with food; nasal spray before sleep; antihistamine at bedtime',
            'diet': ['Vegetable soup with garlic/ginger', 'Chicken rice soup', 'Boiled eggs', 'Dal', 'Fresh fruits', 'Whole wheat bread', 'Avoid cheese/heavy'],
            'drinks': ['Hot water with fresh lemon + honey + ginger (best)', 'Herbal tea with tulsi/ginger/black pepper', 'Warm milk with turmeric', 'Water (3-4L daily)'],
            'lifestyle': ['Sleep 8-9 hours daily', 'Avoid AC/cold', 'Wash hands frequently', 'Use separate towel', 'Gargle salt water 2-3x daily'],
            'advice': 'Common viral; mostly self-limiting in 7-10 days. Focus on hydration and rest.'
        },
        'elderly': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 8 hours (if fever)', 'Cetirizine 10mg — 1 tablet at night (lower dose)', 'NO NSAIDs — safer with paracetamol'],
            'medicine_timing': 'Every 8 hours with food; antihistamine at night only',
            'diet': ['Warm vegetable broth', 'Soft rice soup', 'Boiled eggs', 'Dal', 'Soft fruits', 'Avoid hard/cold'],
            'drinks': ['Warm water with honey + lemon (limited)', 'Mild herbal tea (gentle ginger)', 'Warm milk (if tolerated)', 'Water (2-3L daily)'],
            'lifestyle': ['Sleep 8-9 hours', 'Avoid AC/sudden cold', 'Frequent hand washing', 'Gentle activity', 'Monitor BP regularly'],
            'advice': 'Cold in elderly needs monitoring. Maintain hydration, avoid sudden movements.'
        }
    },
    'weakness': {
        'infant': {
            'medicines': ['Doctor prescribed only', 'Iron drops — as prescribed', 'Vitamin supplements — as advised'],
            'medicine_timing': 'Per pediatrician prescription',
            'diet': ['Breast milk optimally', 'Fortified formula', 'Nutritious foods per age'],
            'drinks': ['Breast milk/formula', 'Warm water (limited)'],
            'lifestyle': ['Frequent feeding', 'Adequate sleep (18-20 hrs)', 'Regular monitoring', 'Comfortable environment'],
            'advice': 'Weakness in infants concerning. Ensure proper feeding and nutrition.'
        },
        'child': {
            'medicines': ['Iron syrup — 5ml daily in morning (empty stomach)', 'Multivitamin — 1 tsp daily', 'Vitamin B12 — as prescribed'],
            'medicine_timing': 'Morning on empty stomach with orange juice (enhances absorption)',
            'diet': ['Red meat/chicken 3-4 times weekly', 'Eggs — 2 daily', 'Lentils/dal — daily', 'Spinach 2-3x weekly', 'Almonds (5-6 daily)', 'Dates (2-3 daily)', 'Banana'],
            'drinks': ['Fresh orange juice — 1 glass daily', 'Pomegranate juice — 1 glass daily', 'Milk — 1 glass daily', 'Dry fruit shake (milk, dates, almonds)'],
            'lifestyle': ['Rest 2-3 hours daily', 'Light play outdoors', 'Sleep 10-12 hours', 'Nutritious diet strictly'],
            'advice': 'Weakness may indicate anemia, malnutrition, or infection. Get proper nutrition.'
        },
        'teen': {
            'medicines': ['Iron tablet — Ferrous Sulphate 325mg, 1 daily in morning (empty stomach)', 'Multivitamin — 1 tablet daily', 'Vitamin B12 — injections if needed'],
            'medicine_timing': 'Morning empty stomach with orange juice; multivitamin with breakfast',
            'diet': ['Red meat/chicken 3-4 times weekly', 'Eggs — 2-3 daily', 'Lentils/dal — daily', 'Spinach 3-4x weekly (cooked with ghee)', 'Beans/chickpeas', 'Almonds (5-6 daily)', 'Dates (2-3 daily)', 'Peanuts'],
            'drinks': ['Fresh orange juice — 1 glass daily', 'Pomegranate juice — 1 glass daily', 'Milk — 1 glass daily', 'Dry fruit shake daily'],
            'lifestyle': ['Rest 1-2 hours daily', 'Outdoor sports/exercise', 'Sleep 8-9 hours', 'Nutritious diet consistently'],
            'advice': 'Weakness may indicate anemia, low blood sugar, or infection. Get proper nutrition.'
        },
        'adult': {
            'medicines': ['Iron tablet — Ferrous Sulphate 325mg, 1 daily morning (empty stomach)', 'Multivitamin (Becosules CD) — 1 tablet daily', 'Vitamin B12 — 1 injection weekly if needed'],
            'medicine_timing': 'Iron in morning empty stomach with orange juice; multivitamin with breakfast',
            'diet': ['Red meat (goat/mutton) 3-4 times weekly', 'Chicken liver 2-3x weekly (best iron)', 'Spinach 3-4x weekly (cooked)', 'Eggs — 2 daily', 'Lentils/dal — daily', 'Beans/chickpeas', 'Almonds (5-6 soaked)', 'Dates (2-3 daily)', 'Whole wheat bread'],
            'drinks': ['Fresh orange juice — 1 glass daily (best for iron)', 'Pomegranate juice — 1 glass daily', 'Milk — 1 glass daily with breakfast', 'Dry fruit shake — dates, almonds, milk'],
            'lifestyle': ['Rest 1-2 hours daily', 'Regular exercise (walking)', 'Sleep 7-8 hours', 'Consistent nutritious diet'],
            'advice': 'Weakness may indicate anemia, low blood sugar, or infection. Get proper nutrition and hydration.'
        },
        'elderly': {
            'medicines': ['Iron tablet — Ferrous Sulphate 325mg, 1 every OTHER day (gentler)', 'Multivitamin (gentle formula) — 1 tablet daily', 'Vitamin B12 — 1 injection monthly if needed'],
            'medicine_timing': 'Take with food (easier on stomach); NO empty stomach; with gastroprotection if needed',
            'diet': ['Soft chicken/fish 3-4 times weekly', 'Eggs — 1-2 daily', 'Dal (lentil) — daily', 'Cooked spinach — 2-3x weekly', 'Soft bread', 'Mashed fruits', 'Avoid hard/difficult'],
            'drinks': ['Fresh orange juice — 1 glass every OTHER day (if kidneys OK)', 'Milk — 1 glass daily (if tolerated)', 'Water (2-3L daily)', 'Gentle herbal tea'],
            'lifestyle': ['Rest 2-3 hours daily (important)', 'Gentle morning walk (10-15 mins)', 'Sleep 7-8 hours', 'Regular monitoring of vitals'],
            'advice': 'Weakness in elderly concerning. May indicate anemia, malnutrition, medication side effects. Needs monitoring.'
        }
    },
    'abdominal_pain': {
        'infant': {
            'medicines': ['NO painkillers without doctor approval', 'Doctor-prescribed only', 'Assess symptoms first'],
            'medicine_timing': 'Per pediatrician only',
            'diet': ['Breast milk only', 'Clear liquids', 'Avoid solid foods'],
            'drinks': ['Breast milk/warm water only', 'ORS if dehydration'],
            'lifestyle': ['Gentle rocking/comfort', 'Monitor closely', 'Keep warm', 'Position of comfort'],
            'advice': 'Abdominal pain in infants needs urgent evaluation. Crying may indicate pain.'
        },
        'child': {
            'medicines': ['NO painkillers in first 24 hours — observe first', 'Antacid — Gelusil syrup, 1-2 tsp after meals', 'If cramping: Buscopan suspension — 2.5ml, 2x daily'],
            'medicine_timing': 'Antacid 30 mins after meals; others 15 mins before meals',
            'diet': ['FIRST 24HRS: liquids only (broth, water)', 'DAY 2-3: rice (boiled), toast', 'DAY 4+: dal, vegetables, banana', 'Gradually: soft chicken', 'Avoid fried/spicy 1-2 weeks'],
            'drinks': ['Coconut water — 1-2 glasses daily', 'ORS solution', 'Warm water only', 'Gentle broth'],
            'lifestyle': ['Bed rest 1-2 days', 'Sit upright after meals 30 mins', 'Avoid lying down', 'Heating pad on abdomen'],
            'advice': 'Mild pain usually improves with rest. Avoid solid foods initially. Seek urgent care if severe.'
        },
        'teen': {
            'medicines': ['NO painkillers in first 24 hours', 'Antacid — Gelusil MPS suspension, 1-2 tsp after meals 2-3x daily', 'If cramping: Buscopan 10mg — 1 tablet, 2-3x daily', 'If nausea: Domperidone 10mg — 1 tablet before meals 3x daily'],
            'medicine_timing': 'Antacid 30 mins after meals; others 15 mins before meals',
            'diet': ['FIRST 24HRS: liquids only (broth, water, electrolytes)', 'DAY 2-3: boiled rice, toast, crackers', 'DAY 4+: dal, boiled vegetables, banana', 'Gradually: plain chicken, steamed fish', 'Avoid spicy/fried/dairy 1-2 weeks'],
            'drinks': ['Coconut water — 1-2 glasses daily', 'ORS solution (prepared)', 'Warm water only', 'Buttermilk if pain improves', 'Clear broth', 'Water (2-3L daily, sip slowly)'],
            'lifestyle': ['Bed rest 1-2 days', 'Sit upright 30 mins after meals', 'Avoid lying immediately', 'Heating pad on abdomen', 'Avoid strenuous activity'],
            'advice': 'Mild pain usually improves with rest. Avoid solid foods initially. Seek urgent care if severe.'
        },
        'adult': {
            'medicines': ['NO painkillers in first 24 hours', 'Antacid — Gelusil MPS, 1-2 tsp after meals 2-3x daily', 'If cramping: Buscopan 10mg — 1 tablet, 2-3x daily', 'If nausea: Domperidone 10mg — 1 tablet before meals 3x daily'],
            'medicine_timing': 'Antacid 30 mins after meals; others 15 mins before meals with water',
            'diet': ['FIRST 24HRS: liquids only (broth, water, ORS)', 'DAY 2-3: boiled rice, toast, crackers', 'DAY 4+: dal, boiled vegetables, banana', 'Gradually: plain chicken, steamed fish', 'Avoid spicy/fried/dairy/milk 1-2 weeks'],
            'drinks': ['Coconut water — 1-2 glasses daily', 'ORS solution (prepared)', 'Warm water only', 'Buttermilk (if pain improves)', 'Clear broth/soup', 'Water (2-3L daily, sip slowly)'],
            'lifestyle': ['Bed rest 1-2 days', 'Sit upright 30 mins after meals', 'Avoid lying down immediately', 'Heating pad on abdomen', 'Avoid strenuous activity', 'Complete rest initially'],
            'advice': 'Mild pain usually improves with rest. Avoid solid foods initially. Seek urgent care if severe.'
        },
        'elderly': {
            'medicines': ['NO painkillers in first 24 hours — observe first', 'Antacid (gentle) — Gelusil suspension, 1-2 tsp after meals (limited)', 'CONSULT DOCTOR — may need prescription antispasmodics'],
            'medicine_timing': 'Under doctor supervision only; antacid 30 mins after meals if approved',
            'diet': ['FIRST 24HRS: clear liquids only (water, broth — NO milk)', 'DAY 2-3: soft rice, toast (no butter)', 'DAY 4+: soft dal, steamed vegetables', 'Gradually: soft chicken/fish', 'Avoid hard/fried/spicy'],
            'drinks': ['Warm water only (main)', 'Gentle broth', 'Limited ORS if dehydration', 'No milk initially', 'Water (2-3L daily, sip slowly)'],
            'lifestyle': ['Complete bed rest', 'Frequent monitoring of vitals', 'Elevate head (if comfortable)', 'Avoid sudden movements', 'Frequent small position changes'],
            'advice': 'Abdominal pain in elderly needs urgent evaluation. May indicate serious conditions.'
        }
    },
    'rash': {
        'infant': {
            'medicines': ['NO topical creams without doctor approval', 'Calamine lotion (check with doctor)', 'Doctor prescribed only'],
            'medicine_timing': 'Per pediatrician only',
            'diet': ['Breast milk', 'Soft foods', 'Avoid allergens'],
            'drinks': ['Breast milk/warm water', 'Avoid new juices'],
            'lifestyle': ['Cool room', 'Loose cotton clothes only', 'Monitor fever', 'Avoid scratching'],
            'advice': 'Rash in infants needs immediate evaluation. Monitor closely for fever.'
        },
        'child': {
            'medicines': ['NO painkiller if fever <38.5°C', 'Paracetamol syrup (if fever) — 5ml every 6 hours', 'Calamine lotion — apply on rash, 2-3 times daily', 'Antihistamine — Cetirizine syrup 5ml at night'],
            'medicine_timing': 'Calamine after bath; antihistamine at bedtime; Paracetamol only if fever',
            'diet': ['Cool foods — cucumber, bottled gourd, watermelon', 'Light proteins — boiled eggs, soft chicken', 'Rice, dal, banana, papaya', 'Avoid — hot foods, spicy, nuts, seafood, processed'],
            'drinks': ['Coconut water — 1-2 glasses daily (cooling)', 'Fresh juice (diluted 50%)', 'Neem water (boil leaves, cool, drink)', 'Warm water (2-3L daily)', 'Milk with turmeric (limited)'],
            'lifestyle': ['Wear cotton loose clothes only', 'Keep clean and dry', 'Avoid sun exposure', 'Cut nails short', 'Use soft towel', 'NO scratching — apply lotion'],
            'advice': 'Rash with fever needs evaluation. Avoid scratching to prevent infection.'
        },
        'teen': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 6 hours (if fever)', 'Calamine lotion — apply on rash, 2-3 times daily', 'Antihistamine — Cetirizine 10mg at night', 'Hydrocortisone 1% cream — on severe itching areas, 2x daily'],
            'medicine_timing': 'Calamine after bath; antihistamine at bedtime; Hydrocortisone only on red areas',
            'diet': ['Cool foods — cucumber, bottled gourd, watermelon', 'Light proteins — eggs, soft chicken', 'Rice, dal, banana, papaya', 'Avoid — hot/spicy, nuts, seafood, processed, chocolate'],
            'drinks': ['Coconut water — 1-2 glasses daily (cooling)', 'Fresh juice (diluted)', 'Neem water (boil leaves, cool, drink)', 'Water (3-4L daily)', 'Mild milk'],
            'lifestyle': ['Cotton loose clothes only', 'Keep clean and dry', 'Avoid sun exposure', 'Cut nails short', 'Use soft towel', 'NO scratching — apply lotion'],
            'advice': 'Rash with fever needs evaluation. Avoid scratching to prevent infection.'
        },
        'adult': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 6 hours (if fever)', 'Calamine lotion — apply on rash, 2-3 times daily', 'Antihistamine — Cetirizine 10mg at night', 'Hydrocortisone 1% cream — on severe red/inflamed areas, 2x daily'],
            'medicine_timing': 'Calamine after bath; antihistamine at bedtime; Hydrocortisone only on inflamed areas',
            'diet': ['Cool foods — cucumber, bottled gourd, watermelon', 'Light proteins — eggs, fish, soft chicken', 'Rice, dal, banana, papaya', 'Avoid — hot/spicy, nuts, shellfish, processed, chocolate'],
            'drinks': ['Coconut water — 1-2 glasses daily (cooling)', 'Fresh juice (50% diluted)', 'Neem water (boil neem leaves, cool, drink)', 'Water (3-4L daily)', 'Milk with turmeric (limited)'],
            'lifestyle': ['Cotton loose clothes only', 'Keep areas clean and dry', 'Avoid sun exposure', 'Cut nails short', 'Use soft towel', 'Avoid scratching — apply lotion instead'],
            'advice': 'Rash with fever needs evaluation. Avoid scratching to prevent infection.'
        },
        'elderly': {
            'medicines': ['Paracetamol 500mg — 1 tablet every 8 hours (if fever, lower dose)', 'Calamine lotion (gentle) — apply, 2x daily', 'Antihistamine (low dose) — Cetirizine 5mg at night (NOT 10mg)', 'NO hydrocortisone without doctor approval'],
            'medicine_timing': 'Calamine 2x daily; antihistamine at night only; limited paracetamol',
            'diet': ['Cooling foods — soft cucumber, watermelon (limited)', 'Light protein — soft boiled eggs, steamed fish', 'Soft rice, dal, banana', 'Avoid — hot/spicy, hard, nuts, seafood, processed'],
            'drinks': ['Coconut water (limited, if kidney OK)', 'Gentle juice (50% diluted)', 'Warm water (2-3L daily)', 'Mild milk (if tolerated)', 'Avoid — tea, coffee, cold drinks'],
            'lifestyle': ['Loose soft cotton clothes', 'Keep clean and dry', 'Avoid sun exposure completely', 'Keep nails short', 'Frequent position changes', 'Avoid scratching'],
            'advice': 'Rash in elderly needs careful monitoring. May indicate serious conditions or medication reaction.'
        }
    }
}


def get_month_specific_infant_recommendations(symptom, months):
    """Get month-specific recommendations for infants (0-12 months).
    Provides pediatrician-grade dosages based on baby's age in months.
    """
    if months is None or months < 0 or months > 12:
        return {}
    
    # Month ranges: newborn (0-2), young infant (3-5), older infant (6-8), advanced infant (9-12)
    MONTH_SPECIFIC = {
        'fever': {
            '0-2': {  # Newborn (0-2 months)
                'medicines': ['URGENT: Do NOT self-medicate. Fever in newborn requires immediate doctor visit.', 'Paracetamol only if prescribed by pediatrician — 10-15 mg/kg per dose'],
                'medicine_timing': 'Only under pediatrician supervision; never self-medicate',
                'diet': ['Exclusive breast milk (every 2-3 hours)', 'NO formula unless prescribed'],
                'drinks': ['Breast milk only', 'NO water or other liquids'],
                'lifestyle': ['Maintain warm environment (23-25°C)', 'Frequent skin-to-skin contact', 'Monitor diaper output (6+ wet diapers/day)', 'Check temperature every 30 mins'],
                'advice': 'Newborn fever is serious. ALWAYS consult pediatrician immediately. Keep warm, continue feeding.',
                'age_stage': 'Newborn (0-2 months)'
            },
            '3-5': {  # Young infant (3-5 months)
                'medicines': ['Paracetamol syrup 125mg/5ml — 2.5ml every 4-6 hours (max 4 doses/day)', 'Ibuprofen alternative (NOT before 6 months without doctor approval)'],
                'medicine_timing': 'Every 4-6 hours; max 4 doses/day; only if fever >38.5°C and baby uncomfortable',
                'diet': ['Exclusive breast milk (6-8 feeds/day)', 'Start trying solid foods if 6 months: iron-fortified rice cereal (1 tsp mixed with milk)'],
                'drinks': ['Breast milk only', 'NO cow milk, NO sugar water'],
                'lifestyle': ['Light clothing during fever', 'Cool room (22-24°C)', 'Sponge bath with lukewarm water (10-15 mins)', 'Frequent feeds to maintain hydration', 'Diaper checks for hydration (6+ wet)'],
                'advice': 'Young infant fever needs close monitoring. Keep breastfeeding frequent. Cool sponging helps. Call doctor if fever >38.5°C or lasts >24 hours.',
                'age_stage': 'Young infant (3-5 months)'
            },
            '6-8': {  # Older infant (6-8 months)
                'medicines': ['Paracetamol syrup 125mg/5ml — 5ml every 4-6 hours (max 4 doses/day)', 'Ibuprofen syrup 100mg/5ml — 2.5ml every 6-8 hours (if >6 months and doc-approved; max 3 doses/day)'],
                'medicine_timing': 'Every 4-6 hours; max 4 paracetamol doses/day',
                'diet': ['Breast milk (4-6 feeds/day)', 'Rice cereal (2-3 tsp with milk)', 'Mashed fruits: banana, apple, papaya', 'Vegetable purees: carrots, sweet potato (cooked well)', 'Soft boiled egg yolk (start with tiny amount)', 'Diluted dal water'],
                'drinks': ['Breast milk primarily', 'Boiled cooled water (max 100ml/day)', 'Diluted fruit juice (1:1 ratio, max 100ml)', 'ORS solution if diarrhea present'],
                'lifestyle': ['Light cotton clothes', 'Room temperature 22-24°C', 'Sponge bath 10-15 mins with lukewarm water', 'Frequent breastfeeds + solids 2-3 times/day', 'Dry promptly after sponging'],
                'advice': 'Older infant can tolerate more foods. Introduce new foods one at a time (wait 3 days). Sponging reduces fever naturally. Breastfeed more frequently.',
                'age_stage': 'Older infant (6-8 months)'
            },
            '9-12': {  # Advanced infant (9-12 months)
                'medicines': ['Paracetamol syrup 125mg/5ml — 5-7.5ml every 4-6 hours (max 4 doses/day)', 'Ibuprofen syrup 100mg/5ml — 5ml every 6-8 hours (if 9+ months; max 3 doses/day)'],
                'medicine_timing': 'Every 4-6 hours; max 4 paracetamol or 3 ibuprofen doses/day',
                'diet': ['Breast milk (2-3 feeds/day)', 'Soft khichdi (rice + dal) with ghee', 'Mashed vegetables: carrot, potato, pumpkin', 'Fruits: banana, apple, papaya, orange (mashed)', 'Soft boiled egg (whole egg okay now)', 'Chicken/fish porridge (small pieces)', 'Plain yogurt (small amount)', 'Soft finger foods: toast, crackers'],
                'drinks': ['Breast milk', 'Boiled cooled water (200-300ml/day)', 'Diluted fruit/vegetable juice', 'ORS if diarrhea', 'Coconut water (limited)'],
                'lifestyle': ['Light clothing during fever', 'Room temp 22-24°C', 'Sponge bath 10-15 mins with lukewarm water', 'Frequent fluids + soft foods', 'Sleep elevation with pillow (small, safe)', 'Allow playtime when fever <38°C'],
                'advice': '9-12 month infant has better fever tolerance. Introduce more foods. Continue sponging. Monitor for warning signs: difficulty breathing, rash, extreme lethargy.',
                'age_stage': 'Advanced infant (9-12 months)'
            }
        },
        'cough': {
            '0-2': {
                'medicines': ['NO cough syrups or medications', 'Steam inhalation only (under supervision)', 'Honey NOT recommended before 1 year'],
                'medicine_timing': 'No medicines; monitor and consult doctor',
                'diet': ['Exclusive breast milk', 'NO solids'],
                'drinks': ['Breast milk only'],
                'lifestyle': ['Keep air moist (use humidifier)', 'Elevate baby (safe angle)', 'Feed frequently in upright position', 'Keep clear of smoke', 'Monitor temperature'],
                'advice': 'Newborn cough needs doctor visit. Use humidity and frequent feeding. NO home remedies or syrups.',
                'age_stage': 'Newborn (0-2 months)'
            },
            '3-5': {
                'medicines': ['NO cough medicines', 'Steam vapor as needed', 'Saline nasal drops if congested'],
                'medicine_timing': 'Monitor daily; call doctor if worsens',
                'diet': ['Breast milk (frequent feeds)', 'Warm foods help'],
                'drinks': ['Breast milk', 'Warm boiled water (sips)'],
                'lifestyle': ['Moist air (use humidifier)', 'Upright position for sleep', 'Keep warm', 'Avoid smoke/cold air', 'Daily temperature check'],
                'advice': 'Cough is natural. Use moisture and breastfeeding. Call doctor if fever, difficulty breathing, or green mucus.',
                'age_stage': 'Young infant (3-5 months)'
            },
            '6-8': {
                'medicines': ['NO cough syrups', 'Saline nasal drops/spray if blocked nose', 'Warm salt water gargle (assisted)'],
                'medicine_timing': 'Saline drops as needed (up to 3-4 times/day)',
                'diet': ['Breast milk (4-6 feeds)', 'Warm semi-solid foods: rice cereal, dal water', 'Honey (1 tsp mixed in warm water or food is okay now — helps cough)'],
                'drinks': ['Breast milk', 'Warm water (200ml/day)', 'Honey + warm water (1 tsp honey)'],
                'lifestyle': ['Humid air (humidifier 40-50%)', 'Upright sleeping position', 'Warm clothes', 'Avoid irritants/smoke', 'Monitor for 5-7 days'],
                'advice': 'Cough usually viral and self-limiting. Humidity + honey + frequent feeds help. Call doctor if fever, fast breathing, or worsening.',
                'age_stage': 'Older infant (6-8 months)'
            },
            '9-12': {
                'medicines': ['NO cough syrups/expectorants', 'Honey 1-2 tsp mixed in warm milk/food for cough relief (honey is now safe)', 'Saline nasal spray if needed'],
                'medicine_timing': 'Honey up to 2-3 times/day; saline as needed',
                'diet': ['Breast milk (2-3 feeds)', 'Warm khichdi with ghee', 'Chicken/vegetable broth', 'Soft fruits', 'Eggs', 'Honey in warm foods'],
                'drinks': ['Breast milk', 'Warm water (300-400ml/day)', 'Honey + warm milk/water', 'Ginger-honey water (trace ginger)', 'Coconut water'],
                'lifestyle': ['Humidifier 40-50% humidity', 'Upright sleep with pillow support', 'Warm clothes', 'Fresh air (avoid cold)', 'Monitor cough pattern'],
                'advice': 'Honey is natural cough suppressant (safe >6 months). Warm foods help. Most coughs resolve in 1-2 weeks. See doctor if worsens.',
                'age_stage': 'Advanced infant (9-12 months)'
            }
        }
    }
    
    # Determine month range
    month_range = None
    if months <= 2:
        month_range = '0-2'
    elif months <= 5:
        month_range = '3-5'
    elif months <= 8:
        month_range = '6-8'
    else:
        month_range = '9-12'
    
    if symptom in MONTH_SPECIFIC and month_range in MONTH_SPECIFIC[symptom]:
        return MONTH_SPECIFIC[symptom][month_range]
    
    return {}


def get_realtime_thinking_for_babies(symptom, months):
    """Generate real-time thinking process for baby recommendations"""
    thinking = {
        'analysis_steps': [],
        'reasoning': '',
        'final_recommendation': {}
    }
    
    # Step 1: Analyze age group
    thinking['analysis_steps'].append({
        'step': 1,
        'title': 'Analyzing Baby Age Group',
        'content': f'Baby is {months} months old. Determining appropriate age category for {symptom}...'
    })
    
    # Step 2: Determine month range
    if months <= 2:
        month_range = '0-2'
        age_stage = 'Newborn (0-2 months)'
        thinking['analysis_steps'].append({
            'step': 2,
            'title': 'Age Category Identified',
            'content': f'Baby falls in NEWBORN category (0-2 months). This is a critical age where utmost care is needed. Newborn immune system is developing, so approach is CONSERVATIVE - emphasis on doctor supervision and exclusive breastfeeding.'
        })
    elif months <= 5:
        month_range = '3-5'
        age_stage = 'Young infant (3-5 months)'
        thinking['analysis_steps'].append({
            'step': 2,
            'title': 'Age Category Identified',
            'content': f'Baby falls in YOUNG INFANT category (3-5 months). At this stage, baby is still primarily breastfed but starting to develop immunity. Medicines are introduced carefully, starting very low doses.'
        })
    elif months <= 8:
        month_range = '6-8'
        age_stage = 'Older infant (6-8 months)'
        thinking['analysis_steps'].append({
            'step': 2,
            'title': 'Age Category Identified',
            'content': f'Baby falls in OLDER INFANT category (6-8 months). Baby is starting solid foods and developing better tolerance. Medicine doses can be increased slightly. Introduction of certain foods like honey now becomes safer.'
        })
    else:
        month_range = '9-12'
        age_stage = 'Advanced infant (9-12 months)'
        thinking['analysis_steps'].append({
            'step': 2,
            'title': 'Age Category Identified',
            'content': f'Baby falls in ADVANCED INFANT category (9-12 months). Baby is eating more varied foods, developing better immune response. Can tolerate more diverse diet and appropriate medications.'
        })
    
    # Step 3: Analyze symptom
    thinking['analysis_steps'].append({
        'step': 3,
        'title': 'Analyzing Symptom Context',
        'content': f'Symptom reported: {symptom.upper()}. Looking up age-appropriate treatment protocols for {age_stage}...'
    })
    
    # Step 4: Get recommendations
    from age_specific_recommendations import get_month_specific_infant_recommendations
    recs = get_month_specific_infant_recommendations(symptom, months)
    
    if recs:
        medicines_count = len(recs.get('medicines', []))
        diet_count = len(recs.get('diet', []))
        
        thinking['analysis_steps'].append({
            'step': 4,
            'title': 'Treatment Protocol Selected',
            'content': f'Found specialized {months}-month protocol for {symptom}. Protocol includes: {medicines_count} medicine options, {diet_count} dietary recommendations, specific timing guidance, and age-appropriate lifestyle changes.'
        })
        
        thinking['analysis_steps'].append({
            'step': 5,
            'title': 'Recommendation Summary',
            'content': f'Based on {age_stage} development: {recs.get("advice", "")} This recommendation prioritizes {age_stage.lower()} safety and natural healing methods appropriate for this age.'
        })
        
        thinking['reasoning'] = f'For a {months}-month-old baby with {symptom}, the {age_stage} protocol recommends careful monitoring with age-appropriate medicines and nutrition. The baby\'s developing immune system requires gentle, evidence-based approaches.'
        thinking['final_recommendation'] = recs
    
    return thinking


def get_age_specific_recommendations(symptom, age):
    """Get age-specific recommendations for a given symptom.
    If age is fractional (infant with months), calls month-specific function.
    """
    # If age is fractional (0.25, 0.5, 0.75, 1.0) it means months data was provided
    if age is not None and age < 2 and age != int(age):
        # Convert back to months for more precise recommendations
        months = int(round(age * 12))
        month_recs = get_month_specific_infant_recommendations(symptom, months)
        if month_recs:
            return month_recs
    
    age_cat = get_age_category(age)
    
    if symptom in AGE_SPECIFIC_SYMPTOMS:
        return AGE_SPECIFIC_SYMPTOMS[symptom].get(age_cat, AGE_SPECIFIC_SYMPTOMS[symptom].get('adult', {}))
    
    return {}
