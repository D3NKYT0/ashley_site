import json

with open("data/achievements.json", encoding="utf-8") as achievements:
    achievements = json.load(achievements)

with open("data/answers.json", encoding="utf-8") as answers:
    answers = json.load(answers)

with open("data/artifacts.json", encoding="utf-8") as artifacts:
    artifacts = json.load(artifacts)

with open("data/attribute.json", encoding="utf-8") as attribute:
    attribute = json.load(attribute)

# auth nao é carregado aqui!

with open("data/battle.json", encoding="utf-8") as battle:
    battle = json.load(battle)

with open("data/cards.json", encoding="utf-8") as cards:
    cards = json.load(cards)

with open("data/config.json", encoding="utf-8") as config:
    config = json.load(config)

with open("data/ctf.json", encoding="utf-8") as ctf:
    ctf = json.load(ctf)

with open("data/emojis.json", encoding="utf-8") as emojis:
    emojis = json.load(emojis)

with open("data/equips.json", encoding="utf-8") as equips:
    equips = json.load(equips)

with open("data/especial_recipes.json", encoding="utf-8") as especial_recipes:
    especial_recipes = json.load(especial_recipes)

with open("data/forca.json", encoding="utf-8") as forca:
    forca = json.load(forca)

with open("data/icons.json", encoding="utf-8") as icons:
    icons = json.load(icons)

with open("data/items.json", encoding="utf-8") as items:
    items = json.load(items)

with open("data/palin.json", encoding="utf-8") as palin:
    palin = json.load(palin)

with open("data/pets.json", encoding="utf-8") as pets:
    pets = json.load(pets)

with open("data/poke.json", encoding="utf-8") as poke:
    poke = json.load(poke)

with open("data/questions.json", encoding="utf-8") as questions:
    questions = json.load(questions)

with open("data/quests.json", encoding="utf-8") as quests:
    quests = json.load(quests)

with open("data/recipes.json", encoding="utf-8") as recipes:
    recipes = json.load(recipes)

with open("data/reflect.json", encoding="utf-8") as reflect:
    reflect = json.load(reflect)

with open("data/riddles.json", encoding="utf-8") as riddles:
    riddles = json.load(riddles)

with open("data/salutation.json", encoding="utf-8") as salutation:
    salutation = json.load(salutation)

with open("data/set_equips.json", encoding="utf-8") as set_equips:
    set_equips = json.load(set_equips)

with open("data/skills.json", encoding="utf-8") as skills:
    skills = json.load(skills)

with open("data/staff.json", encoding="utf-8") as staff:
    staff = json.load(staff)

with open("data/sticker_book.json", encoding="utf-8") as sticker_book:
    sticker_book = json.load(sticker_book)

with open("data/thinker.json", encoding="utf-8") as thinker:
    thinker = json.load(thinker)

with open("data/wiki.json", encoding="utf-8") as wiki:
    wiki = json.load(wiki)

data = {
    "achievements": achievements,
    "answers": answers,
    "artifacts": artifacts,
    "attribute": attribute,
    "battle": battle,
    "cards": cards,
    "config": config,
    "ctf": ctf,
    "emojis": emojis,
    "equips": equips,
    "especial_recipes": especial_recipes,
    "forca": forca,
    "icons": icons,
    "items": items,
    "palin": palin,
    "pets": pets,
    "poke": poke,
    "questions": questions,
    "quests": quests,
    "recipes": recipes,
    "reflect": reflect,
    "riddles": riddles,
    "salutation": salutation,
    "set_equips": set_equips,
    "skills": skills,
    "staff": staff,
    "sticker_book": sticker_book,
    "thinker": thinker,
    "wiki": wiki
}
