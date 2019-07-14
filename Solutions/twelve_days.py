def recite(start_verse, end_verse):
    dayvalue = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
                "eleventh", "twelfth"]
    body = ["and a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ",
            "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]
    totalverse = []

    if end_verse == start_verse and end_verse > 1:
        giftcounter = start_verse - 1
        verse = "On the {0} day of Christmas my true love gave to me: ".format(dayvalue[end_verse-1])
        for j in range(end_verse):
            verse += body[giftcounter]
            giftcounter -= 1
        totalverse.append(verse)
    elif end_verse != start_verse:
        versecounter = start_verse
        for i in range(end_verse - start_verse + 1):
            giftcounter = versecounter - 1
            verse = "On the {0} day of Christmas my true love gave to me: ".format(dayvalue[versecounter-1])
            for j in range(versecounter):
                if versecounter == 1:
                    verse += "a Partridge in a Pear Tree."
                    giftcounter -= 1
                else:
                    verse += body[giftcounter]
                    giftcounter -= 1
            totalverse.append(verse)
            versecounter += 1
    else:
        verse = "On the first day of Christmas my true love gave to me: " \
               "a Partridge in a Pear Tree."  # a little hacky but easiest
        return [verse]
    return totalverse
