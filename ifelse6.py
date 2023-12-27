male_birth_day = int(input("Enter birth day for male: "))
male_birth_month = int(input("Enter birth month for male: "))
female_birth_day = int(input("Enter birth day for female: "))
female_birth_month = int(input("Enter birth month for female: "))

male_sign = ""
female_sign = ""

# Determine male zodiac sign
if male_birth_month == 12 and male_birth_day >= 22 or male_birth_month == 1 and male_birth_day <= 19:
    male_sign = "Capricorn"
elif male_birth_month == 1 and male_birth_day >= 20 or male_birth_month == 2 and male_birth_day <= 18:
    male_sign = "Aquarius"
elif male_birth_month == 2 and male_birth_day >= 19 or male_birth_month == 3 and male_birth_day <= 20:
    male_sign = "Pisces"
elif male_birth_month == 3 and male_birth_day >= 21 or male_birth_month == 4 and male_birth_day <= 19:
    male_sign = "Aries"
elif male_birth_month == 4 and male_birth_day >= 20 or male_birth_month == 5 and male_birth_day <= 20:
    male_sign = "Taurus"
elif male_birth_month == 5 and male_birth_day >= 21 or male_birth_month == 6 and male_birth_day <= 20:
    male_sign = "Gemini"
elif male_birth_month == 6 and male_birth_day >= 21 or male_birth_month == 7 and male_birth_day <= 22:
    male_sign = "Cancer"
elif male_birth_month == 7 and male_birth_day >= 23 or male_birth_month == 8 and male_birth_day <= 22:
    male_sign = "Leo"
elif male_birth_month == 8 and male_birth_day >= 23 or male_birth_month == 9 and male_birth_day <= 22:
    male_sign = "Virgo"
elif male_birth_month == 9 and male_birth_day >= 23 or male_birth_month == 10 and male_birth_day <= 22:
    male_sign = "Libra"
elif male_birth_month == 10 and male_birth_day >= 23 or male_birth_month == 11 and male_birth_day <= 21:
    male_sign = "Scorpio"
elif male_birth_month == 11 and male_birth_day >= 22 or male_birth_month == 12 and male_birth_day <= 21:
    male_sign = "Sagittarius"
else:
    male_sign = "Invalid input"

if female_birth_month == 12 and female_birth_day >= 22 or female_birth_month == 1 and female_birth_day <= 19:
    female_sign = "Capricorn"
elif female_birth_month == 1 and female_birth_day >= 20 or female_birth_month == 2 and female_birth_day <= 18:
    female_sign = "Aquarius"
elif female_birth_month == 2 and female_birth_day >= 19 or female_birth_month == 3 and female_birth_day <= 20:
    female_sign = "Pisces"
elif female_birth_month == 3 and female_birth_day >= 21 or female_birth_month == 4 and female_birth_day <= 19:
    female_sign = "Aries"
elif female_birth_month == 4 and female_birth_day >= 20 or female_birth_month == 5 and female_birth_day <= 20:
    female_sign = "Taurus"
elif female_birth_month == 5 and female_birth_day >= 21 or female_birth_month == 6 and female_birth_day <= 20:
    female_sign = "Gemini"
elif female_birth_month == 6 and female_birth_day >= 21 or female_birth_month == 7 and female_birth_day <= 22:
    female_sign = "Cancer"
elif female_birth_month == 7 and female_birth_day >= 23 or female_birth_month == 8 and female_birth_day <= 22:
    female_sign = "Leo"
elif female_birth_month == 8 and female_birth_day >= 23 or female_birth_month == 9 and female_birth_day <= 22:
    female_sign = "Virgo"
elif female_birth_month == 9 and female_birth_day >= 23 or female_birth_month == 10 and female_birth_day <= 22:
    female_sign = "Libra"
elif female_birth_month == 10 and female_birth_day >= 23 or female_birth_month == 11 and female_birth_day <= 21:
    female_sign = "Scorpio"
elif female_birth_month == 11 and female_birth_day >= 22 or female_birth_month == 12 and female_birth_day <= 21:
    female_sign = "Sagittarius"
else:
    female_sign = "Invalid input"


print("Male zodiac sign:", male_sign)
print("Female zodiac sign:", female_sign)
