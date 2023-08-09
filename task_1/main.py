def count_vowels(word):
    vowels = "aeiouаеёиоуыэюя"  # Гласные буквы
    count = 0
    for char in word:
        if char.lower() in vowels:  # Преобразуем в нижний регистр перед проверкой
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split()
    vowel_counts = [count_vowels(phrase.replace('-', '')) for phrase in phrases]
    
    if len(set(vowel_counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def main():
    poem = input("Введите стихотворение Винни-Пуха: ")
    result = check_rhythm(poem)
    print(result)

if __name__ == "__main__":
    main()
