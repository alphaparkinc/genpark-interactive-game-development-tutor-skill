from client import InteractiveGameDevelopmentTutorClient

def main():
    client = InteractiveGameDevelopmentTutorClient()
    res = client.teach_game_dev("2D Platformer", "beginner")
    print("Lesson Plan:")
    for lesson in res["lesson_plan"]:
        print(f"  - {lesson}")
    print("Starter Code:")
    print(res["starter_code"])

if __name__ == "__main__":
    main()
