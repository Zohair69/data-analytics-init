"""
Module d'analyse statistique des ventes.
Objectif : nettoyer une liste de transactions, calculer les indicateurs
clés (moyenne, médiane, écart-type, etc.) et détecter les valeurs anormales.
"""

import statistics


def analyser_ventes(transactions):
    """
    Analyse une liste de montants de transactions (en euros).

    - Filtre les valeurs invalides (négatives ou nulles).
    - Calcule les indicateurs statistiques clés.
    - Détecte les transactions anormalement élevées (> 2x la moyenne).

    Retourne un dictionnaire structuré avec tous les résultats.
    """
    # Nettoyage : on ignore les valeurs négatives ou nulles (erreurs de saisie)
    transactions_valides = [t for t in transactions if isinstance(t, (int, float)) and t > 0]

    if not transactions_valides:
        return {"erreur": "Aucune transaction valide dans la liste fournie."}

    nombre = len(transactions_valides)
    total = sum(transactions_valides)
    moyenne = total / nombre
    mediane = statistics.median(transactions_valides)
    ecart_type = statistics.stdev(transactions_valides) if nombre > 1 else 0
    valeur_max = max(transactions_valides)
    valeur_min = min(transactions_valides)

    # Détection des anomalies : transactions > 2 fois la moyenne
    anomalies = [t for t in transactions_valides if t > 2 * moyenne]

    resultats = {
        "nombre_transactions": nombre,
        "total_ventes": round(total, 2),
        "moyenne": round(moyenne, 2),
        "mediane": round(mediane, 2),
        "ecart_type": round(ecart_type, 2),
        "valeur_max": valeur_max,
        "valeur_min": valeur_min,
        "anomalies": anomalies,
    }

    return resultats


# --- Bloc d'exécution et de test ---
if __name__ == "__main__":
    jeu_de_test = [150, 200, 89, 450, -20, 0, 1200, 310, 75, 999]

    rapport = analyser_ventes(jeu_de_test)

    print("=== Rapport d'analyse des ventes ===")
    for cle, valeur in rapport.items():
        print(f"{cle} : {valeur}")