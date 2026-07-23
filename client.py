class InteractiveGameDevelopmentTutorClient:
    def teach_game_dev(self, game_genre: str, user_level: str = "beginner") -> dict:
        lessons = [
            "Module 1: Physics gravity & collision detection basics",
            "Module 2: Player movement controller script",
            "Module 3: Score tracking and UI game-over screen"
        ]
        code = f"// Starter code for {game_genre} ({user_level.upper()})\nfunction update(dt) {{\n  player.x += player.vx * dt;\n}}"
        return {
            "lesson_plan": lessons,
            "starter_code": code
        }
