# ========================================================
# SECTION 1: AI BOT BRAIN (Friend 1 - Edit the if/else!)
# ========================================================
def decide_bot_action(distance, bot_health, can_see_player):
    # Valid return words: "SHOOT", "CHASE", "RETREAT", "PATROL"
    if bot_health < 35:
        return "RETREAT"
    elif can_see_player and distance < 22:
        return "SHOOT"
    elif can_see_player:
        return "CHASE"
    else:
        return "PATROL"


# ========================================================
# SECTION 2: SKILL ANALYZER (Friend 2 - Edit the ranks!)
# ========================================================
def analyze_player_skill(kills, deaths, shots_fired, shots_hit):
    if shots_fired > 0:
        accuracy = (shots_hit / shots_fired) * 100
    else:
        accuracy = 0.0

    if kills >= 8 and accuracy >= 45:
        rank = "APEX PREDATOR"
        tip = "Unstoppable aim and movement!"
    elif kills >= 4 and accuracy >= 25:
        rank = "SHARPSHOOTER"
        tip = "Great shots! Keep strafing while firing."
    elif shots_fired > 10 and accuracy < 20:
        rank = "SPRAY & PRAY"
        tip = "Slow down and line up the crosshair first."
    else:
        rank = "ROOKIE"
        tip = "Use the walls for cover and watch your ammo!"

    return f"RANK: {rank}\nAccuracy: {round(accuracy, 1)}% ({shots_hit}/{shots_fired})\nTip: {tip}"
