
SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'


XOFI = XTFI = YTFI = [ 'dollar', 'sterling', 'yen', 'numbersign', 'Euro', 'franc', 'lira', 'naira', 'peseta', 'won', 'dong', 'rupeeIndian', 'liraTurkish', 'manat', 'ruble', 'numero', 'commercialMinusSign', 'florin', 'coloncurrency', 'uni20AD', 'uni20B1', 'uni20B2', 'uni20B5', 'hryvnia', 'tenge', 'dollar.rvrn', 'cent.rvrn', 'coloncurrency.rvrn', 'naira.rvrn', 'won.rvrn', 'uni20B1.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.prop', 'one.prop', 'two.prop', 'three.prop', 'four.prop', 'five.prop', 'six.prop', 'seven.prop', 'eight.prop', 'nine.prop', 'percent', 'perthousand', 'currency', 'degree', 'plus', 'less', 'equal', 'greater', 'minus', 'logicalnot', 'plusminus', 'multiply', 'divide', 'approxequal', 'notequal', 'lessequal', 'greaterequal', 'bulletoperator', 'fraction', 'zerosuperior', 'onesuperior', 'twosuperior', 'threesuperior', 'foursuperior', 'cent', ]

XOLC = XTLC = YTLC = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'germandbls', 'f_f', 'fi', 'fl', 'f_f_i', 'f_f_l', 'f_f_ij', 'f_ij', 'agrave', 'aacute', 'acircumflex', 'atilde', 'adieresis', 'aring', 'ae', 'ccedilla', 'egrave', 'eacute', 'ecircumflex', 'edieresis', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'eth', 'ntilde', 'ograve', 'oacute', 'ocircumflex', 'otilde', 'odieresis', 'oslash', 'ugrave', 'uacute', 'ucircumflex', 'udieresis', 'yacute', 'thorn', 'ydieresis', 'amacron', 'abreve', 'aogonek', 'cacute', 'ccircumflex', 'cdotaccent', 'ccaron', 'dcaron', 'dcroat', 'emacron', 'ebreve', 'edotaccent', 'eogonek', 'ecaron', 'gcircumflex', 'gbreve', 'gdotaccent', 'gcommaaccent', 'hcircumflex', 'hbar', 'itilde', 'imacron', 'ibreve', 'iogonek', 'ij', 'kcommaaccent', 'kgreenlandic', 'lacute', 'lcommaaccent', 'lcaron', 'ldot', 'lslash', 'nacute', 'ncommaaccent', 'ncaron', 'napostrophe', 'eng', 'omacron', 'obreve', 'ohungarumlaut', 'oe', 'racute', 'rcommaaccent', 'rcaron', 'sacute', 'scircumflex', 'scedilla', 'scaron', 'tcedilla', 'tcaron', 'tbar', 'utilde', 'umacron', 'ubreve', 'uring', 'uhungarumlaut', 'uogonek', 'wcircumflex', 'ycircumflex', 'zacute', 'zdotaccent', 'zcaron', 'ohorn', 'uhorn', 'dzcaron', 'idotless', 'jdotless', 'ijacute', 'idotaccent', 'jcircumflex', 'jacute.loclNLD', 'lj', 'nj', 'gcaron', 'oogonek', 'aringacute', 'aeacute', 'oslashacute', 'adblgrave', 'ainvertedbreve', 'edblgrave', 'einvertedbreve', 'idblgrave', 'iinvertedbreve', 'odblgrave', 'oinvertedbreve', 'rdblgrave', 'rinvertedbreve', 'udblgrave', 'uinvertedbreve', 'scommaaccent', 'tcommaaccent', 'odieresismacron', 'otildemacron', 'odotaccentmacron', 'ymacron', 'schwa', 'adotbelow', 'ahookabove', 'acircumflexacute', 'acircumflexgrave', 'acircumflexhookabove', 'acircumflextilde', 'acircumflexdotbelow', 'abreveacute', 'abrevegrave', 'abrevehookabove', 'abrevetilde', 'abrevedotbelow', 'edotbelow', 'ehookabove', 'etilde', 'ecircumflexacute', 'ecircumflexgrave', 'ecircumflexhookabove', 'ecircumflextilde', 'ecircumflexdotbelow', 'ihookabove', 'idotbelow', 'odotbelow', 'ohookabove', 'ocircumflexacute', 'ocircumflexgrave', 'ocircumflexhookabove', 'ocircumflextilde', 'ocircumflexdotbelow', 'ohornacute', 'ohorngrave', 'ohornhookabove', 'ohorntilde', 'ohorndotbelow', 'udotbelow', 'uhookabove', 'uhornacute', 'uhorngrave', 'uhornhookabove', 'uhorntilde', 'uhorndotbelow', 'ygrave', 'ydotbelow', 'yhookabove', 'ytilde', 'wgrave', 'wacute', 'wdieresis', 'grave', 'acute', 'dieresis', 'macron', 'cedilla', 'circumflex', 'caron', 'firsttonechinese', 'breve', 'dotaccent', 'ring', 'ogonek', 'tilde', 'hungarumlaut', 'hookabove', 'breveinverted', 'dblgrave', 'horn', 'dotbelow', 'dieresisbelow', 'commaaccent', 'brevebelow', 'macronbelow', 'commaaccentturned', 'gravecomb', 'acutecomb', 'circumflexcomb', 'tildecomb', 'macroncomb', 'brevecomb', 'dotaccentcomb', 'dieresiscomb', 'hookabovecomb', 'ringcomb', 'hungarumlautcomb', 'caroncomb', 'breveinvertedcomb', 'dblgravecomb', 'horncomb', 'dotbelowcomb', 'dieresisbelowcomb', 'commaaccentcomb', 'cedillacomb', 'ogonekcomb', 'brevebelowcomb', 'macronbelowcomb', 'commaaccentturnedcomb', 'gravecomb-stack', 'acutecomb-stack', 'dieresiscomb-stack', 'macroncomb-stack', 'circumflexcomb-stack', 'caroncomb-stack', 'brevecomb-stack', 'dotaccentcomb-stack', 'ringcomb-stack', 'tildecomb-stack', 'hungarumlautcomb-stack', 'hookabovecomb-stack', 'breveinvertedcomb.stack', 'dblgravecomb-stack', 'grave-stack', 'acute-stack', 'circumflex-stack', 'tilde-stack', 'macron-stack', 'breve-stack', 'dotaccent-stack', 'dieresis-stack', 'hookabove-stack', 'ring-stack', 'hungarumlaut-stack', 'caron-stack', 'breveinverted-stack', 'dblgrave-stack', 'diagonalbarl', 'diagonalbaro', 'engtail', 'horizontalbarlc', 'alpha', 'alphatonos', 'beta', 'gamma', 'delta', 'epsilon', 'epsilontonos', 'zeta', 'eta', 'etatonos', 'theta', 'iota', 'iotadieresistonos', 'iotatonos', 'iotadieresis', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'omicrontonos', 'pi', 'rho', 'finalsigma', 'sigma', 'tau', 'upsilon', 'upsilondieresistonos', 'upsilondieresis', 'upsilontonos', 'phi', 'chi', 'psi', 'omega', 'omegatonos', 'kaisymbol', 'anoteleia', 'tonos', 'tonoscomb', 'dieresistonoscomb', 'acyr', 'abrevecyr', 'adieresiscyr', 'be', 've', 'ghe', 'gje', 'de', 'ie', 'io', 'iebrevecyr', 'zhe', 'zhebrevecyr', 'zhedieresiscyr', 'ze', 'icyr', 'ishort', 'igravecyr', 'ka', 'kje', 'el', 'em', 'en', 'ocyr', 'odieresiscyr', 'pe', 'er', 'es', 'te', 'ucyr', 'ushort', 'umacroncyr', 'udieresiscyr', 'uhungarumlautcyr', 'ef', 'ha', 'tse', 'che', 'sha', 'shcha', 'hard', 'yeru', 'soft', 'ecyr', 'yu', 'ya', 'dje', 'ieukran', 'dze', 'iukran', 'yi', 'je', 'lje', 'nje', 'tshe', 'dzhe', 'gheup', 'ghestroke', 'zhedescender', 'zedescendercyr', 'kadescender', 'kaverticalstrokecyr', 'kabashkircyr', 'endescender', 'esdescendercyr', 'tedescender-cy', 'ustraight', 'ustraightstroke', 'hadescender', 'chedescender-cy', 'cheverticalstroke-cy', 'shha', 'palochka', 'schwacyr', 'obarcyr', 'hastroke-cy', 've.bgr', 'ghe.bgr', 'de.bgr', 'i.bgr', 'igrave.bgr', 'zhe.bgr', 'ze.bgr', 'ka.bgr', 'el.bgr', 'en.bgr', 'pe.bgr', 'te.bgr', 'tse.bgr', 'che.bgr', 'sha.bgr', 'shcha.bgr', 'hard.bgr', 'soft.bgr', 'yu.bgr', 'ishort.bgr', 'be.locl', 'ghe.locl', 'de.locl', 'pe.locl', 'te.locl', 'amacroncyr', 'iemacroncyr', 'omacroncyr', 'obrevecyr', 'emacroncyr', 'ebrevecyr', 'yamacron', 'yumacron', 'breve.cyr', 'yi-dieresis', 'cy-descender', 'breve.cyrcomb', 'yi-dieresiscomb', 'cy-descendercomb', 'u-stroke', 'obarcyr-stroke', 'hacyr-stroke', 'yu-dash', 'idot', ]

XOUC = XTUC = YTUC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Germandbls', 'paragraph', 'ordfeminine', 'ordmasculine', 'quotesingle', 'quotedbl', 'ampersand', 'questiondown', 'question', 'exclamdown', 'exclam', 'parenleft', 'slash', 'parenright', 'bracketleft', 'backslash', 'bracketright', 'braceleft', 'bar', 'braceright', 'brokenbar', 'asterisk', 'comma', 'period', 'colon', 'semicolon', 'ellipsis', 'periodcentered', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotedblleft', 'quotedblright', 'quotedblbase', 'guilsinglleft', 'guilsinglright', 'guillemotleft', 'guillemotright', 'underscore', 'hyphen', 'hyphentwo', 'figuredash', 'endash', 'emdash', 'threequartersemdash', 'softhyphen', 'dagger', 'daggerdbl', 'bullet', 'at', 'copyright', 'registered', 'trademark', 'section', 'asciicircum', 'asciitilde', 'divisionslash', 'primemod', 'doubleprimemod', 'apostrophemod', 'horizontalbar', 'minute', 'second', 'leftanglebracket', 'rightanglebracket', 'micro', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'AE', 'Ccedilla', 'Egrave', 'Eacute', 'Ecircumflex', 'Edieresis', 'Igrave', 'Iacute', 'Icircumflex', 'Idieresis', 'Eth', 'Ntilde', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'Oslash', 'Ugrave', 'Uacute', 'Ucircumflex', 'Udieresis', 'Yacute', 'Thorn', 'Amacron', 'Abreve', 'Aogonek', 'Cacute', 'Ccircumflex', 'Cdotaccent', 'Ccaron', 'Dcaron', 'Dcroat', 'Emacron', 'Ebreve', 'Edotaccent', 'Eogonek', 'Ecaron', 'Gcircumflex', 'Gbreve', 'Gdotaccent', 'Gcommaaccent', 'Hcircumflex', 'Hbar', 'Itilde', 'Imacron', 'Ibreve', 'Iogonek', 'Idotaccent', 'IJ', 'Jcircumflex', 'Kcommaaccent', 'Lacute', 'Lcommaaccent', 'Lcaron', 'Ldot', 'Lslash', 'Nacute', 'Ncommaaccent', 'Ncaron', 'Eng', 'Omacron', 'Obreve', 'Ohungarumlaut', 'OE', 'Racute', 'Rcommaaccent', 'Rcaron', 'Sacute', 'Scircumflex', 'Scedilla', 'Scaron', 'Tcedilla', 'Tcaron', 'Tbar', 'Utilde', 'Umacron', 'Ubreve', 'Uring', 'Uhungarumlaut', 'Uogonek', 'Wcircumflex', 'Ycircumflex', 'Ydieresis', 'Zacute', 'Zdotaccent', 'Zcaron', 'Ohorn', 'Uhorn', 'DZcaron', 'Dzcaron', 'IJacute', 'Jacute.loclNLD', 'LJ', 'Lj', 'NJ', 'Nj', 'Gcaron', 'Oogonek', 'Aringacute', 'AEacute', 'Oslashacute', 'Adblgrave', 'Ainvertedbreve', 'Edblgrave', 'Einvertedbreve', 'Idblgrave', 'Iinvertedbreve', 'Odblgrave', 'Oinvertedbreve', 'Rdblgrave', 'Rinvertedbreve', 'Udblgrave', 'Uinvertedbreve', 'Scommaaccent', 'Tcommaaccent', 'Odieresismacron', 'Otildemacron', 'Odotaccentmacron', 'Ymacron', 'Schwa', 'Adotbelow', 'Ahookabove', 'Acircumflexacute', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Acircumflexdotbelow', 'Abreveacute', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Abrevedotbelow', 'Edotbelow', 'Ehookabove', 'Etilde', 'Ecircumflexacute', 'Ecircumflexgrave', 'Ecircumflexhookabove', 'Ecircumflextilde', 'Ecircumflexdotbelow', 'Ihookabove', 'Idotbelow', 'Odotbelow', 'Ohookabove', 'Ocircumflexacute', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Ocircumflexdotbelow', 'Ohornacute', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Ohorndotbelow', 'Udotbelow', 'Uhookabove', 'Uhornacute', 'Uhorngrave', 'Uhornhookabove', 'Uhorntilde', 'Uhorndotbelow', 'Ygrave', 'Ydotbelow', 'Yhookabove', 'Ytilde', 'Wgrave', 'Wacute', 'Wdieresis', 'diagonalbarO', 'engtail', 'horizontalbarH', 'grave.case', 'acute.case', 'dieresis.case', 'macron.case', 'cedilla.case', 'circumflex.case', 'caron.case', 'breve.case', 'dotaccent.case', 'ring.case', 'ogonek.case', 'tilde.case', 'hungarumlaut.case', 'hookabove.case', 'breveinverted.case', 'dblgrave.case', 'horn.case', 'dotbelow.case', 'dieresisbelow.case', 'commaaccent.case', 'brevebelow.case', 'macronbelow.case', 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', 'grave-stack.case', 'acute-stack.case', 'dieresis-stack.case', 'macron-stack.case', 'circumflex-stack.case', 'caron-stack.case', 'breve-stack.case', 'dotaccent-stack.case', 'ring-stack.case', 'tilde-stack.case', 'hungarumlaut-stack.case', 'hook-stack.case', 'breveinverted-stack.case', 'dblgrave-stack.case', 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', 'Alpha', 'Alphatonos', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Epsilontonos', 'Zeta', 'Eta', 'Etatonos', 'Theta', 'Iota', 'Iotatonos', 'Iotadieresis', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Omicrontonos', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Upsilontonos', 'Upsilondieresis', 'Phi', 'Chi', 'Psi', 'Omega', 'Omegatonos', 'Kaisymbol', 'ohm', 'tonos.case', 'dieresistonos.case', 'tonoscomb.case', 'dieresistonoscomb.case', 'Dje', 'Ieukran', 'Dze', 'Iukran', 'Yi', 'Je', 'Lje', 'Nje', 'Tshe', 'Dzhe', 'Acyr', 'Abrevecyr', 'Adieresiscyr', 'Be', 'Ve', 'Ghe', 'Gje', 'De', 'Ie', 'Io', 'Iebrevecyr', 'Zhe', 'Zhebrevecyr', 'Zhedieresiscyr', 'Ze', 'Icyr', 'Igravecyr', 'Ishort', 'Ka', 'Kje', 'El', 'Em', 'En', 'Ocyr', 'Odieresiscyr', 'Pe', 'Er', 'Es', 'Te', 'Ucyr', 'Ushort', 'Umacroncyr', 'Udieresiscyr', 'Uhungarumlautcyr', 'Ef', 'Ha', 'Tse', 'Che', 'Sha', 'Shcha', 'Hard', 'Yeru', 'Soft', 'Ecyr', 'Yu', 'Ya', 'Gheup', 'Ghestroke', 'Zhedescender', 'Zedescendercyr', 'Kadescender', 'Kaverticalstrokecyr', 'Kabashkircyr', 'Endescender', 'Esdescendercyr', 'Tedescender-cy', 'Ustraight', 'Ustraightstroke', 'Hadescender', 'Chedescender-cy', 'Cheverticalstroke-cy', 'Shha', 'Palochka', 'Schwacyr', 'Obarcyr', 'Hastroke-cy', 'De.bgr', 'Zhe.bgr', 'Ka.bgr', 'El.bgr', 'Amacroncyr', 'Iemacroncyr', 'Omacroncyr', 'Obrevecyr', 'Emacroncyr', 'Ebrevecyr', 'Yamacron', 'Yumacron', 'breve.cyr.case', 'Yi-dieresis.case', 'Cy-descender.case', 'breve.cyrcomb.case', 'Yi-dieresiscomb.case', 'Cy-descendercomb.case', 'U-stroke', 'Obarcyr-stroke', 'Hacyr-stroke', 'Yu-dash.case', ]

YTAS = [ 'b', 'd', 'f', 'h', 'k', 'l', 'germandbls', 'eth', 'thorn', 'dcroat', 'hcircumflex', 'hbar', 'lacute', 'beta', 'delta', 'zeta', 'theta', 'lambda', 'xi', 'phi', 'psi', 'be', 'dje', 'tshe', 'gheup', 've.bgr', 'zhe.bgr', 'be.locl', ]

YTDE = [ 'g', 'j', 'p', 'q', 'y', 'jdotless', 'thorn', 'engtail', 'beta', 'gamma', 'zeta', 'eta', 'mu', 'xi', 'rho', 'finalsigma', 'phi', 'chi', 'psi', 'kaisymbol', 'Dzhe', 'De', 'Tse', 'de', 'tse', 'dzhe', 'ustraight', 'De.bgr', 'ze.bgr','cy-descendercomb', ]

YTOS = ['C', 'G', 'J', 'O', 'Q', 'S', 'U', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'Germandbls', 'germandbls', 'question', 'at', 'ae', 'eth', 'OE', 'oe', 'thorn', 'dollar', 'sterling', 'Euro', 'lira', 'numero', 'florin', 'coloncurrency', 'uni20B2', 'uni20B5', 'hryvnia', 'dollar.rvrn', 'coloncurrency.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'two', 'three', 'five', 'six', 'eight', 'nine', 'zero.prop', 'two.prop', 'three.prop', 'five.prop', 'six.prop', 'eight.prop', 'nine.prop', 'ordfemenine', 'ordmasculine', 'ampersand', 'questiondown', 'question', 'zerosuperior', 'onesuperior', 'twosuperior', 'threesuperior', 'foursuperior', 'Schwa', 'schwa', 'Theta', 'Omega', 'alpha', 'beta', 'delta', 'epsilon', 'eta', 'theta', 'iota', 'lambda', 'mu', 'pi', 'rho', 'finalsigma', 'sigma', 'tau', 'upsilon', 'phi', 'psi', 'omega', 'Ieukran', 'Lje', 'Ze', 'El', 'Ucyr', 'Ecyr', 'be', 'ze', 'el', 'ecyr', 'ieukran', 'lje', 've.bgr', 'ghe.bgr', 'ze.bgr', 'sha.bgr', 'hard.bgr', 'soft.bgr', 'be.locl', ]

XTTW = YTTL = [ 'A', 'M', 'N', 'V', 'W', 'Y', 'v', 'w', 'y' ]

STLI = STLO = [ 'a', 'b', 'c', 'd', 'e', 'g', 'h', 'm', 'n', 'o', 'p', 'q', 's', 'u', 'ae', 'eth', 'thorn', 'oe', 'schwa', 'alpha', 'beta', 'delta', 'epsilon', 'eta', 'theta', 'rho', 'finalsigma', 'sigma', 'upsilon', 'phi', 'psi', 'omega', 'be', 'ze', 'che', 'ecyr', 'ya', 'ieukran', 'lje', 'nje', 'cheverticalstroke-cy', 've.bgr', 'ghe.bgr', 'ze.bgr', 'sha.bgr', 'hard.bgr', 'soft.bgr', 'be.locl', ]

STUI = STUO = [ 'B', 'C', 'D', 'G', 'J', 'O', 'P', 'R', 'Q', 'S', 'U', 'dollar', 'sterling', 'Euro', 'lira', 'peseta', 'dong', 'rupeeIndian', 'liraTurkish', 'manat', 'ruble', 'numero', 'coloncurrency', 'uni20B1', 'uni20B2', 'uni20B5', 'hryvnia', 'dollar.rvrn', 'cent.rvrn', 'coloncurrency.rvrn', 'uni20B1.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'two', 'three', 'five', 'six', 'eight', 'nine', 'zero.prop', 'two.prop', 'three.prop', 'five.prop', 'six.prop', 'eight.prop', 'nine.prop', 'cent', 'currency', 'ordfeminine', 'ordmasculine', 'ampersand', 'questiondown', 'question', 'zerosuperior', 'twosuperior', 'threesuperior', 'Thorn', 'OE', 'Schwa', 'Theta', 'Phi', 'Psi', 'Omega', 'Dje', 'Ieukran', 'Lje', 'Nje', 'Tshe', 'Be', 'Ze', 'Che', 'Hard', 'Soft', 'Ecyr', 'Ya', 'Cheverticalstroke-cy', 'Shha', ]

XTUD = [ 'A', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'Amacron', 'Abreve', 'Aogonek', 'Aringacute', 'Adblgrave', 'Ainvertedbreve', 'Adotbelow', 'Ahookabove', 'Acircumflexacute', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Acircumflexdotbelow', 'Abreveacute', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Abrevedotbelow', 'I', 'K', 'Kcommaaccent', 'M', 'N', 'Ntilde', 'Nacute', 'Ncommaaccent', 'Ncaron', 'V', 'W', 'Wcircumflex', 'Wgrave', 'Wacute', 'Wdieresis', 'AE', 'AEacute', 'Eng', 'Alpha', 'Alphatonos', 'Kappa', 'Mu', 'Nu', 'Kje', 'Acyr', 'Abrevecyr', 'Adieresiscyr', 'Em', 'j', 'Nj', 'naira', 'won', 'numero', 'Amacroncyr', 'diagonalbarO', 'diagonalbarl', 'engtail', 'hookabovecomb-stack', 'idot', 'jdotless', 'caroncomb.alt', 'naira.rvrn', 'won.rvrn', 'breve.cyrcomb.case', 'acute.case', 'grave.case', 'circumflex.case', 'caron.case', 'breve.case', 'macron.case', 'dieresis.case', 'dotaccent.case', 'ring.case', 'cedilla.case', 'acute-stack.case', 'acutecomb-stack.case', 'acutecomb.case', 'acutecombstack.case', 'breve-stack.case', 'brevebelow.case', 'brevebelowcomb.case', 'brevecomb-stack.case', 'brevecomb.case', 'brevecombstack.case', 'breveinverted-stack.case', 'breveinverted.case', 'breveinvertedcomb-stack.case', 'breveinvertedcomb.case', 'caron-stack.case', 'caroncomb-stack.case', 'caroncomb.case', 'cedillacomb.case', 'circumflex-stack.case', 'circumflexcomb-stack.case', 'circumflexcomb.case', 'circumflexcombstack.case', 'commaaccent.case', 'commaaccentcomb.case', 'dblgrave-stack.case', 'dblgrave.case', 'dblgravecomb-stack.case', 'dblgravecomb.case', 'dieresis-stack.case', 'dieresisbelow.case', 'dieresisbelowcomb.case', 'dieresiscomb-stack.case', 'dieresiscomb.case', 'dieresiscombstack.case', 'dotaccent-stack.case', 'dotaccentcomb-stack.case', 'dotaccentcomb.case', 'dotaccentcombstack.case', 'dotbelow.case', 'dotbelowcomb.case', 'grave-stack.case', 'gravecomb-stack.case', 'gravecomb.case', 'gravecombstack.case', 'hook-stack.case', 'hookabove.case', 'hookabovecomb.case', 'hookabovecombstack.case', 'hookcomb-stack.case', 'horn.case', 'horncomb.case', 'hungarumlaut-stack.case', 'hungarumlaut.case', 'hungarumlautcomb-stack.case', 'hungarumlautcomb.case', 'macron-stack.case', 'macronbelow.case', 'macronbelowcomb.case', 'macroncomb-stack.case', 'macroncomb.case', 'macroncombstack.case', 'ogonek.case', 'ogonekcomb.case', 'ring-stack.case', 'ringcomb-stack.case', 'ringcomb.case', 'tilde-stack.case', 'tilde.case', 'tildecomb-stack.case', 'tildecomb.case', 'tildecombstack.case', 'tonoscomb.case', 'A.ital', 'I.ital', 'K.ital', 'M.ital', 'N.ital', 'V.ital', 'W.ital', ]

XTUR = [ 'C', 'G', 'I', 'O', 'Q', 'S', 'Ccedilla', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'Oslash', 'Cacute', 'Ccircumflex', 'Cdotaccent', 'Ccaron', 'Gcircumflex', 'Gbreve', 'Gdotaccent', 'Gcommaaccent', 'Omacron', 'Obreve', 'Ohungarumlaut', 'OE', 'Sacute', 'Scircumflex', 'Scedilla', 'Scaron', 'Ohorn', 'Gcaron', 'Oogonek', 'Oslashacute', 'Odblgrave', 'Oinvertedbreve', 'Scommaaccent', 'Odieresismacron', 'Otildemacron', 'Odotaccentmacron', 'Odotbelow', 'Ohookabove', 'Ocircumflexacute', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Ocircumflexdotbelow', 'Ohornacute', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Ohorndotbelow', 'diagonalbarO', 'Omicron', 'Omicrontonos', 'tonoscomb.case', 'Dze', 'Ocyr', 'Odieresiscyr', 'Es', 'Yu', 'Yumacron', 'Esdescendercyr', 'Obarcyr', 'Obarcyr-stroke', 'Yu-dash.case', 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', 'grave-stack.case', 'acute-stack.case', 'dieresis-stack.case', 'macron-stack.case', 'circumflex-stack.case', 'caron-stack.case', 'breve-stack.case', 'dotaccent-stack.case', 'ring-stack.case', 'tilde-stack.case', 'hungarumlaut-stack.case', 'hook-stack.case', 'breveinverted-stack.case', 'dblgrave-stack.case', 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', 'grave.case', 'acute.case', 'dieresis.case', 'macron.case', 'cedilla.case', 'circumflex.case', 'caron.case', 'breve.case', 'dotaccent.case', 'ring.case', 'ogonek.case', 'tilde.case', 'hungarumlaut.case', 'hookabove.case', 'breveinverted.case', 'dblgrave.case', 'horn.case', 'dotbelow.case', 'dieresisbelow.case', 'commaaccent.case', 'brevebelow.case', 'macronbelow.case', 'C.ital', 'G.ital', 'I.ital', 'O.ital', 'Q.ital', 'S.ital', ]

YOPE = [ 'E', 'F', 'AE', 'OE', 'Xi', ]

ALL = [ 'space', ]

def makeGlyphs(src_font, dst_font, glyphs, in_set):

    src_fontName = SRC_PATH + src_font
    src_font = OpenFont(src_fontName, showInterface=False)
    
    dst_fontName = DST_PATH + dst_font
    dst_font = OpenFont(dst_fontName, showInterface=False)
    
    if in_set:
    
        for glyph in glyphs:
            
            dst_font[glyph] = src_font[glyph]
    
    else:
        
        for glyph in src_font:
            
            if glyph.name not in glyphs:
                
                dst_font[glyph.name] = src_font[glyph.name]
                
            
    dst_font.save()
    print('Propagated glyphs at ' + dst_fontName)


# # # XOPQs
# makeGlyphs('Roboto-Delta-XOPQ2.ufo', 'Roboto-Delta-XOFI2.ufo', XOFI, True)
# makeGlyphs('Roboto-Delta-XOPQ310.ufo', 'Roboto-Delta-XOFI300.ufo', XOFI, True)
# makeGlyphs('Roboto-Delta-XOPQ2.ufo', 'Roboto-Delta-XOLC2.ufo', XOLC, True)
# makeGlyphs('Roboto-Delta-XOPQ310.ufo', 'Roboto-Delta-XOLC294.ufo', XOLC, True)
# makeGlyphs('Roboto-Delta-XOPQ2.ufo', 'Roboto-Delta-XOUC2.ufo', XOUC, True)
# makeGlyphs('Roboto-Delta-XOPQ310.ufo', 'Roboto-Delta-XOUC310.ufo', XOUC, True)

# # XTRAs

# # # XTFI 
makeGlyphs('Roboto-Delta-XTRA244.ufo', 'Roboto-Delta-XTFI244.ufo', XTFI, True)
makeGlyphs('Roboto-Delta-XTRA741.ufo', 'Roboto-Delta-XTFI741.ufo', XTFI, True)
makeGlyphs('Roboto-Delta-XTRA244-opsz144-wdth25-wght100.ufo', 'Roboto-Delta-XTFI244-opsz144-wdth25-wght100.ufo', XTFI, True)
makeGlyphs('Roboto-Delta-XTRA741-opsz144-wdth151-wght100.ufo', 'Roboto-Delta-XTFI741-opsz144-wdth151-wght100.ufo', XTFI, True)

# # # XTLC
makeGlyphs('Roboto-Delta-XTRA244.ufo', 'Roboto-Delta-XTLC244.ufo', XTLC, True)
makeGlyphs('Roboto-Delta-XTRA741.ufo', 'Roboto-Delta-XTLC741.ufo', XTLC, True)
makeGlyphs('Roboto-Delta-XTRA244-opsz144-wdth25-wght100.ufo', 'Roboto-Delta-XTLC244-opsz144-wdth25-wght100.ufo', XTLC, True)
makeGlyphs('Roboto-Delta-XTRA741-opsz144-wdth151-wght100.ufo', 'Roboto-Delta-XTLC741-opsz144-wdth151-wght100.ufo', XTLC, True)

# # # XTUC
makeGlyphs('Roboto-Delta-XTRA244.ufo', 'Roboto-Delta-XTUC244.ufo', XTUC, True)
makeGlyphs('Roboto-Delta-XTRA741.ufo', 'Roboto-Delta-XTUC741.ufo', XTUC, True)
makeGlyphs('Roboto-Delta-XTRA244-opsz144-wdth25-wght100.ufo', 'Roboto-Delta-XTUC244-opsz144-wdth25-wght100.ufo', XTUC, True)
makeGlyphs('Roboto-Delta-XTRA741-opsz144-wdth151-wght100.ufo', 'Roboto-Delta-XTUC741-opsz144-wdth151-wght100.ufo', XTUC, True)

# # # YTAS
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTAS665.ufo', YTAS, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTAS875.ufo', YTAS, False)

# # # YTDE
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTDE-100.ufo', YTDE, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTDE-310.ufo', YTDE, False)

# # # YTFI
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTFI270.ufo', YTFI, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTFI793.ufo', YTFI, False)

# # # YTLC
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTLC426.ufo', YTLC, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTLC584.ufo', YTLC, False)

# # # YTUC
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTUC528.ufo', YTUC, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTUC778.ufo', YTUC, False)

# # # YTOS
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTOS0.ufo', YTOS, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTOS50.ufo', YTOS, False)

# # # XTTW
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-XTTW0.ufo', XTTW, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-XTTW30.ufo', XTTW, False)

# # # YTTL
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTTL0.ufo', YTTL, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-YTTL50.ufo', YTTL, False)

# # # STLI
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STLI2.ufo', STLI, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STLI412.ufo', STLI, False)

# # # STLO
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STLO2.ufo', STLO, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STLO426.ufo', STLO, False)

# # # STUI
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STUI2.ufo', STUI, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STUI736.ufo', STUI, False)

# # # STUO
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STUO2.ufo', STUO, False)
# makeGlyphs('Roboto-Delta-wght400.ufo', 'Roboto-Delta-STUO722.ufo', STUO, False)

# # # XTUD
# makeGlyphs('Roboto-Delta-XTRA741.ufo', 'Roboto-Delta-XTUD741.ufo', XTUD, True)

# # # XTUR
# makeGlyphs('Roboto-Delta-XTRA741.ufo', 'Roboto-Delta-XTUR741.ufo', XTUR, True)

# # # YOPE
# makeGlyphs('Roboto-Delta-YOPQ280.ufo', 'Roboto-Delta-YOPE280.ufo', YOPE, True)

