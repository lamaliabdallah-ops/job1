def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_5 = ((note // 5) + 1) * 5
            if prochain_multiple_5 - note < 3:
                notes_arrondies.append(prochain_multiple_5)
            else:
                notes_arrondies.append(note)
    
    return notes_arrondies

notes_etudiants = [38, 40, 42, 83, 82, 99]
print(arrondir_notes(notes_etudiants))
