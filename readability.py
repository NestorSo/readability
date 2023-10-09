from cs50 import get_string


def main():
    PromedioLetras = 0
    PromedioOraciones = 0
    text = ""
    text = get_string("Digite el texto del libro: ")
    PromedioLetras = (count_letters(text) / count_palabras(text)) * 100
    PromedioOraciones = (count_oraciones(text) / count_palabras(text)) * 100
    grade = CalculateGrade(PromedioOraciones, PromedioLetras)
    if grade < 1:
        print("Before Grade 1\n")
    elif grade >= 16:
        print("Grade 16+\n")
    else:
        print("Grade %d\n", grade)


def count_letters(text):
    letters = 0
    for i in text:
        if i.isalpha() == True:
            letters += 1

    return letters


def count_palabras(text):
    words = 1
    for i in text:
        if i == " ":
            words += 1

    return words


def count_oraciones(text):
    sentences = 0
    for i in text:
        if i == "." or i == "!" or i == "?":
            sentences += 1

    return sentences


def CalculateGrade(PromedioOraciones, PromedioLetras):
    index = 0
    index = round(0.0588 * PromedioLetras - 0.296 * PromedioOraciones - 15.8)
    return index


main()
