def distance_parcourue_par_semaine(nb_marches, hauteur_marche_cm):
    trajets_par_jour = 5 * 2
    jours_par_semaine = 7

    distance_totale_cm = nb_marches * hauteur_marche_cm * trajets_par_jour * jours_par_semaine

    distance_totale_m = distance_totale_cm / 100

    print(f"Pour {nb_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_totale_m:.2f} m par semaine.")

distance_parcourue_par_semaine(10, 20)
