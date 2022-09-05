from tkinter import *
from tkinter import font, messagebox
import random

tim = Tk()
tim.geometry('800x800+300+0')
tim.config(bg="#170055", padx=30, pady=0)
fonts = list(font.families())
style = (fonts[13], 20, "bold")
seconds = 90
resume = True

with open("score.txt", mode="r") as file:
    score = float(file.readline())


def check_result():
    global seconds, resume
    corrects = 0
    errors = 0
    input_list = list(the_input.get(1.0, "end-1c").split())
    my_len = len(input_list)
    chosen_list = list(chosen_text.split())[0:my_len]
    for i in range(my_len):
        if input_list[i] == chosen_list[i]:
            corrects += 1
        else:
            errors += 1
    try:
        answer = round(((my_len-errors)/5)/((90 - seconds)/60), 2)
        result.config(text=f"{answer}")
        if answer > score:
            with open("score.txt", "w") as new:
                new.write(f"{answer}")
            resume = False
            messagebox.showinfo("result", f"yay! you made a highscore\nyour wpm is {answer}")
        else:
            resume = False
            messagebox.showinfo("result", f"your wpm is {answer}")

    except ZeroDivisionError:
        corrects = 0
        errors = 0
        input_list = list(the_input.get(1.0, "end-1c").split())
        my_len = len(input_list)
        chosen_list = list(chosen_text.split())[0:my_len]
        for i in range(my_len):
            if input_list[i] == chosen_list[i]:
                corrects += 1
            else:
                errors += 1

        answer = round(((my_len - errors) / 5), 2)
        result.config(text=f"{answer}")
        if answer > score:
            with open("score.txt", "w") as new:
                new.write(f"{answer}")
            resume = False
            messagebox.showinfo("result", f"yay! you made a highscore\nyour wpm is {answer}")
        else:
            resume = False
            messagebox.showinfo("result", f"your wpm is {answer}")


def start_timer():
    global seconds, resume
    the_input.config(state=NORMAL)
    the_input.focus()
    colors = ["#B9FFF8", "#FEDB39", "#F637EC", "#00FFAB", "#9FB4FF", "#E8FFC2", "#C2FFD9"]
    if resume:
        seconds -= 1

    if seconds == -1:
        check_result()
    elif seconds < 10 and resume:
        time.config(text=f"{seconds}", fg="red")
    else:
        time.config(text=f"{seconds}", fg=random.choice(colors))
    if seconds >= 0 and resume:
        tim.after(ms=1000, func=start_timer)


def exit():
    tim.destroy()


text_list = ["The Moon is a barren, rocky world without air and water. It has dark lava plain on its surface. The Moon is filled wit craters. It has no light of its own. It gets its light from the Sun. The Moo keeps changing its shape as it moves round the Earth. It spins on its axis in 27.3 days stars were named after the Edwin Aldrin were the first ones to set their foot on the Moon on 21 July 1969 They reached the Moon in their space craft named Apollo II.",
             "The sun is a huge ball of gases. It has a diameter of 1,392,000 km. It is so huge that it can hold millions of planets inside it. The Sun is mainly made up of hydrogen and helium gas. The surface of the Sun is known as the photosphere. The photosphere is surrounded by a thin layer of gas known as the chromospheres. Without the Sun, there would be no life on Earth. There would be no plants, no animals and no human beings. As, all the living things on Earth get their energy from the Sun for their survival.",
             "The Solar System consists of the Sun Moon and Planets. It also consists of comets, meteoroids and asteroids. The Sun is the largest member of the Solar System. In order of distance from the Sun, the planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto; the dwarf planet. The Sun is at the centre of the Solar System and the planets, asteroids, comets and meteoroids revolve around it.",
             "The Mahabharata is a story about a great battle between the Kauravas and the Pandavas. The battle was fought in Kurukshetra near Delhi. Many kings and princes took part in the battle. The Pandavas defeated the Kauravas. The Bhagvad Gita is a holy book of the Hindus. It is a part of the Mahabharata. Then, Lord Rama, with the help of It is a book of collection of teachings of Lord Krishna to Arjuna in the battlefield. It is the longest epic in the world.",
             "The Ramayana is a story of Lord Rama written by the SageValmiki. Lord Rama, the prince of Ayodhya, in order to help his father Dasharatha went to exile for fourteen years. His wife, Sita and his younger brother Lakshmana also went with him. He went through many difficulties in the forest. One day Ravana, the king of Lanka carried away Sita with him. Then, Lord Rama, with the help of Hanumana, defeated and killed Ravana; Sita, Rama and Lakshmana returned to Ayod hya after their exile.",
             "The Taj Mahal is a beautiful monument built in 1631 by an Emperor named Shah Jahan in memory of his wife Mumtaz Mahal. It is situated on the banks of river Yamuna at Agra. It looks beautiful in the moonlight. The Taj Mahal is made up of white marble. In front of the monument, there is a beautiful garden known as the Charbagh. Inside the monument, there are two tombs. These tombs are of Shah Jahan and his wife Mumtaz Mahal. The Taj Mahal is considered as one of the Seven Wonders of the World. Many tourists come to see this beautiful structure from different parts of the world.",
             "Delhi is the capital of India. It is situated on the banks of the river Yamuna. It is surrounded by Haryanaand Uttar Pradesh. It has some of the famous buildings and monuments such as the Qutub Minar, Reu Fort, Lotus Temple, Akshardham Temple etc. Some of the monuments are hundreds of years old. Apart from this, there is the Parliament House, the Central Secretariat and the famous Connaught place. Delhi is a beautiful city. But, it is becoming very crowded and polluted. I love Delhi a lot.",
             "A snake charmer is a person who moves the streets with different types of the banks of the river Yamuna. It is snakes in his basket. He goes from one place to another to show various types of snakes and their tricks. He carries a pipe with which he plays music and snakes dance to his tune. He usually wears a colourful dress. The job of a snake charmer is quite dangerous. Some snakes are quite poisonous and can even bite him. It is not an easy task to catch and train them for the shows.",
             "A street beggar can be seen everywhere; at the bus stop, railway stations, religious places, markets etc. Some beggars are crippled, lame and some are blind. They are unable to earn their livelihood. Whereas some are healthy and they do not deserve our sympathy. We should see that they take up some profession. They should not be allowed to beg. On my way to school I see a beggar daily. He wears old rags. He is partially blind. I feel pity seeing him but I can’t help it I can only pray to God to help him to earn his livelihood.",
             "The doctor is a person who looks after the sick people and prescribes medicines so that the patient recovers fast. In order to become a doctor, a person has to study medicine. Doctors lead a hard life. Their life is very busy. They get up early in the morning and go to the hospital. They work without taking a break. They always remain polite so that patients feel comfortable with them. Since doctors work so hard we must realise their value.",
             "A hawker is a person who moves from one place to another and sell their goods, by shouting on the streets. They work hard throughout the day. They move on the street on their bicycle and sometimes on foot and sell their products. We can see hawkers everywhere. They move everywhere selling their goods without caring about the weather. There is a hawker who sells vegetables on his bicycle in our locality. His name is Manoj. He brings fresh vegetables at a very reasonable price. He is a nice and an honest hawker.",
             "India is an agricultural country. Most of the people live in villages and are farmers. They grow cereals, pulses, vegetables and fruits. The farmers lead a tough life. They get up early in the morning and go to the fields. They stay and work on the farm late till evening. The farmers usually live in kuchcha houses. Though, they work hard they remain poor. Farmers eat simple food; wear simple clothes and rear animals like cows, buffaloes and oxen. Without them there would be no cereals for us to eat. They play an important role in the growth and economy of a country."]


timer = Label(text="Timer",  font=(fonts[13], 20, "bold"), fg="white", bg="#170055")
timer.grid(row=0, column=0, pady=10)

time = Label(text=f"{seconds}",  font=(fonts[13], 20, "bold"), fg="white", bg="#170055")
time.grid(row=1, column=0)

title = Label(text="Let's check your typing speed!",  font=(fonts[13], 20, "bold"), fg="#FEDB39", bg="#170055")
title.grid(row=0, column=1, rowspan=2)


highest = Label(text="highest wpm",  font=(fonts[13], 20, "bold"), fg="white", bg="#170055")
highest.grid(row=0, column=2)

highest_wpm = Label(text=f"{score}",  font=(fonts[13], 20, "bold"), fg="white", bg="#170055")
highest_wpm.grid(row=1, column=2)

sample_text = Label(text="SAMPLE TEXT", font=(fonts[13], 10, "bold"), bg="#F5EDDC")
sample_text.grid(row=2, column=0, pady=10, columnspan=3)

chosen_text = random.choice(text_list)

the_text = Label(text=chosen_text, font=(fonts[13], 15, "bold"), bg="#F5EDDC", width=60, height=13, wraplength=500)
the_text.grid(row=3, column=0, pady=10, columnspan=3)

start = Button(text="Start", font=(fonts[13], 10, "bold"), bg="#B9FFF8", command=start_timer)
start.grid(row=4, column=0, pady=10, columnspan=3)

the_input = Text(width=60, height=8, font=(fonts[13], 15, "bold"), state=DISABLED)
the_input.grid(row=5, column=0, columnspan=3)

submit = Button(text="submit", font=(fonts[13], 10, "bold"), bg="#B9FFF8", command=check_result)
submit.grid(row=6, column=0, pady=10)

exit = Button(text="exit", font=(fonts[13], 10, "bold"), bg="#B9FFF8", command=exit)
exit.grid(row=6, column=1, pady=10)

result = Label(text="0.0", font=(fonts[13], 20, "bold"), fg="white", bg="#170055")
result.grid(row=6, column=2)

tim.mainloop()













