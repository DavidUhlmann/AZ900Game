import json
import random

def load_services(filename):
    with open(filename, 'r') as file:
        services = json.load(file)
    return services

def get_unique_categories(services):
    unique_categories = set()
    for service in services:
        unique_categories.update(service['Category'])
    return list(unique_categories)

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input

def validate_categories_input(user_input, max_options):
    input_parts = user_input.replace(" ", "").split(',')
    valid = all(part.isdigit() and 1 <= int(part) <= max_options for part in input_parts)
    return valid, [int(part) for part in input_parts if part.isdigit()] if valid else []

def main():
    filename = 'services.json'
    services = load_services(filename)
    unique_categories = get_unique_categories(services)
    play_again = 'YES'

    while play_again.upper() == 'YES':
        selected_services = random.sample(services, 10)
        score = 0
        questions_left = 10
        wrong_answers = []

        for service in selected_services:
            correct_model = None  # Initialize correct_model before the loop
            print(f"\nYou have {questions_left} questions left.")
            questions_left -= 1

            print(f"\nService: {service['id']}")
            print(f"Description: {service['Short explanation']}")

            service_score = 0

            # Responsibility model
            resp_model = get_user_input("Responsibility model (1 for IaaS, 2 for PaaS, 3 for SaaS): ")
            while resp_model not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                resp_model = get_user_input("Responsibility model (1 for IaaS, 2 for PaaS, 3 for SaaS): ")

            if (resp_model == '1' and service['shared Responsibility model'] == 'IaaS') or \
               (resp_model == '2' and service['shared Responsibility model'] == 'PaaS') or \
               (resp_model == '3' and service['shared Responsibility model'] == 'SaaS'):
                service_score += 1
            else:
                correct_model = service['shared Responsibility model']

            # Categories
            print("\nCategories:")
            for index, category in enumerate(unique_categories, 1):
                print(f"{index}. {category}")
            
            category_input = get_user_input("Enter the category numbers separated by commas (e.g., 1, 3): ")
            valid_input, selected_options = validate_categories_input(category_input, len(unique_categories))
            while not valid_input:
                print("Invalid input. Please try again using the correct format and valid numbers.")
                category_input = get_user_input("Enter the category numbers separated by commas (e.g., 1, 3): ")
                valid_input, selected_options = validate_categories_input(category_input, len(unique_categories))

            selected_categories = [unique_categories[i - 1] for i in selected_options]
            if all(category in selected_categories for category in service['Category']):
                service_score += 1
            else:
                correct_categories = ", ".join(service['Category'])

            if service_score != 2:
                wrong_answers.append((service['id'], correct_model, correct_categories))

            score += service_score

        # Scoring
        print(f"\nYour score is: {score}/20")
        if score < 10:
            print("No words bro, you need to go back to John Savill's videos.")
        elif score < 15:
            print("Sorry, you need to study more.")
        elif score < 18:
            print("Very nice, you have a clue.")
        elif score < 20:
            print("You are very good, well done!")
        else:
            print("Maestro of Azure, respect!!")

        # Displaying wrong answers
        if wrong_answers:
            print("\nHere's where you went wrong:")
            for service, model, categories in wrong_answers:
                print(f"\nService: {service}\nShared Responsibility Model: {model}\nCategories: {categories}")

        play_again = get_user_input("Do you want to play again? (YES/NO): ").upper()

if __name__ == "__main__":
    main()
