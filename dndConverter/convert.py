#! python3
url = "https://raw.githubusercontent.com/jcquinlan/dnd-spells/master/spells.json"
import re,urllib.request,requests,json
regex = r"'<[^<]+?>'"
removetags = lambda stri: re.sub('<[^<]+?>', '', stri)
header = b'''//Sword Coast Adventurer v1.2

var jsonSpellData = '''
# First we downlaod the file
urllib.request.urlretrieve(url,"tmp.json")
# Now we open the file
spell = open("tmp.json","rb").read()
spell = spell.replace(header,b"")
d = open("spells.json","w")
spell = spell.decode("cp1252","ignore")
d.write(spell)
d.close()
data = eval(open("spells.json").read()[:-2])
print("Loaded {} spells. Parsing...".format(len(data)))
out = {}
for spell in data:
    name = spell.pop("name")
    cat = spell.pop("level")
    if not cat in out:
        out[cat] = {}
    for thing in spell:
        spell[thing] = removetags(spell[thing]).capitalize()
    out[cat][name] = spell
out = json.dumps(out)
d = open("../spells.json","w")
d.write(out)
d.close()
print("DONE!")
