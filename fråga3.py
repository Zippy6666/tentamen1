class ChristmasGift():
    def __init__(self, secret_gift, price, gift_to, gift_from, christmas_rhyme) -> None:
        self._secret_gift = secret_gift
        self._price = price
        self.gift_to = gift_to
        self.gift_from = gift_from
        self.christmas_rhyme = christmas_rhyme
    
    def get_secret_gift( self ):
        return self._secret_gift
    
    def get_price( self ):
        return self._price


def main():
    gifts = [
        ChristmasGift("kaffebryggare", "299 kr", "Lotta", "Erik", "Om du känner dej rastlös och nervös hjälper det föga med en fritös. Med denna present blir du säkert tryggare för jag kar köpt dej en …"),
        ChristmasGift("dammsugare", "2000 kr", "Erik", "Lotta", "christmas_rhyme2"),
        ChristmasGift("kattunge", "5000 kr", "Lisa", "Stina", "christmas_rhyme3"),
        ChristmasGift("godis", "10 kr", "Lars", "Olle", "christmas_rhyme4"),
        ChristmasGift("vr headset", "6000 kr", "Olle", "Lars", "christmas_rhyme5"),
    ]

    inp = input("Hey, who wants to look in to santas christmas sack?Hey, who wants to look in to santas christmas sack? ")

    if inp == "Santa Claus" or inp=="Mrs.Claus":
        for gift in gifts:
            print(f"Till {gift.gift_to} från {gift.gift_from} ges en gåva {gift.get_secret_gift()} till ett pris av {gift.get_price()}")

    else:
        for gift in gifts:
            print(f"Från {gift.gift_from} till {gift.gift_to}: '{gift.christmas_rhyme}")





if __name__ == "__main__":
    main()