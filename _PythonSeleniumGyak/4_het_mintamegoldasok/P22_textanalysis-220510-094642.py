import re

# file beolvasas

# with open("source.txt", "r") as input:
#     source = input.read()

source = """The Old Sea-dog at the Admiral Benbow

SQUIRE TRELAWNEY, Dr. Livesey, and the rest of these gentlemen having
asked me to write down the whole particulars about Treasure Island, from
the beginning to the end, keeping nothing back but the bearings of the
island, and that only because there is still treasure not yet lifted,
I take up my pen in the year of grace 17__ and go back to the time when
my father kept the Admiral Benbow inn and the brown old seaman with the
sabre cut first took up his lodging under our roof.

I remember him as if it were yesterday, as he came plodding to the inn
door, his sea-chest following behind him in a hand-barrow, a tall, strong,
heavy, nut-brown man, his tarry pigtail falling over the shoulder of his
soiled blue coat, his hands ragged and scarred, with black, broken nails,
and the sabre cut across one cheek, a dirty, livid white. I remember him
looking round the cover and whistling to himself as he did so, and then
breaking out in that old sea-song that he sang so often afterwards:

"Fifteen men on the dead man's chest Yo-ho-ho, and a bottle of rum!"

in the high, old tottering voice that seemed to have been tuned and
broken at the capstan bars. Then he rapped on the door with a bit of
stick like a handspike that he carried, and when my father appeared,
called roughly for a glass of rum. This, when it was brought to him,
he drank slowly, like a connoisseur, lingering on the taste and still
looking about him at the cliffs and up at our signboard.

"This is a handy cove," says he at length; "and a pleasant sittyated
grog-shop. Much company, mate?"

My father told him no, very little company, the more was the pity.

"Well, then," said he, "this is the berth for me. Here you, matey," he
cried to the man who trundled the barrow; "bring up alongside and help
up my chest. I'll stay here a bit," he continued. "I'm a plain man; rum
and bacon and eggs is what I want, and that head up there for to watch
ships off. What you mought call me? You mought call me captain. Oh, I see
what you're at, there"; and he threw down three or four gold pieces on
the threshold. "You can tell me when I've worked through that," says he,
looking as fierce as a commander."""

# szövegtisztítás és rendezes, split
stripped_source = re.sub('[",.?_;!:]', ' ', source)
smallcap_source = stripped_source.lower()
words = sorted(smallcap_source.split())

#szavak megszámolása, directory feltöltés

words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict.update({word: 1})

#directory kiíratása
count = 0
for key in words_dict:
    count += 1
    print(f"{key}_{count} előfordulások száma_{words_dict[key]}")
