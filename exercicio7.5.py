def cursos_ofertados():

    cursos_manha = {"Matemática", "Física", "Química", "Biologia", "Geografia"}
    cursos_noite = {"História", "Geografia", "Filosofia", "Química", "Literatura"}

    cursos_comum = cursos_manha & cursos_noite
    print("Cursos disponíveis em ambos os turnos (interseção):", cursos_comum)

    cursos_manha_unicos = cursos_manha - cursos_noite
    print("Cursos disponíveis apenas pela manhã:", cursos_manha_unicos)

    cursos_noite_unicos = cursos_noite - cursos_manha
    print("Cursos disponíveis apenas à noite:", cursos_noite_unicos)


cursos_ofertados()