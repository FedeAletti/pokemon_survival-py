import random
from pprint import pprint
from pokeloads import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cual es tu nombre?\n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player):
    print("Elige con que pokemon lucharás")
    for index in range(len(player["pokemon_inventory"])):
        print("{} - {}".format(index,
              get_pokemon_info(player["pokemon_inventory"][index])))
    try:
        return player["pokemon_inventory"][int(input("¿Cual eliges? "))]
    except (ValueError, IndexError):
        print("Opcion inválida, vuelve a elegir.")
        choose_pokemon(player)


def get_pokemon_info(pokemon):
    return "{} | lvl: {} | hp: {}/{}".format(pokemon["name"],
                                             pokemon["level"],
                                             pokemon["current_health"],
                                             pokemon["base_health"])


def player_attack():
    # Implementar multiplicadores en base al tipo de pokemon
    """
    Normal: débil frente a Lucha
    Fuego: débil frente a Agua, Tierra, Roca
    Agua: débil frente a Planta, Eléctrico
    Planta: débil frente a Fuego, Hielo, Veneno, Volador, Bicho
    Eléctrico: débil frente a Tierra
    Hielo: débil frente a Fuego, Lucha, Roca, Acero
    Lucha: débil frente a Volador, Psíquico, Hada
    Veneno: débil frente a Tierra, Psíquico
    Tierra: débil frente a Agua, Planta, Hielo
    Volador: débil frente a Eléctrico, Hielo, Roca
    Psíquico: débil frente a Bicho, Fantasma, Siniestro
    Bicho: débil frente a Volador, Roca, Fuego
    Roca: débil frente a Agua, Planta, Lucha, Tierra, Acero
    Fantasma: débil frente a Fantasma, Siniestro
    Dragón: débil frente a Hielo, Dragón, Hada
    Siniestro: débil frente a Lucha, Bicho, Hada
    Acero: débil frente a Fuego, Lucha, Tierra
    Hada: débil frente a Veneno, Acero


    Multiplicar el ataque * 1.25

    Cuando se elige el ataque del usuario se muestran solo los disponibles en ese nivel

    """
    pass


def enemy_attack():
    pass


def assign_xp(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

        while pokemon["current_exp"] > 20:
            pokemon["current_exp"] -= 20
            pokemon["level"] += 1
            pokemon["current_health"] = pokemon["base_health"]
            print("Tu pokemon ha subido al nivel {}".format(
                get_pokemon_info(pokemon)))

def capture_pokemon(enemy, player):
    pass

def cure_pokemon(player, player_pokemon):
    pass

def fight(player, enemy):
    print("--- NUEVO COMBATE ---")

    attack_history = []

    player_pokemon = choose_pokemon(player)
    print("Contrincantes: {} vs {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy)))

    while any_player_pokemon_lives(player) and enemy["current_health"] > 0:

        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input(
                "¿Qué deseas hacer? [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar")

        if action == "A":
            player_attack(player_pokemon, enemy)
            attack_history.append(player_pokemon)
        elif action == "P":
            # Si tiene pokeballs, se tira una con una probabilidad de capturarlo
            # relativa a la salud restante de {enemy}
            # Cuando se captura pasa al inventario del jugador con la vida que trae
            capture_pokemon(enemy, player)
        elif action == "V":
            # Si el usuario tiene curas en el inventario, cura 50 hasta 100
            # Si no tiene, no se cura
            cure_pokemon(player, player_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player)

        enemy_attack(enemy, player_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player):
            player_pokemon = choose_pokemon(player)

    if enemy["current_health"] == 0:
        print("Has ganado!")
        assign_xp(attack_history)

    input("Presiona ENTER para continuar")

    print("--- FIN COMBATE ---")

def item_lottery(player_profile):
    """
    Segun factor aleatorio le toca una pokeb o una cura
    """

def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)

    

    print("Has perdido en el combate n{}".formate(player_profile["combats"]))


if __name__ == "__main__":
    main()


"""

______________________TO DO

Devolver vida a 0 cuando sean negativo

assign_xp()

        if action == "A":   
            player_attack(player_pokemon, enemy)
            attack_history.append(player_pokemon)
            enemy_attack(enemy,player_pokemon)
        elif action == "P":
            # Si tiene pokeballs, se tira una con una probabilidad de capturarlo 
            # relativa a la salud restante de {enemy}
            # Cuando se captura pasa al inventario del jugador con la vida que trae
            capture_pokemon(enemy, player)
        elif action == "V":
            # Si el usuario tiene curas en el inventario, cura 50 hasta 100
            # Si no tiene, no se cura
            cure_pokemon(player, player_pokemon)

"""
