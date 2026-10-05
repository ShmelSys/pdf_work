import os
from pypdf import PdfWriter

def fusionner_pdfs(dossier_entree="docs_in", fichier_sortie="pdf_fusionne.pdf"):
    # On vérifie si le dossier docs_in existe
    if not os.path.exists(dossier_entree):
        print(f"Erreur : Le dossier '{dossier_entree}' n'existe pas dans le répertoire courant.")
        return

    # On récupère tous les fichiers se terminant par .pdf
    fichiers_pdf = [f for f in os.listdir(dossier_entree) if f.lower().endswith('.pdf')]
    
    # On trie les fichiers par ordre alphabétique pour que l'ordre de fusion soit logique
    fichiers_pdf.sort()

    if not fichiers_pdf:
        print(f"Aucun fichier PDF trouvé dans le dossier '{dossier_entree}'.")
        return

    # Initialisation de l'outil de fusion
    fusionneur = PdfWriter()

    # Parcours des fichiers et ajout à la fusion
    for nom_fichier in fichiers_pdf:
        chemin_complet = os.path.join(dossier_entree, nom_fichier)
        print(f"Ajout du fichier : {nom_fichier}")
        fusionneur.append(chemin_complet)

    # Sauvegarde du fichier final
    with open(fichier_sortie, "wb") as fichier_final:
        fusionneur.write(fichier_final)
    
    print(f"\nFusion terminée avec succès !")
    print(f"Le fichier regroupant tous les documents a été créé sous le nom : {fichier_sortie}")

if __name__ == "__main__":
    fusionner_pdfs()