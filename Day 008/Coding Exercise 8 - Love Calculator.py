def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase for case-insensitive counting
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    true_count = (
            combined_names.count('t') +
            combined_names.count('r') +
            combined_names.count('u') +
            combined_names.count('e')
    )

    # Count letters in "LOVE"
    love_count = (
            combined_names.count('l') +
            combined_names.count('o') +
            combined_names.count('v') +
            combined_names.count('e')
    )

    # Combine counts to form a two-digit number
    love_score = int(str(true_count) + str(love_count))

    # Print the love score
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")