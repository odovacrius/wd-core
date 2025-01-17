#!/usr/bin/python3
"""

إضافة وصف الأفلام

python pwb.py des/filmnew

"""

#
# (C) Ibrahem Qasim, 2022
#
#
import re
import pywikibot

# ---

from newapi import printe

# ---
# ---
from wd_api import wd_desc
from wd_api import wd_bot

# ---
wikidatasite = pywikibot.Site("wikidata", "wikidata")
repo = wikidatasite.data_repository()
# ---
AskSave = {1: True}
# ---
# def AddDes( item , pa , lang , Qid , keys):


def action_one_item(Qid, pa, lang, keys):
    item = getwditem(pa["item"])
    if not item:
        return
    # desc = MakeDesc(Qid, auth, lang)
    # Summary= 'Bot: - Add descriptions: '+ lang
    keys = sorted(keys)
    # ---

    printe.output(f"keys:{str(keys)}")
    # ---
    descriptions = item.descriptions
    NewDesc = {}
    addedlangs = []
    # ---
    for lang in keys:
        if lang not in descriptions.keys():
            # ---
            lang2 = lang

            # ---
            if MakeDesc(Qid, pa, lang2):
                des = MakeDesc(Qid, pa, lang2)
                NewDesc[lang] = {"language": lang, "value": des}
                dns = ""
                if "endes" in pa:
                    dns = pa["endes"]
                printe.output(f"newar:{des},en:{dns}")
                addedlangs.append(lang)
            else:
                printe.output(f'*no desc for "{lang}"')
    # ---
    if addedlangs:
        qitem = item.title(as_link=False)
        if AskSave[1]:
            printe.output(f"================== + {addedlangs}")
            for lan, value in NewDesc.items():
                printe.output(f"""lang:{lan}, value: \"{value['value']}\"""")
            saaa = pywikibot.input(" Add as descriptions? ")
            if saaa in ["y", "a", ""]:
                if saaa == "a":
                    AskSave[1] = False
                wd_desc.work_api_desc(NewDesc, qitem)
            else:
                printe.output("* rong answer")
        else:
            wd_desc.work_api_desc(NewDesc, qitem)


def getwditem(qitem):
    try:
        item = pywikibot.ItemPage(repo, qitem)
        # ---
        item.get()
        return item
    except BaseException:
        return False


# ---
Comma = {
    "an": " y ",
    "ar": "، و",
    "ast": " y ",
    "ca": " i ",
    "de": " und ",
    "es": " y ",
    "ext": " y ",
    "fr": " et ",
    "he": " ו",
    "gl": " e ",
    "it": " e ",
    "nl": " en ",
    "oc": " e ",
    "pt": " e ",
    "ro": " și ",
    "sv": " och ",
    "en": ", ",
}
Comma2 = {"ar": "، و", "en": ", ", "de": ", ", "fr": ", ", "nl": ", "}


def GetQuery(Qid, lang, keys):
    # ---
    P50 = "P57"
    # ---
    ur = f"SELECT ?item ?{lang} "
    head = "?" + " ?".join([x for x in keys if x != lang])
    ur = ur + head
    ur = ur + " ?endes  ?dates \n WHERE {"
    ur = f"{ur} \n?item wdt:{P50} ?auths . \n?item wdt:{P50} ?auths2 .\n"
    # ---
    sa = " ?item wdt:P31 wd:Q11424 .\n?item wdt:P577 ?date2.\nBIND(year(?date2) AS ?dates). \n"
    sa += 'OPTIONAL { ?item schema:description ?endes. FILTER((LANG(?endes)) = "en") }\n'
    ur = ur + sa

    def fofo(x):
        xx = "OPTIONAL {"
        xx += f'?auths rdfs:label ?{x} filter (lang(?{x}) = "{x}")'
        xx += "} ."
        return xx

    # ---
    OPTIONAL = "\n".join([fofo(x) for x in keys if x != lang])
    ur = ur + OPTIONAL
    # ---
    ur = ur + " \n{"
    ur = f'{ur}?auths2 rdfs:label ?{lang}2 filter (lang(?{lang}2) = "{lang}") .'
    ur = ur + "}\n"
    ur = ur + "OPTIONAL {"
    ur = f'{ur}   ?item schema:description ?itemDes filter(lang(?itemDes) = "{lang}")'
    ur = ur + "} FILTER(!BOUND(?itemDes))\n"  # GROUP BY ?item '
    ur = ur + "SERVICE wikibase:label { "
    ur = f'{ur}     bd:serviceParam wikibase:language "ar,en". ?auths rdfs:label ?{lang}'
    ur = ur + " }}\n"
    # printe.output(ur)
    # ---
    return ur


def Gquery2(json1):
    table = {}
    # table = []
    # for head in json1['head']['vars']:
    for result in json1["results"]["bindings"]:
        q = "item" in result and result["item"]["value"].split("/entity/")[1] or ""
        s = {se: result[se]["value"] for se in result}
        s["item"] = q
        table[q] = s
    return table


# ---
xsxsx = {
    "an": "cinta de ~YEAR~ dirichita por ~AUTHOR~",
    "ar": "فيلم أُصدر سنة ~YEAR~، من إخراج ~AUTHOR~",
    "ast": "película de ~YEAR~ dirixida por ~AUTHOR~",
    "ca": "pel·lícula de ~YEAR~ dirigida per ~AUTHOR~",
    "de": "Film von ~AUTHOR~ (~YEAR~)",
    "es": "película de ~YEAR~ dirigida por ~AUTHOR~",
    "ext": "pinicla de ~YEAR~ dirigía por ~AUTHOR~",
    "fr": "film de ~AUTHOR~, sorti en ~YEAR~",
    "gl": "filme de ~YEAR~ dirixido por ~AUTHOR~",
    # 'he': 'סרט של ~AUTHOR~ משנת ~YEAR~', #warning, avoid mix Latin and Hebrew chars for directors name
    "he": "סרט משנת ~YEAR~",
    "it": "film del ~YEAR~ diretto da ~AUTHOR~",
    "nl": "film uit ~YEAR~ van ~AUTHOR~",
    "oc": "filme de ~YEAR~ dirigit per ~AUTHOR~",
    "pt": "filme de ~YEAR~ dirigido por ~AUTHOR~",
    "ro": "film din ~YEAR~ regizat de ~AUTHOR~",
    "sv": "film från ~YEAR~ regisserad av ~AUTHOR~",
}
filmform = {"film": {
    "ar": "فيلم أُصدر سنة ~YEAR~، من إخراج ~AUTHOR~",
    "en": "~YEAR~ film by ~AUTHOR~",
    "nl": "film uit ~YEAR~ van ~AUTHOR~",
}}
# ---
quaua = """SELECT #DISTINCT
?item ?ar ?nl ?en ?endes  ?dates ?auths
WHERE {
?item wdt:P57 ?auths .
#?item wdt:P57 ?auths2 .
?item wdt:P31 wd:Q11424 .
?item wdt:P577 ?date2.
BIND(year(?date2) AS ?dates).
OPTIONAL { ?item schema:description ?endes. FILTER((LANG(?endes)) = "en") }
OPTIONAL {?auths rdfs:label ?nl filter (lang(?nl) = "nl")} .
OPTIONAL {?auths rdfs:label ?en filter (lang(?en) = "en")} .
#{?auths2 rdfs:label ?ar2 filter (lang(?ar2) = "ar")} .
#OPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "ar")} FILTER(!BOUND(?itemDes))
MINUS {?item schema:description ?itemDes filter(lang(?itemDes) = "ar")}# FILTER(!BOUND(?itemDes))
SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". ?auths rdfs:label ?ar }}

"""


def WorkWithOneLang(Qid, lang, keys):
    printe.output("*<<lightyellow>> WorkWithOneLang: ")
    limit = 200
    # limit = '10000'
    # lang = 'de'
    # keys =
    # try:
    # ---
    quary = quaua
    # quary = GetQuery(Qid , lang, keys)
    quary = quary + "\n limit %d" % limit
    printe.output(quary)
    # ---
    PageList = wd_bot.sparql_generator_url(quary, key="item")
    # ---
    total = len(PageList)
    # ---
    printe.output("* PageList: ")
    for num, pa in enumerate(PageList.keys(), start=1):
        printe.output(pa)
        PageList[pa]["item"] = pa.split("/entity/")[1]
        SAO = filmform[Qid][lang]
        printe.output("<<lightblue>>> %s (%s) :%s/%d : %s" % (lang, SAO, num, total, PageList[pa]["item"]))
        # ---
        action_one_item(Qid, PageList[pa], lang, keys)


# ---
by_list = {"ar": "من تأليف", "en": "by", "fr": "de", "de": "von", "nl": "van", "ca": "per", "cs": "od", "la": "ab", "it": "da", "io": "da", "eo": "de", "da": "af", "pl": "przez", "ro": "de", "es": "por", "sv": "av"}


def MakeDesc(Qid, pa, lang):
    # for lang in language:
    # auth
    description = False
    english = ["en-gb", "en-ca"]
    if lang in english:
        lang = "en"
    # ---
    if lang not in by_list:
        printe.output(f'<<lightblue>>> cant find "by" in by_list for lang: "{lang}"')
        return False
    co = "من أداء " if (Qid == "Q482994") and (lang == "ar") else f"{by_list[lang]} "
    # ---
    if (lang in pa) and (pa[lang] != ""):
        if auth := pa[lang]:
            if lang in filmform[Qid]:
                des = filmform[Qid][lang]
                YEAR = pa["dates"]
                YEARS = YEAR  # .split(',')
                endes = pa["endes"][0]
                # ---
                true_year = ""
                if len(YEARS) > 1:
                    for ye in YEARS:
                        if endes != re.sub(ye, "", endes):
                            true_year = ye
                else:
                    true_year = pa["dates"][0]
                auth2 = Comma[lang].join(auth)
                # ---
                # d = d + ' '                        # الرابط by
                d = re.sub(r"~AUTHOR~", auth2, des)
                d = re.sub(r"~YEAR~", true_year, d)
                # printe.output( 'd' )
                # printe.output( d )
                description = d
    # else:
    # description = False
    if lang == "ar":
        if description and description != re.sub(r"[abcdefghijklmnobqrstuvwxyz]", "", description):
            printe.output(f'<<lightred>> arabic description test failed "{description}".')
            description = False
    return description


def films():
    printe.output("films: ")
    Q = "film"
    # for lang in language:
    keys = filmform[Q].keys()
    WorkWithOneLang(Q, "ar", keys)


# ---
if __name__ == "__main__":
    films()
# ---
