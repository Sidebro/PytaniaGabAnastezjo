from __future__ import annotations

import os
import random

from flask import Flask, jsonify, render_template


app = Flask(__name__)

CATEGORIES = {
    "Resuscytacja i stany zagrożenia życia": {
        "label": "Resuscytacja i stany zagrożenia życia",
        "questions": [
            "Mechanizmy zatrzymania krążenia u dorosłych.",
            "Mechanizmy zatrzymania krążenia u dzieci.",
            "Co to są odwracalne przyczyny zatrzymania krążenia?",
            "W jaki sposób można udrożnić drogi oddechowe.",
            "Schemat resuscytacji krążeniowo-oddechowej w migotaniu komór.",
            "Schemat resuscytacji krążeniowo-oddechowej w asystolii.",
            "Schemat resuscytacji krążeniowo-oddechowej w czynności elektrycznej bez tętna (PEA).",
            "W jaki sposób podajemy/dawkujemy adrenalinę, w stanach zagrożenia życia.",
            "Schemat resuscytacji krążeniowo-oddechowej dziecka 5 letniego.",
            "Różnica między kardiowersją a defibrylacją.",
            "Defibrylacja - wskazania i sposób wykonania (AED).",
            "Wstępne postępowanie w ostrych zespołach wieńcowych.",
            "Kiedy rozpoczynać i kiedy kończyć resuscytację. Od czego zależy skuteczność resuscytacji.",
            "Pacjent z odma opłucnową prężną – objawy kliniczne, sposób postępowania.",
            "Tamponada serca jako stan zagrożenia życia – definicja, rozpoznanie, postępowanie.",
            "Duszność krtaniowa u dziecka leczenie.",
            "Dostęp doszpikowy- wskazania/zastosowanie.",
            "Pacjent z urazem wielonarządowym - postępowanie wstępne, FAST.",
            "Kwasica metaboliczna – przyczyny, rozpoznanie, postępowanie.",
            "Kwasica oddechowa – przyczyny, rozpoznanie, postępowanie.",
            "Przydatność pulsoksymetrii w monitorowaniu chorych w stanie zagrożenia życia.",
            "Zastosowanie i dawkowanie atropiny.",
            "Charakterystyka amin presyjnych (podstawowe różnice i zastosowanie w różnych przyczynach hipotensji)/",
            "Wskazania i bezpieczne stosowanie amiodaronu.",
            "Podstawowe cele opieki poresuscytacyjnej.",
            "Adenozyna – wskazania i sposób zastosowania.",
            "Bezpieczeństwo czynności resuscytacyjnych w warunkach szpitalnego i pozaszpitalnego zatrzymania krążenia.",
            "Zaburzenia rytmu serca zagrażające zatrzymaniem krążenia.",
            "Niepodejmowanie czynności resuscytacyjnych – Kruchość, Kacheksja, Stan terminalny.",
            "Powikłania poresuscytacyjne – ocena, rokowanie."
        ],
    },
    "Znieczulenie ogólne i regionalne": {
        "label": "Znieczulenie ogólne i regionalne",
        "questions": [
            "Przygotowanie pacjenta do operacji, zasady dotyczące picia płynów i spożywania pokarmów oraz leków przyjmowanych przewlekle w okresie przedoperacyjnym.",
            "Przedoperacyjna ocena stanu ogólnego w skali ASA.",
            "Przeciwwskazania do znieczulenia w trybie planowym/pilnym.",
            "Premedykacja: cel stosowania, wybór środków, wady.",
            "Znieczulenie ogólne - elementy składowe.",
            "Indukcja znieczulenia ogólnego – opis procedury.",
            "Ogólna charakterystyka środków zwiotczających mięśnie.",
            "Monitorowanie układu oddechowego.",
            "Monitorowanie układu krążenia.",
            "Przyrządowe udrażnianie dróg oddechowych do zabiegu operacyjnego.",
            "Maska krtaniowa a rurka intubacyjna - różnice w zastosowaniu.",
            "Intubacja tchawicy – wskazania, technika, weryfikacja położenia rurki, powikłania.",
            "Monitorowanie pacjenta w sali pooperacyjnej.",
            "Kryteria wypisu pacjenta z sali pooperacyjnej.",
            "Postępowanie mające na celu ograniczenie ryzyka przedostania się treści żołądkowej do dróg oddechowych u dorosłego pacjenta z niedrożnością przewodu pokarmowego.",
            "Świadoma zgoda na wykonanie procedury medycznej.",
            "Powikłania blokad centralnych.",
            "Znieczulenie podpajęczynówkowe – anatomia przestrzeni podpajęczynówkowej, wskazania, sposób wykonania, postępowanie.",
            "Znieczulenie zewnątrzoponowe - anatomia przestrzeni zewnątrzoponowej, wskazania, sposób wykonania, postępowanie.",
            "Różnica między znieczuleniem podpajęczynówkowym a zewnątrzoponowym.",
            "Środki miejscowo znieczulające – adjuwanty, dawkowanie, czas działania. (lidokaina, bupiwakaina).",
            "Przedawkowanie względne i bezwzględne środków miejscowo znieczulających.",
            "Postępowanie przy przedawkowaniu środków miejscowo znieczulających.",
            "Wskazania i przeciwwskazania do znieczulenia zewnątrzoponowego porodu.",
            "Metody znieczulenia regionalnego kończyny górnej - rodzaje, powikłania, wskazania.",
            "Metody znieczulenia regionalnego kończyny dolnej - rodzaje, powikłania, wskazania.",
            "Opieka pooperacyjna nad pacjentem po blokadzie centralnej.",
            "Popunkcyjne bóle głowy – rozpoznawanie, leczenie.",
            "Wskazania i przeciwwskazania do wykonywania blokad centralnych.",
            "Anestezja regionalna u dzieci.",
        ],
    },
    "Intensywna Terapia i Ból": {
        "label": "Intensywna Terapia i Ból",
        "questions": [
            "Drabina analgetyczna – schemat leczenia bólu.",
            "Leczenie bólu ostrego pooperacyjnego.",
            "Analgezja multimodalna.",
            "Metody oceny natężenia bólu - Skale oceny bólu.",
            "Łagodzenie dolegliwości porodowych.",
            "Anestezja regionalna w leczeniu bólu pooperacyjnego - techniki ciągłe.",
            "Paracetamol – dawkowanie, objawy toksyczne, leczenie zatrucia.",
            "Niesteroidowe leki przeciwzapalne – zasady stosowania w okresie okołooperacyjnym.",
            "Metamizol (pyralgina – dawkowanie, jego miejsce w drabinie analgetycznej.",
            "Pacjent z urazem wielomiejscowym – jakie leki przeciwbólowe można zastosować w opiece przedszpitalnej/SOR.",
            "Leki przeciwbólowe u pacjentki ciężarnej.",
            "Śmierć mózgu (definicja, diagnostyka, dlaczego jest wykonywana diagnostyka śmierci mózgu).",
            "Zgoda domniemana – pobranie narządów, sposoby wyrażania sprzeciwu.",
            "Wkłucie centralne, wskazania, powikłania, opieka nad cewnikiem centralnym.",
            "Kwalifikacja pacjenta do leczenia w OIT.",
            "Terapia uporczywa/daremna.",
            "Przeciwwskazania do leczenia w OIT.",
            "Procedura DNR („nie podejmuj resuscytacji”, „pozwól na naturalną śmierć”).",
            "Interpretacja przykładowego badania gazometrycznego: technika i miejsce pobrania.",
            "Ostra niewydolność oddechowa – przyczyny, rozpoznanie, postępowanie.",
            "Wentylacja zastępcza – wskazania, monitorowanie.",
            "Co to jest ARDS?",
            "Definicja wstrząsu, jego rodzaje.",
            "Wstrząs hipowolemiczny – patomechanizm, objawy, leczenie.",
            "Wstrząs septyczny – patomechanizm, objawy, leczenie.",
            "Wstrząs anafilaktyczny – patomechanizm, objawy, leczenie.",
            "Wstrząs kardiogenny – patomechanizm, objawy, leczenie.",
            "Płynoterapia we wstrząsie niekardiogennym u dziecka.",
            "Tlenoterapia wskazania sposoby monitorowania, efekty niepożądane.",
            "Kapnografia- zastosowanie w monitorowaniu wentylacji.",
            "Miejsce USG w diagnostyce stanów nagłych/ anestezjologii i intensywnej terapii.",
            "Charakterystyka obwodowych dostępów dożylnych - wskazania",
        ],
    },
}

QUESTION_POOLS = {}


def reset_question_pool(category: str) -> list[str] | None:
    category_data = CATEGORIES.get(category)

    if category_data is None:
        return None

    QUESTION_POOLS[category] = list(category_data["questions"])
    return QUESTION_POOLS[category]


def draw_question(category: str) -> tuple[str | None, int | None]:
    pool = QUESTION_POOLS.get(category)

    if pool is None or not pool:
        pool = reset_question_pool(category)

    if pool is None:
        return None, None

    question = random.choice(pool)
    pool.remove(question)
    return question, len(pool)


@app.get("/")
def index():
    return render_template("index.html", categories=CATEGORIES)


@app.get("/api/question/<category>")
def get_question(category: str):
    category_data = CATEGORIES.get(category)

    if category_data is None:
        return jsonify({"error": "Nieznana kategoria."}), 404

    question, remaining = draw_question(category)
    return jsonify(
        {
            "category": category,
            "label": category_data["label"],
            "question": question,
            "remaining": remaining,
            "total": len(category_data["questions"]),
        }
    )


@app.post("/api/reset/<category>")
def reset_category(category: str):
    category_data = CATEGORIES.get(category)

    if category_data is None:
        return jsonify({"error": "Nieznana kategoria."}), 404

    pool = reset_question_pool(category)
    return jsonify(
        {
            "category": category,
            "label": category_data["label"],
            "message": "Pula pytan zostala zresetowana.",
            "remaining": len(pool),
            "total": len(category_data["questions"]),
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
