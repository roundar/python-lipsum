# Lipsum

Custom encoding for storing bytes as lorem ipsum text and a command line utility for converting it.

## Install: 
```
pip install git+https://github.com/roundar/python-lipsum
```

## Lipsum Guidelines:
1. Lipsum encoded string starts with 'Lorem ipsum dolor sit amet' referred to as the 'intro.'
2. All non-alpha sequences are a single separator.
3. The following four letter words are used (without regard to case) to represent bytes (byte value is the index in the following list):
```
['neco', 'cito', 'sino', 'acsi', 'eris', 'demo', 'suus', 'cura', 'ipsa', 'aqua', 'prae', 'vita', 'huic', 'vado', 'eger', 'alia', 'bibo', 'unus', 'pons', 'deus', 'mens', 'tibi', 'sedi', 'opus', 'lues', 'prex', 'ideo', 'lusi', 'leve', 'tunc', 'illo', 'texo', 'neut', 'etsi', 'usus', 'post', 'volo', 'vaco', 'mire', 'ergo', 'clam', 'pica', 'apto', 'itis', 'tero', 'risi', 'tego', 'diei', 'fama', 'suum', 'amor', 'puto', 'unde', 'quas', 'from', 'vidi', 'pono', 'orno', 'hunc', 'dare', 'male', 'curo', 'iter', 'loci', 'utor', 'hora', 'mica', 'fovi', 'atra', 'colo', 'nota', 'addo', 'sepe', 'rgis', 'sedo', 'repo', 'ligo', 'mora', 'labo', 'pius', 'arma', 'quam', 'cavi', 'alui', 'cras', 'haud', 'levo', 'rexi', 'quot', 'voro', 'reus', 'ater', 'fore', 'mare', 'ceno', 'cogo', 'alii', 'quid', 'ledo', 'pupa', 'fors', 'lama', 'miro', 'vovi', 'erga', 'fero', 'furs', 'mihi', 'texi', 'queo', 'lego', 'mons', 'armo', 'iste', 'inis', 'flax', 'dies', 'cedo', 'mane', 'ager', 'ordo', 'misi', 'immo', 'pene', 'sato', 'nisi', 'moti', 'mors', 'nego', 'indo', 'hanc', 'uter', 'onus', 'muto', 'olim', 'pluo', 'agri', 'celo', 'cado', 'onis', 'itum', 'haec', 'pala', 'puga', 'coma', 'malo', 'tres', 'egre', 'rogo', 'quem', 'ille', 'rego', 'paro', 'sane', 'duro', 'lino', 'ludo', 'esse', 'bene', 'fleo', 'quos', 'lima', 'sono', 'illi', 'dedi', 'plus', 'luna', 'novo', 'meus', 'vito', 'dens', 'ipse', 'arca', 'uxor', 'sese', 'cena', 'iuge', 'iuvo', 'dito', 'tuli', 'scio', 'abeo', 'quae', 'quin', 'spes', 'past', 'inde', 'vero', 'adeo', 'erro', 'vivo', 'frux', 'nunc', 'gemo', 'fluo', 'pium', 'eluo', 'laus', 'ante', 'iuro', 'enim', 'veni', 'vici', 'vera', 'apud', 'gero', 'fugo', 'fere', 'humo', 'creo', 'acer', 'urbs', 'crux', 'hinc', 'pyga', 'voco', 'nemo', 'puer', 'modo', 'illa', 'cubo', 'gens', 'lens', 'dico', 'vere', 'duco', 'oris', 'sano', 'ista', 'eruo', 'idem', 'pyus', 'sumo', 'nolo', 'peto', 'homo', 'loco', 'ioco', 'cibo', 'pars', 'quia', 'sine', 'rota', 'quod', 'fuga', 'leno', 'vixi', 'crur', 'egeo', 'opes', 'sive', 'leto', 'opto', 'tria', 'arto', 'odio']
```
4. All words not in this list are considered filler and ignored.
5. ' ex.' denotes the end of a lipsum encoded string (subsequent characters are ignored).

## Usage

#### Commandline
```bash
~$ echo "This is a test!" | lipsum --compressed --wrap 80 > file.txt
~$ lipsum --decode --compressed file.txt
This is a test!
~$ echo "All together now..." | lipsum | lipsum -d
All together now...
~$ cat file.txt
Lorem ipsum dolor sit amet. Alveus mica reus subitus erga orno. Nocens suum hora
voro defendo mire alui, voro rursus muto mihi arx suum quem. Caries neco neco
vapulus sino urbs nego an neco bibo. Functus alii neco eris quaeso, neco usus
alii nuper huic neco. Pessime neut neco genuit suum neco fama, xiphias neut creo
minutum illi neut! Paratus arma ceno unus labores lima pono mihi. Seputus male
mare veni niveus mens duco mica. Vespera mica tibi lente arca ante cras ex.
```

#### As module
```python
>>> import lipsum

>>> example = 'This is a test!"
>>> result = lipsum.to_lipsum(example)
>>> print(result)
Lorem ipsum dolor sit amet. Lactuca cras erga fero, sustuli flax neut vox fero flax forma neut quid. Pluvit neut dies quercus lama flax supra dies etsi. Prae ex.
>>> print(lipsum.from_lipsum(result).encode())
This is a test!
```